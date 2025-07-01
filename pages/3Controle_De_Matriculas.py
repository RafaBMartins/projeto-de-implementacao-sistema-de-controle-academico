import streamlit as st
import pandas as pd
import csv
from src.models.MatriculaModel import MatriculaModel

st.title("Controle De Matriculas")

col1, col2 = st.columns([1, 1])

with col1:
    tab_matricular, tab_cancelar = st.tabs(["Cadastrar", "Deletar"])

    with tab_matricular:
        with st.form("form_matricular_aluno"):
            st.write("Matricular Aluno")
            cpf_aluno = st.text_input("CPF: ", placeholder="Informe o CPF do aluno")
            codigo_disciplina = st.text_input("Código: ", placeholder="Informe o código da disciplina")
            st.form_submit_button("Cadastrar")

    with tab_cancelar:
        with st.form("form_deletar_matricula"):
            st.write("Cancelar Matrícula")
            cpf_aluno = st.text_input("CPF: ", placeholder="Informe o CPF do aluno")
            codigo_disciplina = st.text_input("Código: ", placeholder="Informe o código da disciplina")
            st.form_submit_button("Deletar", type="primary")

with col2:
    st.subheader("Matriculas Cadastradas")

    #Vou criar 5 objetos MatriculaModel para simular que o dado vem do banco de dados para montar a tabela
    matricula1 = MatriculaModel(1, "12345678901", "12345678901", "2023-01-01 00:00:00")
    matricula2 = MatriculaModel(2, "12345678902", "12345678902", "2023-02-01 00:00:00")
    matricula3 = MatriculaModel(3, "12345678903", "12345678903", "2023-03-01 00:00:00")
    matricula4 = MatriculaModel(4, "12345678904", "12345678904", "2023-04-01 00:00:00")
    matricula5 = MatriculaModel(5, "12345678905", "12345678905", "2023-05-01 00:00:00")
    matriculas = [matricula1, matricula2, matricula3, matricula4, matricula5]

    matriculas_dict = [[matricula.cpf_aluno, matricula.codigo_disciplina, matricula.data_hora] for matricula in matriculas]

    df = pd.DataFrame(matriculas_dict, columns=["CPF Aluno", "Código Disciplina", "Data Hora"])

    st.table(df)

    if st.button("Exportar"):
        df.to_csv("output/matriculas.csv", index=False, sep=";", header=False, quoting=csv.QUOTE_NONNUMERIC)