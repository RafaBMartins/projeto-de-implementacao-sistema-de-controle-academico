import streamlit as st

import sqlite3 as sq3

while True:
    try:
        banco=sq3.connect('controle_academico.db')

        cursor=banco.cursor()

        codigo_disc=str(input('Informe o código da disciplina: '))
        nome_disc=input('Informe o nome da disciplina a ser cadastrada: ')
        carga_horaria=str(input('Informe a carga horária da disciplina: '))
        nome_professor=input('Informe o nome do professor da matéria: ')

        cursor.execute('INSERT INTO Disciplina VALUES("'+codigo_disc+'","'+nome_disc+'","'+carga_horaria+'","'+nome_professor+'","'+endereco+'")')

        banco.commit()
        
    except sq3.IntegrityError:
        print("Código de disciplina já cadastrado no sistema!")
        #implementar para quando esse erro aparecer, redirecionar para edição
        #da disciplina com o código informado
        break
    except sq3.Error as erro:
        print("Erro inesperado: {erro}")
        break
    finally:
        banco.close()
    break



