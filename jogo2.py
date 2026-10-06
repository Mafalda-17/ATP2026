import random

def computador():
    máx=100
    total=0
    computador=1
    total= total+computador
    print("Computador escolheu:", computador)
    print("Total:", total)
    while total<100:
        jogador=int(input("Escolha um número de 1 a 10:"))
        while jogador < 1 or jogador > 10:
            print("Número inválido!")
            jogador = int(input("Escolha um número de 1 a 10: "))
        total= total + jogador
        print("Total=", total)
        if total<100:
            computador= 11 - jogador
            total= total+computador
            print("Computador escolheu:", computador)
            print("Total:",total)
    if total==100:
        if jogador == 11 - computador:
            print("Computador venceu!")
computador()

def jogador():
    total= 0
    ultima_jogada= ""
    while total<100:
        jogador=int(input("Escolha um número de 1 a 10:"))
        while jogador < 1 or jogador > 10:
                print("Número inválido!")
                jogador = int(input("Escolha um número de 1 a 10: "))
        total= total + jogador
        print("Total:", total)
        ultima_jogada="jogador"
        if total<100:
            computador= 11-jogador
            total= total + computador
            print("O computador escolheu", computador)
            print("Total:", total)
            ultima_jogada= "computador"
    if total==100:
        if ultima_jogada == "computador":
            print("Computador venceu!")
        else:
            print("O jogador venceu!")
jogador()



