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
