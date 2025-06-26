import streamlit as st
import database as db

#Definindo a paginação na tela
st.set_page_config(page_title="Credenciamento", layout="wide")
st.title("📋 Formulário de Credenciamento")

#Chamando a função de criar a tabela do Banco
db.criar_tabela()

#===========================================================================================================

#FORMULÁRIO

#Definindo o formulário
with st.form('form_cadastro', clear_on_submit=True):
    nome = st.text_input('Nome Completo', placeholder='Digite o nome do aluno')
    idade = st.number_input('Idade', min_value=0, max_value=120)
    grau = st.selectbox('Grau', ['Ensino Fundamental', 'Ensino Médio', 'Ensino Superior', 'Pós-Graduação', 'Outro'])
    genero = st.radio('Gênero', ['Masculino', 'Feminino', 'Outro'])
    cadastrar = st.form_submit_button('Cadastrar Aluno')


#===========================================================================================================


#Realizando a condição caso o usuário existar cancelar cadastro, caso contrrário adicionar
if cadastrar:
    
    #Chamando a função do databse para adicionar aluno
    if nome:
        db.adicionar_aluno(nome, idade, grau, genero)
        st.success(f'Aluno "{nome}" cadastrado com sucesso!')
    else:
        st.error("O campo 'Nome' é obrigatório.")

