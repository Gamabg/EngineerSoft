def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

n = int(input("Quantos números da sequência de Fibonacci você quer?"
              "Digite aqui: "))

print(f"Sequência de Fibonacci com {n} números:")
print(fibonacci(n))

def saudacao(nome):
    print(f"Olá, {nome}!")
# Chamando a função
saudacao("Maria")
saudacao("Lucas")

ola = "Ola, Lucas e Maria"
print(ola)

def saudacao():
    print("Olá alunos feiosos e noias!")
saudacao()


def calcularMedia(a, b):
    return(a + b)/2


nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota:'))
media = calcularMedia(a=nota1, b=nota2)
print(media)


def somar(a, b):
    return a + b

kwargs = {'a' : 3, 'b' : 5}
resultado = somar(**kwargs)

print(resultado)

def somar(a = 3, b = 5):
    return a + b

resultado = somar()

print(resultado)


def alteraA(a):
    a = a + 1
    print(a)
a = 2
alteraA(a)
print()

def alteraLista(lista):
    lista.append(2)
    lista.append(5)
    print(lista)

lista = [1, 7, 8, 3]
alteraLista(lista[:])
print(lista)


def somaTotal(*numeros):

    return sum(numeros)

print(somaTotal(1, 2, 3))
print(somaTotal(10, 20, 30, 40))
print(somaTotal())


def exibir_informacoes(**informacoes):

    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

exibir_informacoes(nome="ana", idade=25, cidade="sao paulo")
exibir_informacoes(produto="notebook", preco=2500.00, marca="dell ")