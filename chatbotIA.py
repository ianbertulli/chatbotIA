#streamlit frontend e backend para criação de sites

# exemplo de lista:
# nomes["amor", "ian", "piolho", "khan"]
# como selecionar um item da lista: primeiro_item = nomes[0]

# dicionário (para armazenar a lista de mensagens do chat)
# role = quem enviou a mensagem (função)
# content = texto da mensagem (conteúdo)

#exemplo de dicionário:
# mensagem = {"quem": "user", "content": "olá"}
# como selecionar um item do dicionário: texto_mensagem = mensagem["content"]

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

chave = os.getenv("APIkey")

genai.configure(api_key=chave)
model =  genai.GenerativeModel("gemini-2.5-flash-lite")

st.write("""
         # ChatBot com IA
         Olá! Este site é uma demonstração do uso das ferramentas Streamlit e Google Generative IA, em Python.""")#markdown

# session state = memória do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# para adicionar uma mensagem:
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Digite sua mensagem aqui")

if mensagem_usuario:
    # user = ser humano
    # assistant = IA
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo = model.generate_content(mensagem_usuario)
    resposta_ia = resposta_modelo.text
    print(resposta_modelo.text)
    print(mensagem_usuario)

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)