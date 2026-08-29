mystr = "Meu"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))

for letra in mystr:
    print(letra, end='')

Lista = ['Dark Side of the Moon', 'Animals', 'The Wall']
for album in Lista:
 print(album)
lista = list(range(0, 31))
for x in lista:
 print(x)

 s = 'the quick brown fox jumps over the lazy dog'
 if 'a' in s:
    print('contido')
 if '6' not in s:
    print('não está contido')

 for i in range(0, 30):
  if i == 10:
     break
 print(i)

 for m in range(0, 30):
        if i%2 != 0:
         continue
        print(m)

for i in range(0, 30):
    if i == 10:
        print('Encontrei')
        break
else:
    print('Não Encontrei')

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
c = ("Jessy", "Carlos", "Murilo")
Junto = zip(a, b, c)
print(list(Junto))
print(Junto)

names = ['John', 'Robert', 'Bruno', 'Murilo']
surnames = ['Smith', 'Gama', 'De Niro', 'de Lucas']
numbers = [69, 2, 3, 24]
for name, surname, number in zip(names,
surnames, numbers):
    print(name, surname, number)

L = [value ** 2 for value in range(1, 11)]
print(L)

pares = [i for i in range(0, 10) if i % 2 ==0]
print(pares)

# currentNumber = 0
# while currentNumber <= 10:
#     print(currentNumber)
# currentNumber += 1

while True:
    entrada = input('Digite algo: ')
    if entrada == 'quit':
        break
    else:
        print('O texto digitado foi: '+ entrada)
        break