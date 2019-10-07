import numpy as np

import random

def Myr(Mayor):
    NumMyr = 0
    for i in Mayor:
        if i > NumMyr:
            NumMyr = i
    return NumMyr


ListTemp = np.zeros((3, 12))


for i in range(len(ListTemp)):
    for j in range(len(ListTemp[i])):
        if(i == 0):
            Departamento = "Santander"
        elif(i == 1):
            Departamento = "Guajira"

        elif(i == 2):
            Departamento = "Nariño"
        ListTemp[i][j] = (random.randrange(18, 30))


print(ListTemp)

Prom = 0
Prome = 0
Promed = 0

for i in range(3):
    for j in range(12):
        if (i == 0):
            Prom = Prom+ListTemp[i][j]
        elif (i == 1):
            Prome = Prome+ListTemp[i][j]
        elif (i == 2):
            Promed = Promed+ListTemp[i][j]

print(f"El Promedio de Santander: {Prom/12}")

print(f"El Promedio de La Guajira: {Prome/12}")

print(f"El Promedio de Nariño: {Promed/12}")

x = ((Prom/12)+(Prome/12)+(Promed/12))/3

print(f"El Promedio nacional es: {x}")



r = range(12)
MaxSant = Myr(ListTemp[0][[r]])
print(MaxSant)

MaxGua = Myr(ListTemp[1][[r]])
print(MaxGua)

MaxNari = Myr(ListTemp[2][[r]])

print(MaxNari)

l = (MaxSant+MaxGua+MaxNari)/3

print(f"El promedio de los 3 mayores es: {l}")