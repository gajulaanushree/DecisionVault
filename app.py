import streamlit as st
from hindsight_client import Hindsight

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="DecisionVault",
    page_icon="🧠",
    layout="wide"
)

BANK_ID = "novatech"
BASE_URL = "https://api.hindsight.vectorize.io"


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f6f7f9;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

.title {
    font-size: 46px;
    font-weight: 800;
    letter-spacing: -1px;
}

.subtitle {
    color: #6b7280;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
}

.metric {
    background: white;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    min-height: 130px;
}

.metric-label {
    color: #6b7280;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

.metric-number {
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}

.timeline {
    border-left: 3px solid #d1d5db;
    padding-left: 25px;
    margin-left: 10px;
}

.timeline-item {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
}

.timeline-dot {
    font-size: 24px;
}

.alert {
    background: #fff7ed;
    border: 1px solid #fed7aa;
    padding: 28px;
    border-radius: 18px;
    margin: 22px 0;
}

.memory {
    background: #eef2ff;
    border: 1px solid #c7d2fe;
    padding: 25px;
    border-radius: 18px;
    margin: 20px 0;
}

.success {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    padding: 25px;
    border-radius: 18px;
    margin: 20px 0;
}

.before {
    background: #f9fafb;
    border: 1px solid #e5e7eb;
    padding: 25px;
    border-radius: 18px;
}

.after {
    background: #eef2ff;
    border: 1px solid #c7d2fe;
    padding: 25px;
    border-radius: 18px;
}

.section {
    font-size: 27px;
    font-weight: 750;
    margin-top: 30px;
    margin-bottom: 18px;
}

.small {
    color: #6b7280;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HINDSIGHT CLIENT
# =========================================================

@st.cache_resource
def create_client(api_key):
    return Hindsight(
        base_url=BASE_URL,
        api_key=api_key
    )


# =========================================================
# API KEY
# =========================================================

api_key = st.session_state.get("hindsight_api_key")

if not api_key:

    st.markdown(
        '<div class="title">🧠 DecisionVault</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Company decisions that become smarter with experience.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("## 🔐 Connect to Hindsight")

    entered_key = st.text_input(
        "Hindsight API Key",
        type="password",
        placeholder="Paste your Hindsight API key"
    )

    if st.button(
        "🔐 Connect",
        type="primary",
        use_container_width=True
    ):

        if entered_key.strip():

            st.session_state["hindsight_api_key"] = entered_key.strip()
            st.rerun()

        else:

            st.warning("Please enter your Hindsight API key.")

    st.stop()


client = create_client(api_key)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🧠 DecisionVault</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI that remembers what your company decided, why it decided it, '
    'and what happened next.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🧠 DecisionVault")

st.sidebar.caption("NovaTech Company Memory")

page = st.sidebar.radio(
    "Navigate",
    [
        "Dashboard",
        "Analyze Decision",
        "Add Decision",
        "Decision History"
    ]
)


# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

    st.header("Company Memory")

    st.write(
        "DecisionVault turns past company experience into memory "
        "that can influence future decisions."
    )

    st.divider()

    # -----------------------------------------------------
    # METRICS
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown("""
        <div class="metric">
            <div class="metric-label">Memory Engine</div>
            <div class="metric-number">Hindsight</div>
            <p>Persistent memory</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="metric">
            <div class="metric-label">Memory Bank</div>
            <div class="metric-number">NovaTech</div>
            <p>Company experience</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="metric">
            <div class="metric-label">Learning Loop</div>
            <div class="metric-number">ACTIVE</div>
            <p>Decision → Lesson</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.markdown("""
        <div class="metric">
            <div class="metric-label">Memory State</div>
            <div class="metric-number">LIVE</div>
            <p>Ready for decisions</p>
        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # MAIN VALUE
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">Why DecisionVault?</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <h2>🤖 Normal AI</h2>

        <p>
        Answers based mainly on the current question.
        </p>

        <br>

        <b>Question</b>

        <br>

        ↓

        <br>

        AI generates an answer.

        <br><br>

        The experience from previous company decisions
        can easily remain disconnected.

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="memory">

        <h2>🧠 DecisionVault + Hindsight</h2>

        <p>
        Connects today's decision with yesterday's experience.
        </p>

        <br>

        <b>New Decision</b>

        <br>

        ↓

        <br>

        🧠 Search company memory

        <br>

        ↓

        <br>

        📚 Past decisions + outcomes

        <br>

        ↓

        <br>

        💡 Better recommendation

        </div>
        """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # TIMELINE
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">🕐 Decision Learning Timeline</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="timeline">

        <div class="timeline-item">
            <span class="timeline-dot">💡</span>
            <h3>Decision</h3>
            Company chooses a new strategy.
        </div>

        <div class="timeline-item">
            <span class="timeline-dot">📊</span>
            <h3>Result</h3>
            The company observes what actually happened.
        </div>

        <div class="timeline-item">
            <span class="timeline-dot">📚</span>
            <h3>Lesson</h3>
            The experience is converted into a useful lesson.
        </div>

        <div class="timeline-item">
            <span class="timeline-dot">🧠</span>
            <h3>Hindsight Memory</h3>
            The experience becomes persistent company memory.
        </div>

        <div class="timeline-item">
            <span class="timeline-dot">🔮</span>
            <h3>Future Decision</h3>
            The memory can influence a similar decision later.
        </div>

    </div>
    """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # KILLER FEATURE
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">⚠️ The Killer Feature</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="alert">

    <h2>You've made this mistake before.</h2>

    <p>
    DecisionVault doesn't simply ask:
    <b>"What should we do?"</b>
    </p>

    <p>
    It asks:
    <b>"What happened when we tried something similar?"</b>
    </p>

    <br>

    <b>
    That's the difference between generating answers
    and learning from experience.
    </b>

    </div>
    """, unsafe_allow_html=True)


    # -----------------------------------------------------
    # DEMO
    # -----------------------------------------------------

    st.markdown(
        '<div class="section">🎬 Demo Scenario</div>',
        unsafe_allow_html=True
    )

    st.code(
        "Launch an AI-powered social sharing feature "
        "because our competitor just launched one."
    )

    st.info(
        "Go to Analyze Decision to see what the company's "
        "memory says about this decision."
    )


# =========================================================
# ANALYZE DECISION
# =========================================================

elif page == "Analyze Decision":

    st.header("🧠 Analyze a New Decision")

    st.write(
        "Before making a decision, ask your company's memory "
        "what happened last time."
    )

    st.divider()


    decision = st.text_area(
        "What are you deciding?",
        placeholder=(
            "Example: Launch an AI-powered social sharing feature"
        ),
        height=100,
        key="decision_input"
    )


    reason = st.text_area(
        "Why are you considering it?",
        placeholder=(
            "Example: Our competitor launched a similar feature"
        ),
        height=100,
        key="reason_input"
    )


    expected = st.text_input(
        "What outcome do you expect?",
        placeholder=(
            "Example: 15% increase in engagement"
        ),
        key="expected_input"
    )


    analyze = st.button(
        "🧠 ANALYZE WITH COMPANY MEMORY",
        type="primary",
        use_container_width=True
    )


    if analyze:

        if not decision.strip():

            st.warning("Please enter the decision first.")

        else:

            query = f"""

            A company is considering this new decision.

            DECISION:
            {decision}

            REASON:
            {reason}

            EXPECTED OUTCOME:
            {expected}

            Analyze this decision using the company's stored
            decision history.

            Answer:

            1. Have we made similar decisions before?

            2. What happened?

            3. Which decisions succeeded or failed?

            4. What lessons were learned?

            5. Is this similar to a previous failure?

            6. Give a short practical recommendation.

            Mention relevant past decisions.

            Do not invent company history that is not present
            in memory.

            """

            with st.spinner(
                "🧠 Searching company memory..."
            ):

                try:

                    response = client.reflect(
                        bank_id=BANK_ID,
                        query=query
                    )

                    st.session_state["last_analysis"] = response.text
                    st.session_state["last_decision"] = decision
                    st.session_state["last_reason"] = reason
                    st.session_state["last_expected"] = expected
                    st.session_state["analysis_complete"] = True

                    st.session_state["learning_saved"] = False

                    st.success(
                        "Decision analyzed using Hindsight memory."
                    )

                except Exception as error:

                    st.error(
                        f"Analysis failed:\n\n{error}"
                    )


    # =====================================================
    # DISPLAY STORED ANALYSIS
    # =====================================================

    if st.session_state.get(
        "analysis_complete",
        False
    ):

        saved_analysis = st.session_state.get(
            "last_analysis",
            ""
        )

        saved_decision = st.session_state.get(
            "last_decision",
            ""
        )

        saved_reason = st.session_state.get(
            "last_reason",
            ""
        )

        saved_expected = st.session_state.get(
            "last_expected",
            ""
        )


        analysis_lower = saved_analysis.lower()

        failure_words = [
            "failed",
            "failure",
            "poor outcome",
            "poor result",
            "underperformed",
            "did not meet",
            "negligible impact",
            "low impact",
            "mistake",
            "unsuccessful"
        ]

        found_failure = any(
            word in analysis_lower
            for word in failure_words
        )


        # -------------------------------------------------
        # BEFORE / AFTER
        # -------------------------------------------------

        st.markdown(
            '<div class="section">⚡ Why Memory Matters</div>',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("""
            <div class="before">

            <h2>Without Memory</h2>

            <p>
            "Your competitor launched this feature,
            so you could consider building it too."
            </p>

            <br>

            <span class="small">
            Generic reasoning based on the current situation.
            </span>

            </div>
            """, unsafe_allow_html=True)


        with col2:

            st.markdown("""
            <div class="after">

            <h2>🧠 With Hindsight</h2>

            <p>
            "We've seen something similar before.
            Let's look at what happened."
            </p>

            <br>

            <span class="small">
            Current decision + company experience.
            </span>

            </div>
            """, unsafe_allow_html=True)


        # -------------------------------------------------
        # REVIEW
        # -------------------------------------------------

        st.markdown(
            '<div class="section">Decision Review</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Memory Engine", "Hindsight")

        with col2:
            st.metric("Decision", "Under Review")

        with col3:

            if found_failure:

                st.metric(
                    "Risk Signal",
                    "⚠️ REVIEW"
                )

            else:

                st.metric(
                    "Risk Signal",
                    "NO ALERT"
                )


        # -------------------------------------------------
        # ALERT
        # -------------------------------------------------

        if found_failure:

            st.markdown("""
            <div class="alert">

            <h1>⚠️ MEMORY ALERT</h1>

            <h2>You've faced something similar before.</h2>

            <p>
            DecisionVault found previous company experiences
            with unsuccessful outcomes.
            </p>

            <br>

            <b>
            Review what happened before committing resources.
            </b>

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="success">

            <h2>🧠 MEMORY CHECK</h2>

            <p>
            No obvious previous failure was detected.
            Review the analysis before proceeding.
            </p>

            </div>
            """, unsafe_allow_html=True)


        # -------------------------------------------------
        # ANALYSIS
        # -------------------------------------------------

        st.markdown(
            '<div class="section">🧠 Memory-Based Analysis</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="card">

            {saved_analysis}

            </div>
            """,
            unsafe_allow_html=True
        )


        # -------------------------------------------------
        # TEACH
        # -------------------------------------------------

        st.markdown(
            '<div class="section">'
            '🔄 Teach DecisionVault What Happened'
            '</div>',
            unsafe_allow_html=True
        )

        st.write(
            "The decision is only half of the story. "
            "Record the real outcome and the lesson learned."
        )


        actual_result = st.text_area(
            "What actually happened?",

            placeholder=(
                "Example: Engagement increased only 2%, "
                "much lower than the expected 15%."
            ),

            height=100,

            key="actual_result"
        )


        lesson = st.text_area(
            "What should the company remember?",

            placeholder=(
                "Example: Validate customer demand "
                "before copying competitor features."
            ),

            height=100,

            key="decision_lesson"
        )


        save_outcome = st.button(
            "🧠 SAVE OUTCOME & TEACH DECISIONVAULT",
            type="primary",
            use_container_width=True
        )


        if save_outcome:

            if not actual_result.strip():

                st.warning(
                    "Please enter what actually happened."
                )

            elif not lesson.strip():

                st.warning(
                    "Please enter the lesson."
                )

            else:

                learning_memory = f"""

                DECISION OUTCOME AND LESSON

                Original decision:
                {saved_decision}

                Why the decision was considered:
                {saved_reason}

                Expected outcome:
                {saved_expected}

                Actual outcome:
                {actual_result}

                Lesson learned:
                {lesson}

                Remember this experience when analyzing
                similar future decisions.

                """

                try:

                    client.retain(
                        bank_id=BANK_ID,
                        content=learning_memory
                    )

                    st.session_state["learning_saved"] = True

                    st.session_state[
                        "saved_actual_result"
                    ] = actual_result

                    st.session_state[
                        "saved_lesson"
                    ] = lesson

                    st.success(
                        "🧠 DecisionVault learned from this outcome."
                    )

                    st.balloons()

                except Exception as error:

                    st.error(
                        f"Could not save learning:\n\n{error}"
                    )


        # -------------------------------------------------
        # LEARNING CONFIRMATION
        # -------------------------------------------------

        if st.session_state.get(
            "learning_saved",
            False
        ):

            st.markdown("""
            <div class="memory">

            <h2>🧠 Memory Updated</h2>

            <p>
            This decision is now part of company experience.
            </p>

            <h3>
            Decision → Result → Lesson → Memory
            </h3>

            <p>
            Future decisions can use this experience.
            </p>

            </div>
            """, unsafe_allow_html=True)


        # -------------------------------------------------
        # NEW DECISION
        # -------------------------------------------------

        st.divider()

        if st.button(
            "🔄 START A NEW DECISION",
            use_container_width=True
        ):

            st.session_state["analysis_complete"] = False
            st.session_state["last_analysis"] = ""
            st.session_state["last_decision"] = ""
            st.session_state["last_reason"] = ""
            st.session_state["last_expected"] = ""
            st.session_state["learning_saved"] = False

            st.rerun()


# =========================================================
# ADD DECISION
# =========================================================

elif page == "Add Decision":

    st.header("➕ Add a Company Decision")

    st.write(
        "Store an important company experience in long-term memory."
    )

    st.divider()


    decision = st.text_area(
        "Decision",
        placeholder="Example: We simplified the onboarding process",
        height=100
    )


    reason = st.text_area(
        "Why did we make this decision?",
        placeholder="Example: Users were dropping out during signup",
        height=100
    )


    expected = st.text_area(
        "Expected result",
        placeholder="Example: Reduce onboarding drop-off by 15%",
        height=100
    )


    actual = st.text_area(
        "Actual result",
        placeholder="Example: Drop-off decreased by 18%",
        height=100
    )


    lesson = st.text_area(
        "What did we learn?",
        placeholder="Example: Removing unnecessary signup steps improved completion",
        height=100
    )


    save = st.button(
        "💾 SAVE TO COMPANY MEMORY",
        type="primary",
        use_container_width=True
    )


    if save:

        if not decision.strip():

            st.warning(
                "Please enter the decision."
            )

        else:

            memory = f"""

            COMPANY DECISION RECORD

            Decision:
            {decision}

            Why we made it:
            {reason}

            Expected result:
            {expected}

            Actual result:
            {actual}

            Lesson learned:
            {lesson}

            """

            try:

                client.retain(
                    bank_id=BANK_ID,
                    content=memory
                )

                st.success(
                    "✅ Decision stored in Hindsight memory."
                )

                st.balloons()

            except Exception as error:

                st.error(
                    f"Could not save decision:\n\n{error}"
                )


# =========================================================
# DECISION HISTORY
# =========================================================

elif page == "Decision History":

    st.header("📚 Decision History")

    st.write(
        "Search the company's memory and recover previous experiences."
    )

    st.divider()


    search_query = st.text_input(
        "What do you want to remember?",
        placeholder="Example: competitor decisions that failed"
    )


    search = st.button(
        "🔎 SEARCH COMPANY MEMORY",
        type="primary",
        use_container_width=True
    )


    if search:

        if not search_query.strip():

            st.warning(
                "Enter something to search."
            )

        else:

            with st.spinner(
                "🔎 Searching Hindsight memory..."
            ):

                try:

                    result = client.recall(
                        bank_id=BANK_ID,
                        query=search_query
                    )

                    memories = getattr(
                        result,
                        "results",
                        None
                    )

                    if memories is None:
                        memories = []


                    if len(memories) == 0:

                        st.info(
                            "No matching memories were found."
                        )

                    else:

                        st.success(
                            f"Found {len(memories)} relevant memories."
                        )


                        for index, memory in enumerate(
                            memories,
                            start=1
                        ):

                            text = getattr(
                                memory,
                                "text",
                                None
                            )

                            if text is None:

                                text = getattr(
                                    memory,
                                    "content",
                                    str(memory)
                                )


                            st.markdown(
                                f"""
                                <div class="timeline-item">

                                <h3>
                                🧠 Memory {index}
                                </h3>

                                {text}

                                </div>
                                """,
                                unsafe_allow_html=True
                            )


                except Exception as error:

                    st.error(
                        f"Memory search failed:\n\n{error}"
                    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "DecisionVault • Powered by Hindsight • "
    "Company decisions that become smarter with experience"
)