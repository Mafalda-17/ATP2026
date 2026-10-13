import random 
lista=[]
Menu= """ 
            Menu:
                (1) Criar Lista
                (2) Ler Lista
                (3) Soma
                (4) Média
                (5) Maior
                (6) Menor
                (7) estaOrdenada por ordem crescente
                (8) estaOrdenada por ordem decrescente
                (9) Procura um elemento
                (0) Sair
                """

def CriarLista():
    lista.clear()
    n= int(input("Quantos elementos quer na lista:"))
    for i in range(n):
        lista.append(random.randint(1 , 100))



def LeLista(n):
    lista=[]
    contador= 0
    while contador<n:
        num=int(input("Introduza um número:"))
        lista.append(num)
        contador= contador + 1
    return lista


def SomaLista():
    soma=0
    for elem in lista:
        soma= soma + elem
    return soma


def mediaLista():
    return SomaLista() / len(lista)



def MaiorLista():
    maior= lista[0]
    for elem in lista:
        if elem>maior:
            maior=elem
    return maior


def MenorLista():
    menor= lista[0]
    for elem in lista:
        if elem<menor:
            menor=elem
    return menor


def estaOrdenada_crescente():
    i = 0
    res= True
    while i < len(lista) -1 and res:
        if lista[i] > lista[i + 1]:
            res= False
        i = i + 1
    return res

def estaOrdenada_decrescente():
    i = 0 
    res = True
    while i < len(lista) -1 and res:
        if lista[i] < lista[i + 1]:
            res= False
        i = i + 1
    return res


def procura(lista, elem):
    res= -1
    i = 0
    encontrei= False
    while i < len(lista) and not encontrei:
            if lista[i]==elem:
                res= i
                encontrei= True
            i = i + 1
    return res

opcao= ""
while opcao!= "0":
    print(Menu)
    opcao= input("Opção:")
    if opcao== "1":
        CriarLista()
        print(f"Lista criada: {lista}")
    elif opcao == "2":
        n= int(input("Quantos elementos quer na lista:"))
        lista = LeLista(n)
        print(f"Lista guardada: {lista}")
    elif opcao== "3":
        print(f"Soma: {SomaLista()}")
    elif opcao== "4":
            print(f"Média: {mediaLista()}")
    elif opcao== "5":
            print(f"Maior número da lista: {MaiorLista()}")
    elif opcao== "6":
            print(f"Menor número da lista: {MenorLista()}")
    elif opcao== "7":
        if estaOrdenada_crescente():
            print("Sim")
        else:
             print("Não")
    elif opcao== "8":
        if estaOrdenada_decrescente():
            print("Sim")
        else:
             print("Não")
    elif opcao== "9":
          elem = int(input("Elemento a procurar: "))
          print(procura(lista, elem))
    elif opcao== "0":
         print(f"Lista guardada: {lista}")
         print("Saiu da Aplicação.")
    else:
         print("Opção inválida. Escolha um número de 0 a 9.")
