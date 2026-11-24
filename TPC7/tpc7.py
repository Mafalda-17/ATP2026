# a) lista formada por elementos não comuns ás 2 listas

lista1= [1,2,3,4,5]
lista2= [4,5,6,7,8]
ncomuns= [x for x in lista1 if x not in lista2] + [x for x in lista2 if x not in lista1]

print(ncomuns)
