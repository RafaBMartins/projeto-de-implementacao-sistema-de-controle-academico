import sqlite3 as sq3
import requests 
import json


#código para cadastrar novo aluno
while True:
    try:
        banco=sq3.connect('controle_academico.db')

        cursor=banco.cursor()

        nome_aluno=input('Informe o nome: ')
        cpf=str(input('Informe o CPF: '))
        idade=str(input('Informe a idade: '))
        email=input('Informe o e-mail: ')
        cep=input('Informe o CEP: ')

        endereco="cep" #Implementar conexão com correios
        cursor.execute('INSERT INTO Aluno VALUES("'+cpf+'","'+nome_aluno+'","'+idade+'","'+email+'","'+endereco+'")')

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
#codigo para atualizar um aluno

cpf=input('Informe o CPF do aluno a ser atualizado')

banco=sq3.connect('controle_academico.db')

cursor=banco.cursor()

cursor.execute("SELECT * FROM Aluno WHERE cpf =?",(cpf,))

registro=cursor.fetchone()

banco.close()

if not registro:
    print("CPF não encontrado")
else:
    
    

