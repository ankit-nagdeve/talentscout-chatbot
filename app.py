
import streamlit as st
from utils.llm import get_tech_questions
from prompts.base import GREETING_PROMPT, ENDING_KEYWORDS

st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")

st.title("🤖 TalentScout - Hiring Assistant Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []
    st.session_state.tech_stack = ""
    st.session_state.ended = False

def collect_info():
    st.subheader("📋 Candidate Information")
    full_name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.slider("Years of Experience", 0, 20, 0)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_input("Tech Stack (comma-separated)")
    submit = st.button("Start Chat")
    return submit, full_name, email, phone, experience, position, location, tech_stack

if not st.session_state.chat:
    st.write(GREETING_PROMPT)
    submitted, name, email, phone, exp, pos, loc, techs = collect_info()
    if submitted:
        st.session_state.chat.append(f"Name: {name}, Email: {email}, Phone: {phone}")
        st.session_state.tech_stack = techs
        st.session_state.chat.append(f"Experience: {exp} years")
        st.session_state.chat.append(f"Desired Position: {pos} at {loc}")
        st.session_state.chat.append(f"Tech Stack: {techs}")

        questions = get_tech_questions(techs)
        st.session_state.chat += questions

else:
    st.subheader("🧠 Interview Questions")
    for msg in st.session_state.chat:
        st.write("- " + msg)

    user_input = st.text_input("Your Message")
    if user_input:
        if any(k in user_input.lower() for k in ENDING_KEYWORDS):
            st.session_state.ended = True
            st.write("✅ Thank you! We’ll contact you with next steps.")
        else:
            st.write("📝 Response recorded.")
