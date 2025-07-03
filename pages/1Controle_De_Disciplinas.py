import streamlit as st
import pandas as pd
import csv
from src.models.DisciplinaModel import DisciplinaModel
from src.controllers.DisciplinaController import DisciplinaController

st.set_page_config(layout="wide")

st.title("Controle De Disciplinas")

col1, col2 = st.columns([1, 2])

with col1:
    tab_cadastrar, tab_atualizar, tab_deletar = st.tabs(["Cadastrar", "Atualizar", "Deletar"])

    with tab_cadastrar:
        with st.form("form_cadastrar_disciplina"):
            st.write("Cadastrar Disciplina")
            codigo_disciplina = st.text_input("Código: ", placeholder="Informe o código da disciplina")
            nome_disciplina = st.text_input("Nome: ", placeholder="Informe o nome da disciplina")
            carga_horaria = st.number_input("Carga Horária: ", step=1, min_value=0)
            nome_professor = st.text_input("Professor: ", placeholder="Informe o nome do professor")
            if st.form_submit_button("Cadastrar"):
                disciplina = DisciplinaModel(codigo_disciplina, nome_disciplina, carga_horaria, nome_professor)
                try:
                    disciplina_controller = DisciplinaController(disciplina)
                    disciplina_controller.cadastrar_disciplina()
                    st.success("Disciplina cadastrada com sucesso")
                except Exception as erro_message:
                    st.error(erro_message)

    with tab_atualizar:
        @st.dialog("Atualizar Disciplina")
        def atualizar_disciplina(disciplina: DisciplinaModel):
            st.info("Deixe o campo vazio para manter o dado atual")
            nome_disciplina = st.text_input("Nome: ", placeholder=disciplina.nome)
            carga_horaria = st.number_input("Carga Horária: ", step=1, min_value=0, value=disciplina.carga_horaria)
            nome_professor = st.text_input("Professor: ", placeholder=disciplina.professor)
            if st.button("Confirmar"):
                disciplina = DisciplinaModel(disciplina.codigo, nome_disciplina, carga_horaria, nome_professor)
                try:
                    disciplina_controller = DisciplinaController(disciplina)
                    disciplina_controller.atualizar_disciplina()
                    st.success("Disciplina atualizada com sucesso")
                    st.rerun()
                except Exception as erro_message:
                    st.error(erro_message)

        with st.form("form_atualizar_disciplina"):
            st.write("Atualizar Disciplina")
            codigo_disciplina = st.text_input("Código: ", placeholder="Informe o código da disciplina")
            if st.form_submit_button("Atualizar"):
                try:
                    disciplina_controller = DisciplinaController()
                    disciplina = disciplina_controller.buscar_por_codigo(codigo_disciplina)
                    atualizar_disciplina(disciplina)
                except Exception as erro_message:
                    st.error(erro_message)

    with tab_deletar:
        with st.form("form_deletar_disciplina"):
            st.write("Deletar Disciplina")
            codigo_disciplina = st.text_input("Código: ", placeholder="Informe o código da disciplina")
            if st.form_submit_button("Deletar", type="primary"):
                try:
                    disciplina_controller = DisciplinaController()
                    disciplina_controller.deletar_disciplina(codigo_disciplina)
                    st.success("Disciplina deletada com sucesso")
                except Exception as erro_message:
                    st.error(erro_message)

with col2:
    st.subheader("Disciplinas Cadastradas")

    try:
        disciplina_controller = DisciplinaController()
        disciplinas = disciplina_controller.buscar_todas_disciplinas()

        if not disciplinas:
            df = pd.DataFrame([["Nenhuma disciplina encontrada"]], columns=["Mensagem"])
            st.table(df)

            if st.button("Exportar"):
                df.to_csv("output/disciplinas.csv", index=False, sep=";", header=False, quoting=csv.QUOTE_NONNUMERIC)
        else:
            disciplinas_list = [[disciplina.codigo, disciplina.nome, disciplina.carga_horaria, disciplina.professor] for disciplina in disciplinas]
            df = pd.DataFrame(disciplinas_list, columns=["Código", "Nome", "Carga Horária", "Professor"])
            st.table(df)

            if st.button("Exportar"):
                df.to_csv("output/disciplinas.csv", index=False, sep=";", header=False, quoting=csv.QUOTE_NONNUMERIC)

    except Exception as erro_message:
        st.error(erro_message)