alunos = []


# Função para cadastrar aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    # Função para garantir que a nota seja válida (entre 0 e 10)
    def obter_nota(nota_num):
        while True:
            try:
                nota = float(input(f"Digite a {nota_num}ª nota: "))
                if 0 <= nota <= 10:
                    return nota
                else:
                    print("❌ A nota deve ser entre 0 e 10. Tente novamente.")
            except ValueError:
                print("❌ Por favor, insira um número válido para a nota.")

    nota1 = obter_nota(1)
    nota2 = obter_nota(2)
    nota3 = obter_nota(3)

    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": [nota1, nota2, nota3]
    }

    alunos.append(aluno)
    print(f"✅ Aluno {nome} cadastrado com sucesso!")


# Função para mostrar todos os alunos
def mostrar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n📋 Lista de Alunos:\n")
    for aluno in alunos:
        media = sum(aluno["notas"]) / 3
        situacao = "Aprovado" if media >= 7 else "Reprovado"
        notas_str = ", ".join(f"{n:.1f}" for n in aluno["notas"])
        print(
            f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Notas: {notas_str} | Média: {media:.2f} | Situação: {situacao}")


# Função para calcular as estatísticas
def mostrar_estatisticas():
    if not alunos:
        print("Nenhum aluno cadastrado para calcular as estatísticas.")
        return

    # 1. Média de idade dos alunos
    soma_idades = sum(aluno["idade"] for aluno in alunos)
    media_idade = soma_idades / len(alunos)

    # 2. Maior média de notas
    aluno_maior_media = max(alunos, key=lambda aluno: sum(aluno["notas"]) / 3)
    maior_media = sum(aluno_maior_media["notas"]) / 3

    # 3. Quantos alunos estão aprovados
    aprovados = sum(1 for aluno in alunos if sum(aluno["notas"]) / 3 >= 7)

    # Exibir resultados
    print(f"\n📊 Estatísticas:\n")
    print(f"Média de Idade dos Alunos: {media_idade:.2f}")
    print(f"Aluno com a maior média de notas: {aluno_maior_media['nome']} | Média: {maior_media:.2f}")
    print(f"Quantidade de alunos aprovados: {aprovados}")


# Menu com match-case
def menu():
    while True:
        print("\n1 - Cadastrar novo aluno")
        print("2 - Listar alunos cadastrados")
        print("3 - Ver estatísticas")
        print("4 - Sair do programa")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                cadastrar_aluno()
            case "2":
                mostrar_alunos()
            case "3":
                mostrar_estatisticas()
            case "4":
                print("Encerrando o sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")


# Iniciar o sistema
menu()
