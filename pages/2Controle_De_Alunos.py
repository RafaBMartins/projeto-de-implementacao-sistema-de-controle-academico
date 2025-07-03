import streamlit as st
import pandas as pd
import csv
import requests
from src.models.AlunoModel import AlunoModel
from src.controllers.AlunoController import AlunoControler

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
            if st.form_submit_button("Cadastrar"):
                aluno = AlunoModel(cpf, nome_aluno, idade, email, cep)
                try:
                    aluno_controller = AlunoControler(aluno)
                    aluno_controller.cadastrar_aluno()
                    st.success("Aluno cadastrado com sucesso")
                except Exception as erro_message:
                    st.error(erro_message)

    with tab_atualizar:
        @st.dialog("Atualizar Aluno")
        def atualizar_aluno(aluno: AlunoModel):
            st.info("Deixe o campo vazio para manter o dado atual")
            nome_aluno = st.text_input("Nome: ", placeholder=aluno.nome)
            idade = st.number_input("Idade: ", step=1, min_value=0, value=aluno.idade)
            email = st.text_input("E-mail: ", placeholder=aluno.email)
            cep = st.text_input("CEP: ", placeholder=aluno.cep)
            if st.button("Confirmar"):
                aluno = AlunoModel(aluno.cpf, nome_aluno, idade, email, cep)
                try:
                    aluno_controller = AlunoControler(aluno)
                    aluno_controller.atualizar_aluno()
                    st.success("Aluno atualizado com sucesso")
                    st.rerun()
                except Exception as erro_message:
                    st.error(erro_message)

        with st.form("form_atualizar_aluno"):
            st.write("Atualizar Aluno")
            cpf = st.text_input("CPF: ", placeholder="Informe o CPF do aluno")
            if st.form_submit_button("Atualizar"):
                try:
                    aluno_controller = AlunoControler()
                    aluno = aluno_controller.buscar_por_cpf(cpf)
                    atualizar_aluno(aluno)
                except Exception as erro_message:
                    st.error(erro_message)


    with tab_deletar:
        with st.form("form_deletar_aluno"):
            st.write("Deletar Aluno")
            cpf = st.text_input("CPF: ", placeholder="Informe o CPF do aluno")
            if st.form_submit_button("Deletar", type="primary"):
                try:
                    aluno_controller = AlunoControler()
                    aluno_controller.deletar_aluno(cpf)
                    st.success("Aluno deletado com sucesso")
                except Exception as erro_message:
                    st.error(erro_message)

with col2:
    st.subheader("Alunos Cadastrados")

    try:
        aluno_controller = AlunoControler()
        alunos = aluno_controller.buscar_todos_alunos()

        if not alunos:
            df = pd.DataFrame([["Nenhum aluno encontrado"]], columns=["Mensagem"])
            st.table(df)

            if st.button("Exportar"):
                df.to_csv("output/alunos.csv", index=False, sep=";", header=False, quoting=csv.QUOTE_NONNUMERIC)
        else:
            alunos_list = [[aluno.cpf, aluno.nome, aluno.idade, aluno.email, aluno.cep] for aluno in alunos]

            for aluno in alunos_list:
                PATH_CORREIOS = f"https://viacep.com.br/ws/{aluno[4]}/json/"
                response = requests.get(PATH_CORREIOS)
                endereco = response.json()
                aluno.append(endereco["logradouro"])
                aluno.append(endereco["bairro"])
                aluno.append(endereco["localidade"])

            df = pd.DataFrame(alunos_list, columns=["CPF", "Nome", "Idade", "E-mail", "CEP", "Logradouro", "Bairro", "Cidade"])
            st.table(df)
            st.write("Total de alunos cadastrados: ", len(alunos))

            if st.button("Exportar"):
                df.to_csv("output/alunos.csv", index=False, sep=";", header=False, quoting=csv.QUOTE_NONNUMERIC)

    except Exception as erro_message:
        st.error(erro_message)
