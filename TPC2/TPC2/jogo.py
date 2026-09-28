import random
def jogo1():
    print("O computador vai pensar num número de 0 a 100")
    num=random.randint(0,100)
    tentativa= 0
    while True:
        palpite= int(input("Introduza um número de 0 a 100:"))
        tentativa= tentativa + 1
        if palpite == num:
            print(f"Acertou com {tentativa} tentativas!")
            break
        elif palpite<num:
            print("O número que pensei é maior.")
        else:
            print("O número que pensei é menor.")
jogo1()

def jogo2():
    print("Pensa num número de 0 a 100.")
    minimo=0
    maximo=100
    tentativa=0
    while minimo<=maximo:
        palpite=(minimo+maximo)//2
        tentativa= tentativa + 1
        print(f" O meu palpite é {palpite}.")
        resposta= input("Escreve 'Acertou!', ' Maior', 'Menor':")
        if resposta== "Acertou!":
            print(f"Acertou!")
            break
        elif resposta== "Maior":
             minimo= palpite + 1
        else:
            maximo= palpite - 1
    print(f"Acertei com {tentativa} tentativas!")
jogo2()



           

