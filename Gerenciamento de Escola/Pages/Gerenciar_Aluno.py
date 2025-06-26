import streamlit as st
import database as db  

# Entrada do nome para busca
nome_busca = st.text_input("Digite o nome do aluno para buscar")


#======================================================================================================#


#BOTÃO INPUT
if st.button("Buscar"):
    # Chama a função para buscar o aluno no banco de dados
    aluno = db.buscar_aluno(nome_busca)

    if aluno:
        # Se o aluno for encontrado, salva os dados no session_state
        st.session_state.aluno_encontrado = aluno
    else:
        # Se não encontrar, mostra erro e limpa qualquer aluno anterior no estado
        st.error("Aluno não encontrado.")
        st.session_state.aluno_encontrado = None

#======================================================================================================#


#FORMULÁRIO

# Se já existe um aluno salvo no estado, exibe o formulário
if 'aluno_encontrado' in st.session_state and st.session_state.aluno_encontrado:
    
    # Extrai os dados salvos no estado
    id_aluno, nome_atual, idade_atual, grau_atual, genero_atual = st.session_state.aluno_encontrado
    st.success("Aluno encontrado! Você pode editar os dados abaixo.")

    # Cria o formulário de edição
    with st.form("form_edicao"):
        novo_nome = st.text_input("Nome", value=nome_atual)
        nova_idade = st.number_input("Idade", value=idade_atual, min_value=0, max_value=100)
        novo_grau = st.selectbox(
            "Grau",
            ["Ensino Fundamental", "Ensino Médio", "Ensino Superior", "Pós-Graduação", "Outro"],
            index=["Ensino Fundamental", "Ensino Médio", "Ensino Superior", "Pós-Graduação", "Outro"].index(grau_atual)
        )
        novo_genero = st.selectbox(
            "Gênero",
            ["Masculino", "Feminino", "Outro"],
            index=["Masculino", "Feminino", "Outro"].index(genero_atual)
        )

        # Botões dentro do formulário
        button_renomear = st.form_submit_button('Renomear aluno')
        button_excluir = st.form_submit_button('Excluir Aluno')
        

#======================================================================================================#


#CONDIÇÃO PARA DUNÇÃO DO BOTÃO

        if button_renomear:
            # Atualiza o aluno no banco de dados
            db.atualizar_aluno(id_aluno, novo_nome, nova_idade, novo_grau, novo_genero)
            st.success('Alteração realizada com sucesso!')

        if button_excluir:
            # Exclui o aluno do banco
            db.excluir_aluno(id_aluno)
            st.success('Aluno excluído com sucesso.')

            # Limpa o estado após a exclusão para esconder o formulário
            st.session_state.aluno_encontrado = None

#======================================================================================================#