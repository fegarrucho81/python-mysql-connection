import mysql.connector
from configparser import ConfigParser

config = ConfigParser()
config.read('C:\\Users\\felip\\OneDrive\\Área de Trabalho\\FELIPE\\fundação bradesco\\python\\python avançado\\python with sql\\src\\config.ini')

myDb = mysql.connector.connect(
    host="localhost",
    user=config.get('mysql', 'user'),
    password=config.get('mysql', 'password'),
    database="agenda"
)

if myDb.is_connected():
    print("Conexão bem-sucedida!")


mycursor = myDb.cursor()


def adicionar_aluno(nome, data_nascimento, endereco, telefone, turma, notas, id_disciplina):
    try:
        myDb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1Flp2004a!",
            database="agenda"
        )
        mycursor = myDb.cursor()
        sql_insert_aluno = "INSERT INTO tb_alunos (nome_aluno, data_nascimento, endereco_aluno, telefone_aluno, turma_aluno, notas, id_disciplina) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores_aluno = (nome, data_nascimento, endereco, telefone, turma, notas, id_disciplina)
        mycursor.execute(sql_insert_aluno, valores_aluno)
        myDb.commit()
        print("Aluno adicionado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao adicionar aluno: {err}")
    finally:
        if myDb.is_connected():
            mycursor.close()
            myDb.close()


def remover_aluno(id_aluno):
    try:
        myDb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1Flp2004a!",
            database="agenda"
        )
        mycursor = myDb.cursor()
        sql_delete_aluno = "DELETE FROM tb_alunos WHERE id_aluno = %s"
        mycursor.execute(sql_delete_aluno, (id_aluno,))
        myDb.commit()
        print("Aluno removido com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao remover aluno: {err}")
    finally:
        if myDb.is_connected():
            mycursor.close()
            myDb.close()


def consultar_alunos():
    try:
        myDb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1Flp2004a!",
            database="agenda"
        )
        mycursor = myDb.cursor()
        mycursor.execute("SELECT * FROM tb_alunos")
        alunos = mycursor.fetchall()
        for aluno in alunos:
            print(aluno)
    except mysql.connector.Error as err:
        print(f"Erro ao consultar alunos: {err}")
    finally:
        if myDb.is_connected():
            mycursor.close()
            myDb.close()


def menu():
    print("Menu:")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Consultar alunos")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
        endereco = input("Digite o endereço do aluno: ")
        telefone = input("Digite o telefone do aluno: ")
        turma = input("Digite a turma do aluno: ")
        notas = float(input("Digite a nota do aluno: "))
        id_disciplina = int(input("Digite o ID da disciplina: "))
        adicionar_aluno(nome, data_nascimento, endereco, telefone, turma, notas, id_disciplina)
    elif opcao == "2":
        id_aluno = int(input("Digite o ID do aluno a ser removido: "))
        remover_aluno(id_aluno)
    elif opcao == "3":
        consultar_alunos()
    elif opcao == "4":
        print("Encerrando o programa.")
        return
    else:
        print("Opção inválida.")

    menu() 


menu()


mycursor.close()
myDb.close()