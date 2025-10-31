# agent.py
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

class Agent:
    def chat(self, prompt: str):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

agent = Agent()
