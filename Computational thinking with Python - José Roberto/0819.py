# #EXC1

# matriz = [
#         [1,3,5],  
#         [2,2,2],
#         [3,3,3]
# ]
# def somar_matriz(matriz):   
#     soma = 0
#     for linha in matriz:
#         for elemento in linha:
#             soma += elemento
    
#     return soma
# resposta = somar_matriz(matriz)
# print(resposta)   

# #EXC2

# import random

# matriz = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
# print("Matriz:")
# for linha in matriz:
#     print(linha)

# diagonal = [matriz[i][i] 
#         for i in range(3)]

# print("\nDiagonal principal:", diagonal)

# #EXC3

# import random

# matriz = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
# print("Matriz:")
# for linha in matriz:
#     print(linha)

# diagonal = [matriz[i][2-i] 
#         for i in range(3)]

# print("\nDiagonal Segundaria:", diagonal)

#EXC4

# import random

# matriz - [[rando.randint(1,9) for m in range(3) for n in range(3)]]
# print("matriz:")

# for j in range(m):
#     j.append

# print(matriz)

# def trans_matriz(matriz):
#     linha = []
#     for i in range(matriz):


#KAZYS mode 

import random.randint




#METODO 1

import random.randint

m = int(input("Digite o numero de linhas da matriz"))
n = int(input("Digite o numero de Colunas da Matriz"))

matriz = [
    [],
    [],
    []
]

#METODO 2 

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposta = [list(i) for i in zip(*matriz)]

print("Matriz Original:")
for linha in matriz:
    print(linha)

print("\nMatriz Transposta:")
for linha in transposta:
    print(linha)


#METODO 3 

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

linhas = len(matriz)
colunas = len(matriz[0])

transposta = []

for j in range(colunas): 
    nova_linha = []
    for i in range(linhas):
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha) 

print("Matriz Original:")
for linha in matriz:
    print(linha)

print("\nMatriz Transposta:")
for linha in transposta:
    print(linha)