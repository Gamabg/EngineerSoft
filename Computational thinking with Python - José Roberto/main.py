#IF
 # def calcular_media(a, int):
 #     hhhhh
 #     if a == 1:
 #         aaaaa

#Exemplo
number = int(input('Digite um número: '))
if number > 6:
    print('maior que 6')

#IF Else
numero = int(input('Digite um numero:'))

if numero >= 6:
    print('aprovado')

else:
    print('Reprovado')


#Operador
print( 1 > 2 )
print( "a" > "b" )
print( 5 < 10 )
print (200 == 200 )

print(200 < 200.00001)


#Exemplo 1
nota = int(input('Digite sua nota: '))

if nota >= 0:
    print('aprovado')
else:
    print('reprovado')


#Exemplo 2

nota = int(input('Digite a sua nota: '))
if nota >= 6:
 print('aprovado')
elif nota >= 5.0:
 print('exame')
else:
 print('reprovado')

#Operadores logicos

a = True
b = False

if a and b :
    print(True)

else:
    print(False)