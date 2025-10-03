import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
if not API_TOKEN:
    st.error("API Token not found! Please create a .env file with your Hugging Face token.")
    st.stop() 
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
st.title("📄 AI Question-Answering Bot")
st.write("This bot can answer questions based on the text provided below.")

context = st.text_area("Context", """
The James Webb Space Telescope (JWST) is the most powerful space telescope ever built. 
Launched in December 2021, it is designed to see the universe in infrared light, 
allowing it to observe the first stars and galaxies that formed after the Big Bang.
""", height=150)

question = st.text_input("Ask a question about the context")

if st.button("Get Answer"):
    if not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("AI is thinking..."):
            api_payload = {
                "inputs": {
                    "question": question,
                    "context": context
                }
            }
            output = query(api_payload)
            
            if 'error' in output:
                st.error(f"Error: {output['error']}")
            else:
                st.success(f"**Answer:** {output.get('answer', 'No answer found.')}")