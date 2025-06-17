import sqlite3 as sq3
import requests 
import json


#código para cadastrar novo aluno
while True:
    try:
        banco=sq3.connect('controle_academico.db')

        cursor=banco.cursor()

        nome_aluno=input('Informe o nome: ')
        cpf=int(input('Informe o CPF: '))
        idade=int(input('Informe a idade: '))
        email=input('Informe o e-mail: ')
        cep=input('Informe o CEP: ')

        endereco="cep" #Implementar conexão com correios
        cursor.execute('INSERT INTO Aluno VALUES("'+str(cpf)+'","'+nome_aluno+'","'+str(idade)+'","'+email+'","'+endereco+'")')

        banco.commit()
        
    except sq3.IntegrityError:
        print("CPF já cadastrado no sistema!")
        break
    except sq3.Error as erro:
        print("Erro inesperado: {erro}")
        break
    finally:
        banco.close()
    break




