import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCpqldIOjklqL1c4nsOgyyXHUQR0wabQY4")

model = genai.GenerativeModel(model_name="gemini-pro")

st.title("Akıllı Robot")

if "messages" not in st.session_state:
    st.session_state.messages=[
        {
            "role": "assistant",
            "content": "Merhaba"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def llmCall(query):
    response=model.generate_content(query)
    with st.chat_message("assistant"):
        st.markdown(response.text)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )

query=st.chat_input("Buraya Yazın")
if query:
    with st.chat_message("user"):
        st.markdown(query)

    llmCall(query=query)