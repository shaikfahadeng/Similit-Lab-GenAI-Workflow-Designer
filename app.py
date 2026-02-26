import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompt_engine import build_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Similit Lab — GenAI Idea Sandbox")
st.write("Design your AI solution using structured guidance.")

problem = st.text_area("Problem to solve")
users = st.text_input("Target users")
data_input = st.text_input("Data input type")
output = st.text_input("Expected output")

automation = st.selectbox(
    "Automation level",
    ["Manual assist", "Semi automated", "Fully autonomous"]
)

if st.button("Generate AI Solution Blueprint"):

    prompt = build_prompt(problem, users, data_input, output, automation)

    with st.spinner("AI architect thinking..."):

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content

    st.subheader("AI Generated Solution")
    st.write(result)