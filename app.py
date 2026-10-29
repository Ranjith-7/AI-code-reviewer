import streamlit as st
from llm_service import analyze_code
from llm_service import analyze_code

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="*",
    layout="wide",
)

st.title("AI Code Reviewer & Explainer")

st.write(
    "Review bugs, understand code, and discover "
    "optimization opportunities using GenAI."
)

language = st.selectbox(
    "Programming language",
    ["Python", "SQL"],
)

action = st.selectbox(
    "Choose an action",
    [
        "Review for Bugs",
        "Explain Logic",
        "Optimize Code",
    ],
)

model = st.text_input(
    "Groq model ID",
    placeholder="Enter a supported model ID",
)

code = st.text_area(
    "Paste your code",
    height=300,
    placeholder="Paste your Python or SQL code here...",
)

if st.button("Analyze Code", type="primary"):
    if not code.strip():
        st.warning("Please enter some code.")
    elif not model.strip():
        st.warning("Please enter a supported Groq model ID.")
    else:
        try:
            with st.spinner("Analyzing your code..."):
                result = analyze_code(
                    code,
                    action,
                    language,
                    model.strip(),
                )

            st.subheader("Analysis Results")
            st.markdown(result)

        except Exception as error:
            st.error(
                "Unable to analyze the code. "
                "Check your API key, model ID, "
                "network, and API limits."
            )