import streamlit as st
import pandas as pd
import csv
from datetime import datetime
from src.models.MatriculaModel import MatriculaModel
from src.controllers.MatriculaController import MatriculaController
from src.controllers.AlunoController import AlunoControler
from src.controllers.DisciplinaController import DisciplinaController

st.set_page_config(layout="wide")

st.title("Controle De Matriculas")

col1, col2 = st.columns([1, 2])

with col1:
    tab_matricular, tab_cancelar = st.tabs(["Cadastrar", "Deletar"])

    with tab_matricular:
        with st.form("form_matricular_aluno"):
            st.write("Matricular Aluno")
            aluno_controller = AlunoControler()
            alunos = aluno_controller.buscar_todos_alunos()
            cpf_aluno = st.selectbox("Aluno: ", [aluno.cpf for aluno in alunos], placeholder="Selecione um aluno")
            disciplina_controller = DisciplinaController()
            disciplinas = disciplina_controller.buscar_todas_disciplinas()
            codigo_disciplina = st.selectbox("Disciplina: ", [disciplina.codigo for disciplina in disciplinas], placeholder="Selecione uma disciplina")
            if st.form_submit_button("Cadastrar"):
                matricula = MatriculaModel(cpf_aluno, codigo_disciplina, None)
                try:
                    matricula_controller = MatriculaController(matricula)
                    matricula_controller.cadastrar_matricula()
                    st.success("Matricula cadastrada com sucesso")
                except Exception as erro_message:
                    st.error(erro_message)


    with tab_cancelar:
        with st.form("form_deletar_matricula"):
            st.write("Cancelar Matrícula")
            aluno_controller = AlunoControler()
            alunos = aluno_controller.buscar_todos_alunos()
            cpf_aluno = st.selectbox("Aluno: ", [aluno.cpf for aluno in alunos], placeholder="Selecione um aluno")
            disciplina_controller = DisciplinaController()
            disciplinas = disciplina_controller.buscar_todas_disciplinas()
            codigo_disciplina = st.selectbox("Disciplina: ", [disciplina.codigo for disciplina in disciplinas], placeholder="Selecione uma disciplina")
            if st.form_submit_button("Deletar", type="primary"):
                try:
                    matricula_controller = MatriculaController()
                    matricula_controller.deletar_matricula(cpf_aluno, codigo_disciplina)
                    st.success("Matricula deletada com sucesso")
                except Exception as erro_message:
                    st.error(erro_message)

with col2:
    st.subheader("Matriculas Cadastradas")

    try:
        matricula_controller = MatriculaController()
        matriculas = matricula_controller.buscar_todas_matriculas()

        if not matriculas:
            df = pd.DataFrame([["Nenhuma matricula encontrada"]], columns=["Mensagem"])
            st.table(df)

            if st.button("Exportar"):
                df.to_csv("output/matriculas.csv", index=False, sep=";", header=False, quoting=csv.QUOTE_NONNUMERIC)
        else:
            matriculas_list = [[matricula.cpf_aluno, matricula.codigo_disciplina, datetime.strptime(matricula.data_hora, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M:%S")] for matricula in matriculas]
            df = pd.DataFrame(matriculas_list, columns=["CPF Aluno", "Código Disciplina", "Data/Hora"])
            st.table(df)
            st.write("Total de matriculas cadastradas: ", len(matriculas))

            if st.button("Exportar"):
                df.to_csv("output/matriculas.csv", index=False, sep=";", header=False, quoting=csv.QUOTE_NONNUMERIC)

    except Exception as erro_message:
        st.error(erro_message)