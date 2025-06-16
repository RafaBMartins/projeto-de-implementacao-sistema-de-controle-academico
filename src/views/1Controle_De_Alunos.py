import sqlite3 as sq3

banco=sq3.connect('controle_academico.db')

cursor=banco.cursor()

nome_aluno=input('Informe o nome: ')
cpf=int(input('Informe o CPF: '))
idade=int(input('Informe a idade: '))
email=input('Informe o e-mail: ')
cep=input('Informe o CEP: ')

endereco="cep" #Implementar conexão com correios
cursor.execute('INSERT INTO Aluno VALUES('+cpf+','+nome_aluno+','+idade+','+email+','+endereco+')')

banco.commit()
banco.close()




