
menu= """
        Menu:
              1- Criar uma turma
              2- Inserir um aluno na turma
              3- Listar turma
              4- Consultar um aluno por id
              8- Guardar a turma em ficheiro                  
              9- Carregar uma turma dum ficheiro
              0- Sair da aplicação"""

def criar_turma():
    return[]


def existe_id(turma, id_aluno):
    encontrado= False
    for aluno in turma:
        if aluno[1]== id_aluno:
            encontrado = True
    return encontrado


def inserir_aluno(turma):
    nome= input("Nome:")
    id_aluno= input("Id do aluno:")
    if existe_id(turma, id_aluno):
        print("Já existe um aluno com esse id.")
    else:
        notaTPC= float(input("Nota do TPC:"))
        notaProj= float(input("Nota do Projeto:"))
        notaTeste= float(input("Nota do Teste:"))
        aluno = (nome, id_aluno, [notaTPC, notaProj, notaTeste])
        turma.append(aluno)
        print("Aluno inserido com sucesso.")
    return turma

def listar_turma(turma):
    if len(turma)== 0:
        print("A turma está vazia.")
    else: 
        for nome, id_aluno, notas in turma:
            print("Nome:", nome)
            print("Id do aluno:", id_aluno)
            print("Nota TPC:", notas[0])
            print("Nota Projeto:", notas[1])
            print("Nota Teste:", notas[2])
            print()
            

def consultar_aluno(turma):
    id_aluno= input("Id do aluno:")
    encontrado = False
    for nome, id_a, notas in turma:
        if id_a== id_aluno:
            encontrado= True
            print(f"Nome: {nome} ")
            print(f"Id do aluno: {id_a}")
            print(f"Nota do TPC: {notas[0]}")
            print(f"Nota do Projeto: {notas[1]}")
            print(f"Nota do Teste: {notas[2]}")
    if not encontrado:
        print("Aluno não encontrado.")


def guardar_turma(turma):
    nome_ficheiro= input("Nome do ficheiro:")
    ficheiro= open(nome_ficheiro, "w")
    for aluno in turma:
        nome = aluno[0]
        id_aluno = aluno[1]
        notas = aluno[2]
        ficheiro.write(nome)
        ficheiro.write("\n")
        ficheiro.write(id_aluno)
        ficheiro.write("\n")
        ficheiro.write(str(notas[0]))
        ficheiro.write("\n")
        ficheiro.write(str(notas[1]))
        ficheiro.write("\n")
        ficheiro.write(str(notas[2]))
        ficheiro.write("\n")
    ficheiro.close()
    print("Turma guardada em", nome_ficheiro)
    


def carregar_turma():
    nome_ficheiro = input("Nome do ficheiro: ")
    ficheiro = open(nome_ficheiro, "r")
    turma = []
    linhas = []
    for linha in ficheiro:
        linhas.append(linha[:-1])
    for i in range(0, len(linhas), 5):
        nome = linhas[i]
        id_aluno = linhas[i + 1]
        notaTPC = float(linhas[i + 2])
        notaProj = float(linhas[i + 3])
        notaTeste = float(linhas[i + 4])
        aluno = (nome, id_aluno, [notaTPC, notaProj, notaTeste])
        turma.append(aluno)
    ficheiro.close()
    print("Turma carregada.")
    return turma


turma=[]
opcao= ""
while opcao!=0:
    print(menu)
    opcao= int(input("Opção:"))
    if opcao==1:
        turma= criar_turma()
        print("Turma criada.")
    elif opcao==2:
        turma= inserir_aluno(turma)
    elif opcao==3:
        listar_turma(turma)
    elif opcao==4:
        consultar_aluno(turma)
    elif opcao==8:
        guardar_turma(turma)
    elif opcao==9:
        turma= carregar_turma()
    elif opcao==0:
        print("Saiu da aplicação.")
    else:
        print("Opção invalida.")

