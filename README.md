# 🧠 NeuroBridge
**Learn at Your Pace. Grow with Confidence.**

NeuroBridge is a Python-only learning-support prototype for children with dyslexia and other
reading difficulties. It is built with **Streamlit** and contains **no HTML, CSS, JavaScript or
other languages**.

> ⚠️ NeuroBridge is a school prototype. It does **not** diagnose dyslexia, give medical advice, or
> replace teachers or specialist support. It is meant to complement good teaching and individual
> learning support. No font or game alone treats dyslexia.

---

## 1. Setup and run

You need Python 3.9 or newer.

```bash
# (optional) create a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux

pip install -r requirements.txt
streamlit run app.py
```

Your browser opens the app (usually at http://localhost:8501).

`pyttsx3` (text-to-speech) is optional. If it fails to install, delete that line from
`requirements.txt`; the app still works and shows a friendly message instead of audio.
On Linux, pyttsx3 also needs `espeak` (`sudo apt install espeak`).

## 2. Files

| File | What it does |
|---|---|
| `app.py` | The whole app: pages, quiz engine, games, progress saving, dashboard |
| `content.py` | Plain Python data: stories, vocabulary, questions, maths bank, game content |
| `.streamlit/config.toml` | Built-in Streamlit theme colours (soft cream, teal, pale blue) |
| `requirements.txt` | Python packages |
| `neurobridge_progress.json` | Created automatically when you run the app; stores finished activities |
| `CURSOR_OR_CLAUDE_PROMPT.txt` | The original build prompt |

## 3. The four pages (sidebar)
1. **Home / Student Dashboard** – demo login, random encouraging message, three cards
   (Reading Practice, Quizzes, Games), progress summary, reading settings, change name.
2. **Reading Practice** – 6 original stories (2 Beginner, 2 Intermediate, 2 Advanced), paragraph-by-paragraph
   reader, "Read by Myself" / "Listen and Read", vocabulary helper, 5-question quiz per story (30 total).
3. **Quizzes & Games** – *Maths Quizzes* (6 topics × 3 difficulties, 5 questions each, with step-by-step
   explanations and retries) and *Reading Games* (Letter–Sound Match, Build the Word, Word–Picture Match,
   Put the Story in Order).
4. **Parent/Teacher Dashboard** – 5 summary numbers, 3 charts, recent activity, learning suggestions,
   optional date filter, and an optional clearly-labelled **sample data** view.

## 4. How progress is saved
Each *finished* quiz or game adds one record to `neurobridge_progress.json`
(type, name, score, total, date/time; maths records also store difficulty and class). A record is saved
only once, when the score screen is first shown, so Streamlit reruns cannot create duplicates. If the file
is missing it is created; if it is damaged, it is renamed `neurobridge_progress_damaged.json` and a fresh
file starts. A story counts as "completed" only after its comprehension quiz is finished.

## 5. Honest limitations (because no HTML/CSS/JavaScript is allowed)
- **Font:** Python and Streamlit cannot change the font of individual text. The "Dyslexia-friendly font"
  choice is remembered, but the font only changes if the computer owner adds a font file and describes it in
  `.streamlit/config.toml` using Streamlit's theme settings (`[[theme.fontFaces]]`, see Streamlit's
  theming documentation). This is configuration, not code.
- **Background colour:** the page background comes from the theme file. In the reading box, "White",
  "Cream" and "Pale blue" are shown with built-in Streamlit containers (bordered box, yellow-tinted
  box, blue box). They approximate the colours; they are not exact.
- **Text size:** uses Markdown heading levels (Small = normal text, Medium and Large = bigger text).
  Larger text also appears bold.
- **Line spacing:** "Extra spacing" puts each sentence on its own line, which gives a similar effect,
  but it is not true CSS line height.
- **Highlighting:** the chosen word is highlighted with Streamlit's built-in coloured-text Markdown.
  The current paragraph is shown in bold with a 👉 marker when "Show the whole story" is ticked.
- **Speech:** audio uses the offline `pyttsx3` package to make a temporary audio file played by
  `st.audio`. It depends on the computer's voices and may not work everywhere. If it fails, a friendly message
  appears and the "Practise sentence by sentence" box is still available. NeuroBridge does **not** listen to
  the child, so it cannot check pronunciation or missed words.
- **Login:** the login is a demo. Names are not checked, the password and email are never saved, and the
  Parent/Teacher page is not protected.
- **Class levels:** choosing a class only suggests a starting difficulty; the question bank is organised by
  topic and difficulty.

## 6. How the code works (for your teacher)
- **Streamlit** reruns `app.py` from top to bottom each time the child clicks something. Anything that must
  survive a rerun is kept in `st.session_state` (a dictionary).
- **Functions and callbacks:** buttons call small functions (`on_click=...`) to change state, for example
  `quiz_answer`, `quiz_next`, `game_next`.
- **Dictionaries and lists** in `content.py` hold all the stories, questions and games, so content can be edited
  without changing logic.
- **Reusable quiz engine:** `start_quiz` / `render_quiz` run both the story quizzes and maths quizzes.
- **`run_game`** is a shared frame for all four games (practice round, feedback, score, play again).
- **JSON file handling:** `json.load` / `json.dump` with `try/except` for missing or damaged files.
- **`datetime`** stores and formats time stamps; **`random`** shuffles options and chooses rounds.
- **pandas** (installed with Streamlit) builds tables for `st.line_chart` and `st.bar_chart`.
- **if / elif rules** in `build_suggestions` create the learning suggestions from saved scores.

## 7. Testing checklist
```bash
python -m py_compile app.py content.py     # syntax check
streamlit run app.py                       # then try every page, all 6 stories, each maths topic, 4 games
```
To start with a clean slate, close the app and delete `neurobridge_progress.json`.
