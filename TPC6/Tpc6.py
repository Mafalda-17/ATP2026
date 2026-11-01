menu= """
       MENU:
              1- Adicionar registro à tabela
              2- Lista tabela
              3- Temperatura média
              4- Guardar tabela em ficheiros
              5- Carregar tabela do ficheiro
              6- Temperatura mínima mais baixa
              7- Amplitude Térmica
              8- Dia de maior precipitação
              9- Dias chuvosos
              10- Maior período consecutivo de dias secos
              11- Gráficos
              0- Sair"""


def medias(tabMeteo):
    res = []
    for dia in tabMeteo:
        tmin = dia[1]
        tmax = dia[2]
        media = (tmin + tmax) / 2
        tuplo = (dia[0], media)
        res.append (tuplo)
    return res



def guardaTabMeteo(t, fnome):
    file = open(fnome, "w")
    for data, tmin, tmax, prec in t:
        ano, mes, dia = data
        file.write  (f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{prec}|\n")
    file.close()
    return



def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for line in file:
        data, tmin, tmax, prec, _ = line.split("|")
        ano, mes, dia = data.split ("-")
        tuplo = ((int(ano), int(mes), int(dia)), float(tmin), float(tmax), float(prec))
        res.append (tuplo)
    file.close()
    return res




def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for data, tmin, tmax, prec in tabMeteo:
        if tmin < minima:
            minima = tmin
    return minima


def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        res.append((data, tmax - tmin))
    return res


def maxChuva(tabMeteo):
    max_data = tabMeteo[0][0]
    max_prec = tabMeteo[0][3]
    for data, tmin, tmax, prec in tabMeteo:
        if prec > max_prec:
            max_data = data
            max_prec = prec
    return (max_data, max_prec)


def diasChuvosos(tabMeteo, p):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
    return res


def maxPeriodoCalor(tabMeteo, p):
    maximo = 0
    atual = 0
    for data, tmin, tmax, prec in tabMeteo:
        if prec < p:
            atual = atual + 1
        else:
            atual = 0
        if atual > maximo:
            maximo = atual
    return maximo

import matplotlib.pyplot as plt

def grafTabMeteo(t):
    y_min = [tmin for data, tmin, tmax, prec in t]
    y_max = [tmax for data, tmin, tmax, prec in t]
    y_prec = [prec for data, tmin, tmax, prec in t]
    
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, tmin, tmax, prec in t]
    
    plt.figure() 
    plt.plot(x, y_min, color="blue", marker="o", label="Tmin ºC")
    plt.plot(x, y_max, color="red", marker="o", label="Tmax ºC")
    plt.title("Temperatura")
    plt.xlabel("Data")
    plt.ylabel("Graus (ºC)")
    plt.legend()
    plt.grid(True)
    plt.show() 
    plt.figure()
    plt.bar(x, y_prec, color="green", label="Precipitação (mm)")
    plt.title("Precipitação")
    plt.xlabel("Data")
    plt.ylabel("Quantidade (mm)")
    plt.legend()
    plt.grid(True)
    plt.show() 

    return


tab = []

op= ""
while op!= "0":
    print(menu)
    op= input("Opção:")
    if op == "1":
            data = input("Data (AAAA-MM-DD): ")
            ano, mes, dia = data.split("-")
            tmin = float(input("Temperatura mínima: "))
            tmax = float(input("Temperatura máxima: "))
            prec = float(input("Precipitação: "))
            tab.append(((int(ano), int(mes), int(dia)), tmin, tmax, prec))
    elif op == "2":
        if len(tab) == 0:
            print("Tabela vazia.")
        else:
            for dia in tab:
                print(dia)
    elif op == "3":
            print(medias(tab))        
    elif op == "4":
            fnome = input("Nome do ficheiro: ")
            guardaTabMeteo(tab, fnome)
    elif op == "5":
            fnome = input("Nome do ficheiro: ")
            tab = carregaTabMeteo(fnome)
    elif op == "6":
        if len(tab) == 0:
            print("Tabela vazia.")
        else:
            print(minMin(tab))
    elif op == "7":
            print(amplTerm(tab))
    elif op == "8":
            print(maxChuva(tab))
    elif op == "9":
            p = float(input("Limite p: "))
            print(diasChuvosos(tab, p))
    elif op == "10":
            p = float(input("Limite p: "))
            print(maxPeriodoCalor(tab, p))
    elif op == "11":
            grafTabMeteo(tab)
    elif op== "0":
         print("Saiu da Aplicação")
    else:
        print("Opção inválida.")







