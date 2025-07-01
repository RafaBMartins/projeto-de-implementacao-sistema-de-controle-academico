import streamlit as st
import pandas as pd
import csv
from src.models.DisciplinaModel import DisciplinaModel

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
            st.form_submit_button("Cadastrar")

    with tab_atualizar:
        @st.dialog("Atualizar Disciplina")
        def atualizar_disciplina(disciplina: DisciplinaModel):
            st.info("Deixe o campo vazio para manter o dado atual")
            nome_disciplina = st.text_input("Nome: ", placeholder=disciplina.nome)
            carga_horaria = st.number_input("Carga Horária: ", step=1, min_value=0, value=disciplina.carga_horaria)
            nome_professor = st.text_input("Professor: ", placeholder=disciplina.professor)
            st.button("Confirmar")

        with st.form("form_atualizar_disciplina"):
            st.write("Atualizar Disciplina")
            codigo_disciplina = st.text_input("Código: ", placeholder="Informe o código da disciplina")
            if st.form_submit_button("Atualizar"):
                #Vou criar um objeto DisciplinaModel para simular que o dado vem do banco de dados
                disciplina = DisciplinaModel("12345678901", "Matemática", 20, "João")
                atualizar_disciplina(disciplina)

    with tab_deletar:
        with st.form("form_deletar_disciplina"):
            st.write("Deletar Disciplina")
            codigo_disciplina = st.text_input("Código: ", placeholder="Informe o código da disciplina")
            st.form_submit_button("Deletar", type="primary")

with col2:
    st.subheader("Disciplinas Cadastradas")

    #Vou criar 5 objetos DisciplinaModel para simular que o dado vem do banco de dados para montar a tabela
    disciplina1 = DisciplinaModel("12345678901", "Matemática", 20, "João")
    disciplina2 = DisciplinaModel("12345678902", "Português", 21, "Maria")
    disciplina3 = DisciplinaModel("12345678903", "História", 22, "Pedro")
    disciplina4 = DisciplinaModel("12345678904", "Geografia", 23, "Ana")
    disciplina5 = DisciplinaModel("12345678905", "Física", 24, "Carlos")
    disciplinas = [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5]

    disciplinas_dic = [[disciplina.codigo, disciplina.nome, disciplina.carga_horaria, disciplina.professor] for disciplina in disciplinas]

    df = pd.DataFrame(disciplinas_dic, columns=["Código", "Nome", "Carga Horária", "Professor"])

    st.table(df)

    if st.button("Exportar"):
        df.to_csv("output/disciplinas.csv", index=False, sep=";", header=False, quoting=csv.QUOTE_NONNUMERIC)