import streamlit as st
import pandas as pd
import csv
from src.models.AlunoModel import AlunoModel

st.set_page_config(layout="wide")

st.title("Controle De Alunos")

col1, col2 = st.columns([1, 2])

with col1:
    tab_cadastrar, tab_atualizar, tab_deletar = st.tabs(["Cadastrar", "Atualizar", "Deletar"])

    with tab_cadastrar:
        with st.form("form_cadastrar_aluno"):
            st.write("Cadastrar Aluno")
            nome_aluno = st.text_input("Nome: ", placeholder="Informe o nome do aluno")
            cpf = st.text_input("CPF: ", placeholder="Informe o CPF do aluno")
            idade = st.number_input("Idade: ", step=1, min_value=0)
            email = st.text_input("E-mail: ", placeholder="Informe o e-mail do aluno")
            cep = st.text_input("CEP: ", placeholder="Informe o CEP do aluno")
            endereco = "cep" #Implementar conexão com correios
            st.form_submit_button("Cadastrar")

    with tab_atualizar:
        @st.dialog("Atualizar Aluno")
        def atualizar_aluno(aluno: AlunoModel):
            st.info("Deixe o campo vazio para manter o dado atual")
            nome_aluno = st.text_input("Nome: ", placeholder=aluno.nome)
            idade = st.number_input("Idade: ", step=1, min_value=0, value=aluno.idade)
            email = st.text_input("E-mail: ", placeholder=aluno.email)
            cep = st.text_input("CEP: ", placeholder=aluno.endereco)
            endereco = "cep" #Implementar conexão com correios
            st.button("Confirmar")

        with st.form("form_atualizar_aluno"):
            st.write("Atualizar Aluno")
            cpf = st.text_input("CPF: ", placeholder="Informe o CPF do aluno")
            if st.form_submit_button("Atualizar"):
                #Vou criar um objeto AlunoModel para simular que o dado vem do banco de dados
                aluno = AlunoModel.AlunoModel("12345678901", "João", 20, "M9B3S@example.com", "Rua do João 123 São Paulo SP 12345-678")
                atualizar_aluno(aluno)


    with tab_deletar:
        with st.form("form_deletar_aluno"):
            st.write("Deletar Aluno")
            cpf = st.text_input("CPF: ", placeholder="Informe o CPF do aluno")
            st.form_submit_button("Deletar", type="primary")

with col2:
    st.subheader("Alunos Cadastrados")

    #Vou criar 5 objetos AlunoModel para simular que o dado vem do banco de dados para montar a tabela
    aluno1 = AlunoModel("12345678901", "João", 20, "M9B3S@example.com", "Rua do João 123 São Paulo SP 12345-678")
    aluno2 = AlunoModel("12345678902", "Maria", 21, "M9B3S@example.com", "Rua da Maria 456 São Paulo SP 12345-678")
    aluno3 = AlunoModel("12345678903", "Pedro", 22, "M9B3S@example.com", "Rua do Pedro 789 São Paulo SP 12345-678")
    aluno4 = AlunoModel("12345678904", "Ana", 23, "M9B3S@example.com", "Rua da Ana 1011 São Paulo SP 12345-678")
    aluno5 = AlunoModel("12345678905", "Carlos", 24, "M9B3S@example.com", "Rua do Carlos 1213 São Paulo SP 12345-678")
    alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

    alunos_dic = [[aluno.cpf, aluno.nome, aluno.idade, aluno.email, aluno.endereco] for aluno in alunos]

    df = pd.DataFrame(alunos_dic, columns=["CPF", "Nome", "Idade", "E-mail", "Endereço"])

    st.table(df)

    if st.button("Exportar"):
        df.to_csv("output/alunos.csv", index=False, sep=";", header=False, quoting=csv.QUOTE_NONNUMERIC)
