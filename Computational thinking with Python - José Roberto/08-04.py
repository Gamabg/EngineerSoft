# ex1:

numero = int(input('Digite a sua nota: '))
if numero >= 1:
    print('positivo')
elif numero < 0:
    print('negativo')
else:
    print('zero')

# ex2:

nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
nota3 = int(input('Digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
print(media)

if media >= 7:
    print('aprovado')
else:
    print('reprovado')

# ex3:

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('deu certo')
else:
    print('deu errado')

# ex4:

tupla = (8, 10, 4)

maior = tupla[0]

if tupla[1] > maior:
    maior = tupla[1]

    if tupla[2] > maior:
        maior = tupla[2]
print(maior)

# ex5

numero = int(input('Digite um numero: '))

if numero > 10 and numero < 50:
    print('O numero esta entre o intervalo')
else:
    print('não esta dentro do intervalo')


lista = (6, 3, 4)

maior = lista[0]

if lista[1] > maior:
    maior = lista[1]

    if lista[2] > maior:
        maior = lista[2]

print(maior)

