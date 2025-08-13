alunos =[ 
        {"Nome": "Murilo", "Sexualidade": "Nao Binario Pan"},
        {"Nome": "Kauai", "Sexualidade": "Homossexual"}
]
aluno = alunos[0]

print(aluno["Nome"]), print(aluno["Sexualidade"])



# numeros = [[2,7,8], 
#         [1,3,3,3],
#     [2,3,4,5]]

# matriz = []
# m = 10
# n = 10

# for i in range(m):
#     matriz.append([]) 
#     for j in range(n):
#         matriz[i].append(0)   
        
# for linha in matriz:
#     # print(linha)       

import numpy as np


def matriz_zeros(m, n):
    matriz = []
    
    for i in range(m):
        linha = []
        for j in range(n):
            if i + j == n - 1:  
                linha.append(1)  
            else:
                linha.append(0)
                
        matriz.append(linha)

    return matriz

matriz = matriz_zeros(10, 10)

for linha in matriz:
    print(linha)



