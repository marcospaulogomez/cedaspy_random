import random
print("---------------------------")
print("MAPA DE TURMA - MARÇO/ABRIL")
print("---------------------------")

prof1 = input("Qual o primeiro professor? ")
prof2 = input("Qual o segundo professor? ")
prof3 = input("Qual o terceiro professor? ")
prof4 = input("Qual o quarto professor? ")

professores = [prof1, prof2, prof3, prof4]

#módulos

pro = "Processadore de Textos"
exc = "Excel"
corel = "Ilustração Digital"
photo = "Design Digital"
games = "Games"
hard = "Montagem, Manutenção e Redes"
rob = "Robótica"
tcc = "TCC"

modulos = [pro, exc, corel, photo, games, hard, rob, tcc]

random.shuffle(professores)
random.shuffle(modulos)

print("Os professores irão lecionar os seguintes módulos em março e abril de 2023")
print("")
print("O(a) professor(a) {} lecionará {} e {}".format(professores[0], modulos[0], modulos[1]))
print("O(a) professor(a) {} lecionará {} e {}".format(professores[1], modulos[3], modulos[2]))
print("O(a) professor(a) {} lecionará {} e {}".format(professores[2], modulos[5], modulos[4]))
print("O(a) professor(a) {} lecionará {} e {}".format(professores[3], modulos[7], modulos[6]))