"""
NeuroBridge - Learn at Your Pace. Grow with Confidence.

A Python-only Streamlit learning-support prototype for children with
dyslexia and other reading difficulties (Class 12 AI project).

Run with:   streamlit run app.py

This file contains the app logic. All stories, questions and game content
live in content.py (plain Python lists and dictionaries).
"""

import json
import os
import random
import re
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import streamlit as st

from content import (
    BUILD_WORDS, CLASS_LEVELS, DIFFICULTIES, LEVELS, LETTER_SOUND_ROUNDS,
    MATHS_BANK, MATHS_TOPICS, QUOTES, STORIES, STORY_ORDER_ROUNDS,
    WORD_PICTURE_ROUNDS,
)

st.set_page_config(page_title="NeuroBridge", page_icon="🧠", layout="wide")

PROGRESS_FILE = Path(__file__).with_name("neurobridge_progress.json")
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

PAGES = [
    "🏠 Home / Student Dashboard",
    "📖 Reading Practice",
    "🎯 Quizzes & Games",
    "👩‍🏫 Parent/Teacher Dashboard",
]
PAGE_HOME, PAGE_READING, PAGE_QUIZ, PAGE_DASH = PAGES

SECTION_MATHS = "🔢 Maths Quizzes"
SECTION_GAMES = "🎮 Reading Games"

DEFAULT_PREFS = {
    "font": "Standard readable font",
    "background": "White",
    "size": "Medium",
    "spacing": "Normal",
    "emphasis": True,
}


# ======================================================================
# 1. SAVING AND LOADING PROGRESS (local JSON file)
# ======================================================================
def save_progress(data):
    """Write the progress dictionary to neurobridge_progress.json."""
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return True
    except OSError:
        return False


def load_progress():
    """Read the progress file. Creates it if missing; copes with bad JSON."""
    if not PROGRESS_FILE.exists():
        data = {"activities": []}
        if not save_progress(data):
            st.session_state["file_message"] = (
                "Progress could not be saved on this computer (file is not writable)."
            )
        return data
    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, dict) or not isinstance(data.get("activities"), list):
            raise ValueError("unexpected file layout")
        return data
    except (json.JSONDecodeError, ValueError, OSError):
        # Keep the damaged file as a backup, then start a fresh one.
        try:
            PROGRESS_FILE.replace(PROGRESS_FILE.with_name("neurobridge_progress_damaged.json"))
        except OSError:
            pass
        st.session_state["file_message"] = (
            "The progress file was damaged, so a fresh one was started. "
            "The old one was kept as neurobridge_progress_damaged.json."
        )
        data = {"activities": []}
        save_progress(data)
        return data


def record_activity(activity_type, name, score, total, extra=None):
    """Add ONE finished activity to the progress file. Returns True if saved."""
    entry = {
        "type": activity_type,          # "story", "maths" or "game"
        "name": name,
        "score": score,
        "total": total,
        "timestamp": datetime.now().strftime(TIME_FORMAT),
    }
    if extra:
        entry.update(extra)
    data = load_progress()
    data["activities"].append(entry)
    return save_progress(data)


def get_records():
    """Return only well-formed activity records from the file."""
    records = []
    for item in load_progress()["activities"]:
        try:
            if (item["type"] in ("story", "maths", "game")
                    and int(item["total"]) > 0 and 0 <= int(item["score"]) <= int(item["total"])):
                datetime.strptime(item["timestamp"], TIME_FORMAT)
                records.append(item)
        except (KeyError, TypeError, ValueError):
            continue
    return records


# ======================================================================
# 2. OPTIONAL TEXT-TO-SPEECH (pure Python: pyttsx3 -> audio file -> st.audio)
# ======================================================================
@st.cache_data(show_spinner=False)
def make_speech(text):
    """Turn text into audio bytes with pyttsx3. Returns (bytes, mime) or None."""
    try:
        import pyttsx3
    except ImportError:
        return None
    temp_path = None
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 140)  # a little slower for learners
        handle, temp_path = tempfile.mkstemp(suffix=".wav")
        os.close(handle)
        engine.save_to_file(text, temp_path)
        engine.runAndWait()
        engine.stop()
        with open(temp_path, "rb") as file:
            audio = file.read()
        if len(audio) < 100:
            return None
        mime = "audio/aiff" if audio[:4] == b"FORM" else "audio/wav"
        return audio, mime
    except Exception:  # speech engines fail in many different ways
        return None
    finally:
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError:
                pass


def speak_button(text, key, label="🔊 Listen"):
    """A button that plays the text aloud, with a friendly fallback."""
    if st.button(label, key=key):
        result = make_speech(text)
        if result:
            st.audio(result[0], format=result[1])
        else:
            st.info(
                "🔇 Audio is not available on this computer. "
                "Read slowly, one sentence at a time, or ask a grown-up to read with you."
            )


