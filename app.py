import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from courses import course_data

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY not found!")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)

# System Prompt
SYSTEM_PROMPT = """
You are a Course Information Assistant.

You must:
1. Read the user’s question.
2. Identify the course (by code or title).
3. Identify what field they want (lecturer, credits, objective, prerequisites, resources, title).
4. Answer using ONLY the course_data dictionary provided.
5. If the course or field does not exist, say so.
6. Never hallucinate; do not invent details.
"""

# Gemini LLM Function
def gemini_answer(query):
    prompt = f"{SYSTEM_PROMPT}\n\nHere is the course_data dictionary:\n{course_data}\n\nUser Question: {query}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# Streamlit UI
st.set_page_config(page_title="Course Resource Locator", page_icon="🎓")
st.title("🎓 Course Resource Locator")
st.write("Ask anything about FAS degree programs (lecturer, credits, prerequisites, resources, objective, title).")

query = st.text_input("💬 Type your question:")

if query:
    with st.spinner("Thinking..."):
        try:
            answer = gemini_answer(query)

            st.markdown(
                f"""
                <div style="
                    border: 2px solid #4CAF50;
                    border-radius: 15px;
                    padding: 20px;
                    background-color: #f9fff9;
                    box-shadow: 0 0 15px rgba(0,0,0,0.1);
                    margin-bottom: 20px;
                    white-space: pre-wrap;
                ">
                    {answer}
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Error: {e}")
