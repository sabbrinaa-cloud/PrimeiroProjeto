import streamlit
import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="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")
#titulo  #markdown
st.write("### Chatbot da Sabrina") 

if not "lista_mensagens" in st.session_state:
     st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role":"user","content":texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    
    #IA Respondeu 
    resposta_ia = modelo_ia.chat.completions.create(messages=st.session_state["lista_mensagens"], model="gpt-4o")

    texto_resposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content":texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia) 
 