# ======================================================================
# 3. SMALL HELPERS FOR SESSION STATE
# ======================================================================
def init_state():
    defaults = {
        "logged_in": False,
        "student_name": "Student",
        "student_class": "",
        "prefs": dict(DEFAULT_PREFS),
        "last_page": None,
        "quote": random.choice(QUOTES),
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def set_choice(state_key, value):
    """Set a 'sticky' choice (and its widget) from inside a callback."""
    st.session_state[state_key] = value
    st.session_state["w_" + state_key] = value


def sticky_choice(label, options, state_key, kind="radio", horizontal=True):
    """
    A radio/selectbox whose value is remembered even when the user visits
    another page (Streamlit forgets widgets that are not drawn).
    """
    if st.session_state.get(state_key) not in options:
        st.session_state[state_key] = options[0]
    widget_key = "w_" + state_key
    if st.session_state.get(widget_key) not in options:
        st.session_state.pop(widget_key, None)   # options changed: start again

    def remember():
        st.session_state[state_key] = st.session_state[widget_key]

    # Only give a starting index when the widget has no value yet.
    start = {} if widget_key in st.session_state else {"index": options.index(st.session_state[state_key])}
    if kind == "radio":
        st.radio(label, options, key=widget_key, on_change=remember, horizontal=horizontal, **start)
    else:
        st.selectbox(label, options, key=widget_key, on_change=remember, **start)
    return st.session_state[state_key]


def go_to(page, section_key=None, section_value=None):
    """Callback used by dashboard cards to move to a page/section."""
    st.session_state["nav_page"] = page
    if section_key:
        set_choice(section_key, section_value)


def percent(score, total):
    return round(100 * score / total)


def encouragement(score, total):
    ratio = score / total
    if ratio == 1:
        return "🌟 Perfect score! You are a superstar!"
    if ratio >= 0.6:
        return "😊 Great work! You are getting stronger every time."
    return "💪 Good try! Every attempt helps you learn. Try again when you are ready."


# ======================================================================
# 4. READING SETTINGS AND TEXT DISPLAY (Streamlit built-ins only)
# ======================================================================
def split_sentences(paragraph):
    parts = re.split(r'(?<=[.!?”"])\s+', paragraph.strip())
    return [part for part in parts if part]


def show_reading_text(text, highlight_word=None, bold=False):
    """
    Show text using the student's preferences:
    size    -> Markdown heading level (built-in Streamlit text sizes)
    spacing -> extra spacing puts each sentence on its own line
    background -> st.info (pale blue), st.warning (cream) or a white bordered box
    """
    prefs = st.session_state["prefs"]
    prefix = {"Small": "", "Medium": "#### ", "Large": "### "}[prefs["size"]]
    if highlight_word:
        text = re.sub(rf"\b({re.escape(highlight_word)})\b", r":orange-background[\1]", text,
                      flags=re.IGNORECASE)
    pieces = split_sentences(text) if prefs["spacing"] == "Extra spacing" else [text]
    if bold:
        pieces = [f"**{piece}**" for piece in pieces]
    body = "\n\n".join(prefix + piece for piece in pieces)
    if prefs["background"] == "Pale blue":
        st.info(body)
    elif prefs["background"] == "Cream":
        st.warning(body)
    else:
        with st.container(border=True):
            st.markdown(body)


def pref_widget(label, key, options):
    prefs = st.session_state["prefs"]

    def save():
        st.session_state["prefs"][key] = st.session_state["w_pref_" + key]

    start = {} if "w_pref_" + key in st.session_state else {"index": options.index(prefs[key])}
    st.selectbox(label, options, key="w_pref_" + key, on_change=save, **start)


def reading_settings_panel():
    prefs = st.session_state["prefs"]
    st.write("Choose how reading text looks. Your choices are used on the Reading Practice page.")
    pref_widget("Font", "font", ["Standard readable font", "Dyslexia-friendly font (needs setup)"])
    if prefs["font"].startswith("Dyslexia"):
        st.caption(
            "ℹ️ Python cannot change fonts by itself. This choice is remembered, but the "
            "font only changes if the computer owner adds a font in the theme settings "
            "(see README)."
        )
    pref_widget("Reading background", "background", ["White", "Cream", "Pale blue"])
    pref_widget("Text size", "size", ["Small", "Medium", "Large"])
    pref_widget("Line spacing", "spacing", ["Normal", "Extra spacing"])
    st.caption("Extra spacing puts each sentence on its own line.")

    def save_emphasis():
        st.session_state["prefs"]["emphasis"] = st.session_state["w_pref_emphasis"]

    start = {} if "w_pref_emphasis" in st.session_state else {"value": prefs["emphasis"]}
    st.checkbox("Highlight the current paragraph and let me pick a word to highlight",
                key="w_pref_emphasis", on_change=save_emphasis, **start)
    st.caption("Preview:")
    show_reading_text("The little bird flew over the hills.")


# ======================================================================
# 5. GENERIC MULTIPLE-CHOICE QUIZ ENGINE (used by stories and maths)
# ======================================================================
def prepare_questions(raw_questions):
    """Shuffle the answer options once so the correct one is not always first."""
    prepared = []
    for item in raw_questions:
        options = list(item["options"])
        random.shuffle(options)
        prepared.append({"q": item["q"], "options": options,
                         "answer": item["answer"], "explain": item["explain"]})
    return prepared


def maths_questions(topic, difficulty):
    bank = MATHS_BANK[topic][difficulty]
    chosen = random.sample(bank, min(5, len(bank)))
    return [{"q": q, "options": [right] + list(wrong), "answer": right, "explain": explain}
            for q, right, wrong, explain in chosen]


def start_quiz(key, raw_questions, meta, rebuild=None):
    """Create a fresh quiz in session state. `rebuild` makes new questions on retry."""
    st.session_state[key] = {
        "questions": prepare_questions(raw_questions),
        "index": 0, "score": 0, "status": "asking", "first_try": True,
        "saved": False, "save_failed": False, "meta": meta,
        "raw": raw_questions, "rebuild": rebuild,
    }


def quiz_answer(key, option):
    quiz = st.session_state[key]
    question = quiz["questions"][quiz["index"]]
    quiz["chosen"] = option
    if option == question["answer"]:
        quiz["status"] = "correct"
        if quiz["first_try"]:
            quiz["score"] += 1
    else:
        quiz["status"] = "wrong"
        quiz["first_try"] = False


def quiz_retry_question(key):
    st.session_state[key]["status"] = "asking"


def quiz_next(key):
    quiz = st.session_state[key]
    quiz["index"] += 1
    quiz["status"] = "asking"
    quiz["first_try"] = True


def quiz_restart(key):
    quiz = st.session_state[key]
    raw = quiz["rebuild"]() if quiz["rebuild"] else quiz["raw"]
    start_quiz(key, raw, quiz["meta"], quiz["rebuild"])


def render_quiz(key):
    """Draw the current quiz question or the final score. Saves ONCE at the end."""
    quiz = st.session_state[key]
    questions = quiz["questions"]
    total = len(questions)

    # ----- finished: show score and save exactly once -----
    if quiz["index"] >= total:
        if not quiz["saved"]:
            meta = quiz["meta"]
            extra = {k: v for k, v in meta.items() if k not in ("type", "name")}
            ok = record_activity(meta["type"], meta["name"], quiz["score"], total, extra)
            quiz["saved"] = True
            quiz["save_failed"] = not ok
        st.subheader(f"🏁 You scored {quiz['score']} out of {total}")
        st.success(encouragement(quiz["score"], total))
        if quiz["save_failed"]:
            st.warning("Your score could not be saved on this computer.")
        else:
            st.caption("✅ Your result was saved.")
        st.button("🔁 Try the quiz again", key=f"{key}_again", on_click=quiz_restart, args=(key,))
        return True

    # ----- one question at a time -----
    question = questions[quiz["index"]]
    st.progress(quiz["index"] / total, text=f"Question {quiz['index'] + 1} of {total}")
    st.markdown(f"## {question['q']}")

    if quiz["status"] == "asking":
        for number, option in enumerate(question["options"]):
            st.button(option, key=f"{key}_{quiz['index']}_{number}", width="stretch",
                      on_click=quiz_answer, args=(key, option))
    else:
        for option in question["options"]:
            if option == question["answer"]:
                st.success(f"✅ {option}")
            elif option == quiz.get("chosen"):
                st.error(f"❌ {option}")
            else:
                st.write(f"▫️ {option}")
        if quiz["status"] == "correct":
            st.success("🎉 Correct! Well done.")
        else:
            st.error("Not quite. Let's look at it together.")
        st.info(f"💡 {question['explain']}")
        left, right = st.columns(2)
        if quiz["status"] == "wrong":
            left.button("🔄 Try this question again", key=f"{key}_retry_{quiz['index']}",
                        on_click=quiz_retry_question, args=(key,), width="stretch")
        last = quiz["index"] == total - 1
        right.button("See my score ➡️" if last else "Next question ➡️",
                     key=f"{key}_next_{quiz['index']}", on_click=quiz_next, args=(key,),
                     type="primary", width="stretch")
    return False


# ======================================================================
# 6. PAGE 1 - HOME / STUDENT DASHBOARD
# ======================================================================
def do_login():
    name = st.session_state.get("in_name", "").strip()
    st.session_state["student_name"] = name or "Student"
    st.session_state["student_class"] = st.session_state.get("in_class", "").strip()
    st.session_state["logged_in"] = True
    st.session_state["in_pass"] = ""     # the demo never keeps passwords


def do_demo_mode():
    st.session_state["student_name"] = "Student"
    st.session_state["student_class"] = ""
    st.session_state["logged_in"] = True
    st.session_state["in_pass"] = ""


def do_logout():
    st.session_state["logged_in"] = False


def save_new_name():
    new_name = st.session_state.get("edit_name", "").strip()
    if new_name:
        st.session_state["student_name"] = new_name
    st.session_state["student_class"] = st.session_state.get("edit_class", "").strip()


def new_quote():
    st.session_state["quote"] = random.choice(QUOTES)


def page_home():
    if not st.session_state["logged_in"]:
        st.title("🧠 NeuroBridge")
        st.subheader("Learn at Your Pace. Grow with Confidence.")
        st.write(
            "NeuroBridge is a friendly practice space for children who find reading "
            "difficult. You can read short stories, learn new words, practise maths "
            "and play gentle reading games."
        )
        st.caption(
            "NeuroBridge is a school learning-support prototype. It does not diagnose "
            "dyslexia or give medical advice. It is meant to complement good teaching "
            "and individual learning support."
        )
        with st.container(border=True):
            st.markdown("### 👋 Welcome! Sign in to start")
            st.warning("🔒 Demo only: nothing typed here is saved or checked. "
                       "You can skip everything and press “Continue in Demo Mode”.")
            st.text_input("Student name or username", key="in_name")
            st.text_input("Age or class (optional)", key="in_class")
            st.text_input("Email (demo only, not saved)", key="in_email")
            st.text_input("Password (demo only, not saved)", type="password", key="in_pass")
            left, right = st.columns(2)
            left.button("Log in (demo)", on_click=do_login, width="stretch")
            right.button("🚀 Continue in Demo Mode", on_click=do_demo_mode,
                         type="primary", width="stretch")
        return

    records = get_records()
    stories_done = len({r["name"] for r in records if r["type"] == "story"})
    maths_done = sum(1 for r in records if r["type"] == "maths")
    games_done = sum(1 for r in records if r["type"] == "game")

    st.title(f"👋 Hello, {st.session_state['student_name']}!")
    if st.session_state["student_class"]:
        st.caption(f"Age/class: {st.session_state['student_class']}")
    st.subheader("Learn at Your Pace. Grow with Confidence.")
    st.success(st.session_state["quote"])
    st.button("🔄 New message", on_click=new_quote)

    st.markdown("## What would you like to do?")
    card1, card2, card3 = st.columns(3)
    with card1:
        with st.container(border=True):
            st.markdown("### 📖 Reading Practice")
            st.write("Read stories and discover new words.")
            st.button("Open Reading Practice", key="card_read", width="stretch",
                      on_click=go_to, args=(PAGE_READING,))
    with card2:
        with st.container(border=True):
            st.markdown("### 🔢 Quizzes")
            st.write("Practise maths step by step.")
            st.button("Open Quizzes", key="card_quiz", width="stretch",
                      on_click=go_to, args=(PAGE_QUIZ, "qg_section", SECTION_MATHS))
    with card3:
        with st.container(border=True):
            st.markdown("### 🎮 Games")
            st.write("Learn through fun activities.")
            st.button("Open Games", key="card_games", width="stretch",
                      on_click=go_to, args=(PAGE_QUIZ, "qg_section", SECTION_GAMES))

    st.markdown("## ⭐ My progress")
    col1, col2, col3 = st.columns(3)
    col1.metric("Stories completed", stories_done)
    col2.metric("Maths quizzes completed", maths_done)
    col3.metric("Games played", games_done)
    if not records:
        st.info("Nothing here yet. Pick an activity above to begin! 🌱")

    with st.expander("⚙️ My reading settings"):
        reading_settings_panel()
    with st.expander("✏️ Change my name"):
        st.text_input("Name", value=st.session_state["student_name"], key="edit_name")
        st.text_input("Age or class (optional)", value=st.session_state["student_class"],
                      key="edit_class")
        st.button("Save", on_click=save_new_name)
    st.button("Log out (demo)", on_click=do_logout)


# ======================================================================
# 7. PAGE 2 - READING PRACTICE
# ======================================================================
def change_paragraph(story_id, step, last_index):
    key = f"para_{story_id}"
    new_value = st.session_state.get(key, 0) + step
    st.session_state[key] = max(0, min(last_index, new_value))


def begin_story_quiz(story):
    set_choice(f"section_{story['id']}", "📝 Quiz")
    meta = {"type": "story", "name": story["title"], "level": story["level"]}
    start_quiz(f"quiz_story_{story['id']}", story["questions"], meta)


def story_read_section(story, listen_mode):
    paragraphs = story["paragraphs"]
    last_index = len(paragraphs) - 1
    para_key = f"para_{story['id']}"
    index = st.session_state.get(para_key, 0)
    prefs = st.session_state["prefs"]

    st.progress((index + 1) / len(paragraphs),
                text=f"Paragraph {index + 1} of {len(paragraphs)}")

    chosen_word = None
    if prefs["emphasis"]:
        words = sorted({w.strip(".,!?“”\"'").lower() for w in paragraphs[index].split()
                        if len(w.strip(".,!?“”\"'")) > 3})
        pick = st.selectbox("Pick a word to highlight (optional)", ["(none)"] + words,
                            key=f"hw_{story['id']}_{index}")
        chosen_word = None if pick == "(none)" else pick

    show_reading_text(paragraphs[index], highlight_word=chosen_word)

    nav_left, nav_right = st.columns(2)
    nav_left.button("⬅️ Previous paragraph", key=f"prev_{story['id']}", width="stretch",
                    disabled=index == 0, on_click=change_paragraph,
                    args=(story["id"], -1, last_index))
    nav_right.button("Next paragraph ➡️", key=f"next_{story['id']}", width="stretch",
                     disabled=index == last_index, on_click=change_paragraph,
                     args=(story["id"], 1, last_index))

    if listen_mode:
        speak_button(paragraphs[index], key=f"say_para_{story['id']}_{index}",
                     label="🔊 Listen to this paragraph")
        sentences = split_sentences(paragraphs[index])
        choice = st.selectbox("Replay one sentence", sentences,
                              key=f"sent_{story['id']}_{index}")
        speak_button(choice, key=f"say_sent_{story['id']}_{index}", label="🔊 Listen to this sentence")

    with st.expander("🪜 Practise sentence by sentence"):
        st.write("Read one sentence at a time. Then read the paragraph again, a little faster. 🔁")
        for number, sentence in enumerate(split_sentences(paragraphs[index]), start=1):
            st.markdown(f"**{number}.** {sentence}")

    if st.checkbox("📜 Show the whole story", key=f"whole_{story['id']}"):
        for number, text in enumerate(paragraphs):
            if prefs["emphasis"] and number == index:
                show_reading_text("👉 " + text, bold=True)
            else:
                show_reading_text(text)

    if index == last_index:
        st.success("🎉 You reached the end of the story!")
    st.button("📝 Begin the comprehension quiz", key=f"begin_{story['id']}",
              type="primary", on_click=begin_story_quiz, args=(story,))


def story_vocab_section(story):
    words = list(story["vocabulary"].keys())
    word = st.selectbox("Choose a word", words, key=f"vocab_{story['id']}")
    info = story["vocabulary"][word]
    with st.container(border=True):
        st.markdown(f"## {info['emoji']} {word.capitalize()}")
        st.write(f"**Meaning:** {info['meaning']}")
        st.write(f"**Example:** “{info['example']}”")
    speak_button(f"{word}. {info['meaning']} {info['example']}",
                 key=f"say_vocab_{story['id']}_{word}", label="🔊 Hear this word")
    with st.expander("See all the story words"):
        for name, details in story["vocabulary"].items():
            st.write(f"{details['emoji']} **{name}**: {details['meaning']}")


def page_reading():
    st.header("📖 Reading Practice")
    st.caption("Choose a level and a story. Take your time. There is no rush. 🐢")

    level = sticky_choice("Reading level", LEVELS, "reading_level")
    level_stories = [s for s in STORIES if s["level"] == level]
    titles = [s["title"] for s in level_stories]
    title = sticky_choice("Choose a story", titles, "story_title", horizontal=False)
    story = next(s for s in level_stories if s["title"] == title)

    with st.container(border=True):
        st.markdown(f"### {story['emoji']} {story['title']}")
        st.write(story["description"])
        st.caption(f"Level: {story['level']}  •  About {story['time']}")

    mode = sticky_choice("How do you want to read?", ["Read by Myself", "Listen and Read"],
                         "read_mode")
    section = sticky_choice("Story section", ["📖 Read", "🔤 Words", "📝 Quiz"],
                            f"section_{story['id']}")

    if section == "📖 Read":
        story_read_section(story, listen_mode=(mode == "Listen and Read"))
    elif section == "🔤 Words":
        story_vocab_section(story)
    else:
        quiz_key = f"quiz_story_{story['id']}"
        if quiz_key not in st.session_state:
            st.write("Ready to show what you know? There are 5 questions.")
            st.button("▶️ Start the quiz", key=f"start_{story['id']}", type="primary",
                      on_click=begin_story_quiz, args=(story,))
        else:
            render_quiz(quiz_key)


# ======================================================================
# 8. PAGE 3 - QUIZZES & GAMES
# ======================================================================
def start_maths_quiz(class_level, topic, difficulty):
    meta = {"type": "maths", "name": topic, "difficulty": difficulty, "class_level": class_level}
    start_quiz("quiz_maths", maths_questions(topic, difficulty), meta,
               rebuild=lambda: maths_questions(topic, difficulty))


def leave_maths_quiz():
    st.session_state.pop("quiz_maths", None)


def maths_section():
    st.subheader("🔢 Maths Quizzes")
    if "quiz_maths" in st.session_state:
        meta = st.session_state["quiz_maths"]["meta"]
        st.caption(f"{meta['name']}  •  {meta['difficulty']}  •  {meta['class_level']}")
        render_quiz("quiz_maths")
        st.button("⬅️ Choose a different quiz", on_click=leave_maths_quiz)
        return

    st.write("Pick your class, topic and difficulty. Each quiz has 5 questions.")
    class_level = sticky_choice("School class or level", list(CLASS_LEVELS), "maths_class", kind="select")
    topic = sticky_choice("Topic", MATHS_TOPICS, "maths_topic", kind="select")
    difficulty = sticky_choice("Difficulty", DIFFICULTIES, "maths_difficulty")
    st.caption(f"Suggested starting difficulty for {class_level}: {CLASS_LEVELS[class_level]}")
    st.button("▶️ Start quiz", type="primary", on_click=start_maths_quiz,
              args=(class_level, topic, difficulty))


# ---------- Games ----------
def new_game(rounds):
    return {"rounds": rounds, "index": 0, "score": 0, "status": "asking",
            "first_try": True, "saved": False, "save_failed": False,
            "built": [], "feedback": "", "warning": ""}


def game_answer(key, correct, explanation):
    game = st.session_state[key]
    game["warning"] = ""
    if correct:
        game["status"] = "correct"
        game["feedback"] = explanation
        if game["first_try"] and game["index"] > 0:   # round 0 is practice
            game["score"] += 1
    else:
        game["status"] = "wrong"
        game["feedback"] = explanation
        game["first_try"] = False


def game_retry(key):
    game = st.session_state[key]
    game["status"] = "asking"
    game["built"] = []


def game_next(key):
    game = st.session_state[key]
    game["index"] += 1
    game["status"] = "asking"
    game["first_try"] = True
    game["built"] = []
    game["warning"] = ""


def game_play_again(key):
    st.session_state.pop(key, None)


def run_game(name, instructions, make_rounds, draw_round):
    """Shared frame for all four games: practice round, rounds, feedback, score."""
    key = "game_" + name
    st.info(instructions)
    if key not in st.session_state:
        st.session_state[key] = new_game(make_rounds())
    game = st.session_state[key]
    scored_rounds = len(game["rounds"]) - 1

    if game["index"] >= len(game["rounds"]):          # finished
        if not game["saved"]:
            ok = record_activity("game", name, game["score"], scored_rounds)
            game["saved"] = True
            game["save_failed"] = not ok
        st.subheader(f"🏁 You got {game['score']} out of {scored_rounds}")
        st.success(encouragement(game["score"], scored_rounds))
        if game["save_failed"]:
            st.warning("Your result could not be saved on this computer.")
        else:
            st.caption("✅ Your result was saved.")
        st.button("🔁 Play Again", key=f"again_{name}", type="primary",
                  on_click=game_play_again, args=(key,))
        return

    if game["index"] == 0:
        st.subheader("✏️ Practice round (not scored)")
    else:
        st.subheader(f"Round {game['index']} of {scored_rounds}")
    st.progress(game["index"] / len(game["rounds"]))

    draw_round(key, game, game["rounds"][game["index"]])

    if game["warning"]:
        st.warning(game["warning"])
    if game["status"] == "correct":
        st.success("🎉 Correct! " + game["feedback"])
    elif game["status"] == "wrong":
        st.error("Not quite. " + game["feedback"])
    if game["status"] != "asking":
        left, right = st.columns(2)
        if game["status"] == "wrong":
            left.button("🔄 Try again", key=f"retry_{name}_{game['index']}",
                        on_click=game_retry, args=(key,), width="stretch")
        last = game["index"] == len(game["rounds"]) - 1
        right.button("See my score ➡️" if last else "Next round ➡️",
                     key=f"next_{name}_{game['index']}", type="primary",
                     on_click=game_next, args=(key,), width="stretch")


def pick_rounds(all_rounds, count=5):
    """First round is the practice example; the rest are chosen at random."""
    return [all_rounds[0]] + random.sample(all_rounds[1:], min(count, len(all_rounds) - 1))


# --- Game 1: Letter-Sound Match ---
def letter_sound_rounds():
    rounds = []
    for letter, right, others in pick_rounds(LETTER_SOUND_ROUNDS, 6):
        options = [right] + others
        random.shuffle(options)
        rounds.append({"letter": letter, "right": right, "options": options})
    return rounds


def draw_letter_sound(key, game, rnd):
    st.markdown(f"## Which word starts with the sound of the letter  **{rnd['letter'].upper()}**  ({rnd['letter']})?")
    if game["status"] == "asking":
        columns = st.columns(len(rnd["options"]))
        for number, option in enumerate(rnd["options"]):
            columns[number].button(option, key=f"{key}_{game['index']}_{number}", width="stretch",
                                   on_click=game_answer,
                                   args=(key, option == rnd["right"],
                                         f"{rnd['right']} starts with the “{rnd['letter']}” sound."))


# --- Game 2: Build the Word ---
def build_word_rounds():
    rounds = []
    for word in pick_rounds(BUILD_WORDS, 5):
        letters = list(word)
        while letters == list(word):
            random.shuffle(letters)
        rounds.append({"word": word, "letters": letters})
    return rounds


def add_letter(key, position):
    game = st.session_state[key]
    if position not in game["built"]:
        game["built"].append(position)


def clear_letters(key):
    st.session_state[key]["built"] = []


def check_word(key, rnd):
    game = st.session_state[key]
    attempt = "".join(rnd["letters"][p] for p in game["built"])
    game_answer(key, attempt == rnd["word"], f"The word is “{rnd['word']}”.")


def draw_build_word(key, game, rnd):
    st.markdown("## Put the letters in the right order to make a word")
    attempt = " ".join(rnd["letters"][p].upper() for p in game["built"])
    blanks = " ".join("_" for _ in range(len(rnd["word"]) - len(game["built"])))
    st.markdown(f"# {attempt} {blanks}")
    if game["status"] != "asking":
        return
    columns = st.columns(len(rnd["letters"]))
    for position, letter in enumerate(rnd["letters"]):
        columns[position].button(letter.upper(), key=f"{key}_{game['index']}_{position}",
                                 width="stretch", disabled=position in game["built"],
                                 on_click=add_letter, args=(key, position))
    left, right = st.columns(2)
    left.button("↩️ Clear", key=f"{key}_clear_{game['index']}", on_click=clear_letters,
                args=(key,), width="stretch")
    right.button("✅ Check", key=f"{key}_check_{game['index']}", type="primary",
                 disabled=len(game["built"]) != len(rnd["word"]),
                 on_click=check_word, args=(key, rnd), width="stretch")


# --- Game 3: Word-Picture Match ---
def word_picture_rounds():
    rounds = []
    for word, right, others in pick_rounds(WORD_PICTURE_ROUNDS, 5):
        options = [right] + others
        random.shuffle(options)
        rounds.append({"word": word, "right": right, "options": options})
    return rounds


def draw_word_picture(key, game, rnd):
    st.markdown(f"## Which picture matches the word  **{rnd['word']}**?")
    if game["status"] == "asking":
        columns = st.columns(len(rnd["options"]))
        for number, option in enumerate(rnd["options"]):
            columns[number].button(option, key=f"{key}_{game['index']}_{number}", width="stretch",
                                   on_click=game_answer,
                                   args=(key, option == rnd["right"],
                                         f"{rnd['right']} is a {rnd['word']}."))


# --- Game 4: Put the Story in Order ---
def story_order_rounds():
    rounds = []
    for title, events in pick_rounds(STORY_ORDER_ROUNDS, 4):
        shuffled = list(events)
        while shuffled == events:
            random.shuffle(shuffled)
        rounds.append({"title": title, "correct": events, "shuffled": shuffled})
    return rounds


def check_order(key, rnd):
    game = st.session_state[key]
    chosen = []
    for number, event in enumerate(rnd["shuffled"]):
        value = st.session_state.get(f"{key}_{game['index']}_{number}", "-")
        chosen.append(value)
    if "-" in chosen or len(set(chosen)) != len(chosen):
        game["warning"] = "Choose a different number (1, 2, 3...) for every step first."
        return
    ordered = sorted(zip(chosen, rnd["shuffled"]))
    correct = [event for _, event in ordered] == rnd["correct"]
    answer_text = "  ".join(f"{n}. {e}" for n, e in enumerate(rnd["correct"], start=1))
    game_answer(key, correct, "Correct order: " + answer_text)


def draw_story_order(key, game, rnd):
    st.markdown(f"## {rnd['title']}")
    st.write("Number each step 1, 2, 3... in the order it happens.")
    if game["status"] != "asking":
        return
    numbers = ["-"] + list(range(1, len(rnd["shuffled"]) + 1))
    for number, event in enumerate(rnd["shuffled"]):
        left, right = st.columns([1, 3])
        left.selectbox("Order", numbers, key=f"{key}_{game['index']}_{number}",
                       label_visibility="collapsed")
        right.markdown(f"#### {event}")
    st.button("✅ Check my order", key=f"{key}_check_{game['index']}", type="primary",
              on_click=check_order, args=(key, rnd))


GAMES = {
    "Letter–Sound Match": (
        "🔤 Skill: letters and sounds. Look at the letter and pick the word that begins with its sound. "
        "The first round is practice.",
        letter_sound_rounds, draw_letter_sound),
    "Build the Word": (
        "🧩 Skill: spelling. Tap the letters in the right order to build the word. "
        "The first round is practice.",
        build_word_rounds, draw_build_word),
    "Word–Picture Match": (
        "🖼️ Skill: word recognition. Read the word and pick the matching picture. "
        "The first round is practice.",
        word_picture_rounds, draw_word_picture),
    "Put the Story in Order": (
        "📚 Skill: sequencing. Choose a number for each step so the story makes sense. "
        "The first round is practice.",
        story_order_rounds, draw_story_order),
}


def games_section():
    st.subheader("🎮 Reading Games")
    st.caption("No timers and no rankings, just calm practice. 🌿")
    name = sticky_choice("Choose a game", list(GAMES), "game_choice")
    instructions, make_rounds, draw_round = GAMES[name]
    run_game(name, instructions, make_rounds, draw_round)


def page_quizzes_games():
    st.header("🎯 Quizzes & Games")
    section = sticky_choice("Choose a section", [SECTION_MATHS, SECTION_GAMES], "qg_section")
    st.divider()
    if section == SECTION_MATHS:
        maths_section()
    else:
        games_section()


# ======================================================================
# 9. PAGE 4 - PARENT/TEACHER DASHBOARD
# ======================================================================
def sample_records():
    """Clearly-labelled SAMPLE data, used only if the adult ticks the box."""
    now = datetime.now()
    rows = [
        ("story", "The Little Bird Who Kept Trying", 3, 5, 6),
        ("maths", "Addition and subtraction", 3, 5, 5),
        ("game", "Build the Word", 4, 5, 5),
        ("story", "Mia and the Magical Library", 4, 5, 4),
        ("maths", "Fractions", 1, 5, 3),
        ("story", "The Mystery of the Missing Map", 5, 5, 2),
        ("maths", "Fractions", 4, 5, 1),
        ("game", "Word–Picture Match", 5, 5, 0),
    ]
    return [{"type": t, "name": n, "score": s, "total": tot,
             "timestamp": (now - timedelta(days=d)).strftime(TIME_FORMAT)}
            for t, n, s, tot, d in rows]


def average_percent(items):
    if not items:
        return None
    return round(sum(percent(r["score"], r["total"]) for r in items) / len(items))


def build_suggestions(records):
    """Simple if/elif rules. These are general tips, not diagnoses."""
    suggestions = []
    stories = [r for r in records if r["type"] == "story"]
    maths = [r for r in records if r["type"] == "maths"]

    if len(records) == 0:
        suggestions.append("Start with one short story or quiz. A few minutes a day works well.")
    elif len(records) < 3:
        suggestions.append("Only a few activities are recorded so far. Try a short, regular practice "
                           "session (about 10 minutes) several times a week.")

    recent_reading = [percent(r["score"], r["total"]) for r in stories[-3:]]
    if len(recent_reading) >= 2 and sum(recent_reading) / len(recent_reading) < 60:
        suggestions.append("Reading comprehension scores are often low. Try shorter stories, "
                           "re-read each paragraph, and talk about the story events afterwards.")
    elif len(stories) >= 4:
        first = [percent(r["score"], r["total"]) for r in stories[:2]]
        last = [percent(r["score"], r["total"]) for r in stories[-2:]]
        if sum(last) / 2 > sum(first) / 2:
            suggestions.append("Reading scores are improving. Wonderful progress. Keep it up! 🌟")

    topics = {}
    for r in maths:
        topics.setdefault(r["name"], []).append(percent(r["score"], r["total"]))
    for topic, scores in topics.items():
        if sum(scores) / len(scores) < 60:
            suggestions.append(f"Maths topic “{topic}” had low scores. Try another quiz on this topic "
                               "and go through the worked explanations together.")
    if len(maths) >= 4:
        first = [percent(r["score"], r["total"]) for r in maths[:2]]
        last = [percent(r["score"], r["total"]) for r in maths[-2:]]
        if sum(last) / 2 > sum(first) / 2:
            suggestions.append("Maths scores are improving. Great effort! 🎉")

    if not suggestions:
        suggestions.append("Steady practice so far. Keep up the regular, relaxed sessions. 👍")
    return suggestions


def filter_by_date(records):
    with st.expander("📅 Filter by date (optional)"):
        if st.checkbox("Only show a date range", key="use_date_filter"):
            today = datetime.now().date()
            chosen = st.date_input("Dates", value=(today - timedelta(days=30), today),
                                   key="date_range")
            if isinstance(chosen, (tuple, list)) and len(chosen) == 2:
                start, end = chosen
                return [r for r in records
                        if start <= datetime.strptime(r["timestamp"], TIME_FORMAT).date() <= end]
            st.caption("Pick both a start date and an end date.")
    return records


def page_dashboard():
    st.header("👩‍🏫 Parent/Teacher Dashboard")
    st.warning("🔒 This is a demonstration dashboard. The demo login is not secure "
               "authentication, and anyone using this computer can open this page.")
    st.caption(f"Showing activity for: {st.session_state['student_name']}")

    use_sample = st.checkbox("Show SAMPLE data (for demonstration only, not real progress)",
                             key="use_sample")
    records = sample_records() if use_sample else get_records()
    if use_sample:
        st.info("📌 You are looking at SAMPLE data. Untick the box to see real progress.")
    records = filter_by_date(records)

    stories = [r for r in records if r["type"] == "story"]
    maths = [r for r in records if r["type"] == "maths"]
    games = [r for r in records if r["type"] == "game"]

    # ----- metrics -----
    st.subheader("📊 Overview")
    columns = st.columns(5)
    columns[0].metric("Stories completed", len({r["name"] for r in stories}))
    avg_reading = average_percent(stories)
    columns[1].metric("Avg. reading score", "–" if avg_reading is None else f"{avg_reading}%")
    columns[2].metric("Maths quizzes", len(maths))
    avg_maths = average_percent(maths)
    columns[3].metric("Avg. maths score", "–" if avg_maths is None else f"{avg_maths}%")
    columns[4].metric("Games completed", len(games))

    # ----- charts -----
    st.subheader("📈 Reading Comprehension Progress")
    if stories:
        data = pd.DataFrame({"Score (%)": [percent(r["score"], r["total"]) for r in stories]},
                            index=pd.RangeIndex(1, len(stories) + 1, name="Story quiz attempt"))
        st.line_chart(data)
        st.caption("Each point is one finished story quiz, in order. Higher means more answers correct.")
    else:
        st.info("No story quizzes finished yet. The chart will appear after the first one. 📖")

    st.subheader("📈 Mathematics Progress")
    if maths:
        data = pd.DataFrame({"Score (%)": [percent(r["score"], r["total"]) for r in maths]},
                            index=pd.RangeIndex(1, len(maths) + 1, name="Maths quiz attempt"))
        st.line_chart(data)
        st.caption("Each point is one finished maths quiz, in order. Higher means more answers correct.")
    else:
        st.info("No maths quizzes finished yet. The chart will appear after the first one. 🔢")

    st.subheader("📊 Learning Activities")
    if records:
        data = pd.DataFrame({"Completed": [len(stories), len(maths), len(games)]},
                            index=pd.Index(["Reading sessions", "Maths quizzes", "Games"],
                                           name="Activity"))
        st.bar_chart(data)
        st.caption("This compares how many reading sessions, maths quizzes and games were completed.")
    else:
        st.info("No activities yet. This chart compares reading, maths and games once there are some. 🌱")

    # ----- recent activity -----
    st.subheader("🕒 Recent activity")
    if records:
        labels = {"story": "Reading", "maths": "Maths", "game": "Game"}
        recent = sorted(records, key=lambda r: r["timestamp"], reverse=True)[:10]
        table = pd.DataFrame({
            "Date/time": [r["timestamp"] for r in recent],
            "Activity": [labels[r["type"]] for r in recent],
            "Story / topic / game": [r["name"] for r in recent],
            "Score": [f"{r['score']}/{r['total']}" for r in recent],
        })
        st.dataframe(table, hide_index=True, width="stretch")
    else:
        st.info("Nothing recorded yet.")

    # ----- suggestions -----
    st.subheader("💡 Learning suggestions")
    for suggestion in build_suggestions(records):
        st.write(f"• {suggestion}")
    st.caption("These are simple, general suggestions based on saved scores. "
               "They are not a diagnosis or a clinical assessment.")


# ======================================================================
# 10. MAIN: sidebar navigation and page selection
# ======================================================================
def main():
    init_state()
    if st.session_state.get("nav_page") not in PAGES:
        st.session_state["nav_page"] = PAGE_HOME

    with st.sidebar:
        st.title("🧠 NeuroBridge")
        st.caption("Learn at Your Pace. Grow with Confidence.")
        st.radio("Go to", PAGES, key="nav_page")
        if st.session_state["logged_in"]:
            st.write(f"👤 {st.session_state['student_name']}")
        st.caption("Learning-support prototype. Not a diagnostic or medical tool.")

    page = st.session_state["nav_page"]
    if page == PAGE_HOME and st.session_state["last_page"] != PAGE_HOME:
        st.session_state["quote"] = random.choice(QUOTES)   # fresh message when Home opens
    st.session_state["last_page"] = page

    if page == PAGE_HOME:
        page_home()
    elif page == PAGE_READING:
        page_reading()
    elif page == PAGE_QUIZ:
        page_quizzes_games()
    else:
        page_dashboard()

    if st.session_state.get("file_message"):
        st.sidebar.warning(st.session_state["file_message"])


main()
