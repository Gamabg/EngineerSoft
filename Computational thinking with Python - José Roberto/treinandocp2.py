# def calculadora():
#     while True:
#         operacao = input("Digite a operação (+, -, *, /) ou 'sair' para encerrar: ")
#         if operacao.lower() == 'sair':
#             print("Encerrando a calculadora.")
#             break
#
#         try:
#             num1 = float(input("Digite o primeiro número: "))
#             num2 = float(input("Digite o segundo número: "))
#
#             if operacao == '+':
#                 resultado = num1 + num2
#             elif operacao == '-':
#                 resultado = num1 - num2
#             elif operacao == '*':
#                 resultado = num1 * num2
#             elif operacao == '/':
#                 resultado = num1 / num2
#
#             print("Resultado:", resultado)
#         except ValueError:
#             print("Entrada inválida. Use apenas números.")
# calculadora()
#

# def tabuada(numero, limite):
#     for i in range(1, limite + 1):
#         print(f"{numero} x {i} = {numero * i}")
# try:
#     numero = int(input("Digite o número para ver a tabuada: "))
#     limite = int(input("Digite até onde você quer a tabuada: "))
#     tabuada(numero, limite)


import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    print(numero_secreto)
    print("Tente adivinhar o número entre 1 e 100!")

    while True:

            chute = int(input("Seu palpite: "))

            if chute < numero_secreto:
                print("O número é maior!")
            elif chute > numero_secreto:
                print("O número é menor!")
            else:
                print(f"acertou.")
            if chute == numero_secreto:
                break
jogo_adivinhacao()

