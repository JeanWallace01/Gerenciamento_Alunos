import streamlit as st
import database as db

#Definindo a paginação na tela
st.set_page_config(page_title="Alunos Cadastrados", layout="wide")
st.title("📑 Alunos Cadastrados")

#Chamando a função de visualizar os dados
df = db.visualizar_dados()

#Caso o dataframe não esteja vazio mostrar na tela 
if not df.empty:
    st.dataframe(df)
else:
    st.warning("Nenhum aluno cadastrado ainda.")
