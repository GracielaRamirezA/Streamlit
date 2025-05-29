# mini bot
import streamlit as st

st.title("💬 Mini Chatbot ")

# Entrada de usuario
user_input = st.chat_input("Escribe algo...")

if user_input:
    if user_input.lower() == "hola":
        response = "¡Hola! ¿Cómo estás? 😊"
    elif user_input.lower() == "adiós":
        response = "¡Hasta luego! 👋"
    else:
        response = f"{user_input} <- eso dijiste"


