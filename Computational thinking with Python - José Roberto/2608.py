numero = 10
lista = [1,7,8,9]

try:
    print(lista[2])
except Exception as e:
    print('Excessão Lançada: ', e)
else:
    print('Deu certo porra!')

#EXEMPLO 2

numero = 100
lista = [1]

try:
    print(lista[2])

except ZeroDivisionError as e:
    print("Não Posso Dividir por zero", e)

except Exception as e:
    print('Deu erro: ', e)

finally:
    print('Encerrando')


#Exempmlo 3

numero = 10
lista = (1)

class AlunosBurrosException (Exception):
    def __init__(self, mensagem="Os alunos são muito burros para executar esse programa!"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)


try:
    if True:
        raise AlunosBurrosException

except Exception as e:
    print('Deu erro: ', e)



#EXEMPLO 4
# import os
#
# directory_name = "my_new_directory"
# os.mkdir(directory_name)
#
# with open('exemplo.txt', 'w') as arquivo:
#
#     arquivo.write('Olá, este é um exemplo de escrita em arquivo.\n')
#     arquivo.write('Python é poderoso e versátil!\n')
#     arquivo.write('Fechando o arquivo automaticamente com o bloco "with".\n')

#
# with open ('example.txt', 'r') as arquivo:
#     for linha in arquivo:
#         print(linha.strip())


import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Isso é uma mensagem de depuração')
logging.info('Isso é uma mensagem informativa')
logging.warning('Isso é um alerta')
logging.error('Ocorreu um erro!')
logging.critical('Erro crítico! O sistema pode parar de funcionar.')
