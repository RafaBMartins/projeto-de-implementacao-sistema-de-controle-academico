import streamlit as st
import sqlite3 as sq3

st.set_page_config(layout="wide", page_title="Sistema De Controle Acadêmico")

st.title("Projeto de Implementação - Sistema De Controle Acadêmico")

st.subheader("Desenvolvido por: ")
st.write("Rafael Barbosa Martins e Gabriel Medeiros")

st.subheader("Link do GitHub: ")
st.write("https://github.com/RafaBMartins/projeto-de-implementacao-sistema-de-controle-academico")

def criando_tabelas_banco_de_dados():
    conn = sq3.connect('registro_academico.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS alunos (cpf TEXT PRIMARY KEY, nome TEXT NOT NULL, idade INTEGER NOT NULL, email TEXT NOT NULL, cep TEXT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS disciplinas (codigo TEXT PRIMARY KEY, nome TEXT NOT NULL, carga_horaria INTEGER NOT NULL, professor TEXT NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS matriculas (cpf_aluno TEXT, codigo_disciplina TEXT, data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (cpf_aluno) REFERENCES alunos(cpf), FOREIGN KEY (codigo_disciplina) REFERENCES disciplinas(codigo))")
    conn.commit()
    conn.close()

criando_tabelas_banco_de_dados()
