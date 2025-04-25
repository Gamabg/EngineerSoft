alunos = []

# Menu com match-case
while True:
    print("\n1 - Cadastrar novo aluno")
    print("2 - Listar alunos cadastrados")
    print("3 - Ver estatísticas")
    print("4 - Sair do programa")
    
    opcao = input("Escolha uma opção: ")

    # Usando match-case para as opções do menu
    match opcao:
        case "1":
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            
            # Coletando as 3 notas
            while True:
                try:
                    nota1 = float(input("Digite a 1ª nota: "))
                    if 0 <= nota1 <= 10:
                        break
                    else:
                        print("❌ A nota deve ser entre 0 e 10.")
                except ValueError:
                    print("❌ Por favor, insira um número válido.")
            
            while True:
                try:
                    nota2 = float(input("Digite a 2ª nota: "))
                    if 0 <= nota2 <= 10:
                        break
                    else:
                        print("❌ A nota deve ser entre 0 e 10.")
                except ValueError:
                    print("❌ Por favor, insira um número válido.")
            
            while True:
                try:
                    nota3 = float(input("Digite a 3ª nota: "))
                    if 0 <= nota3 <= 10:
                        break
                    else:
                        print("❌ A nota deve ser entre 0 e 10.")
                except ValueError:
                    print("❌ Por favor, insira um número válido.")
            
            # Criando o dicionário do aluno e adicionando na lista
            aluno = {
                "nome": nome,
                "idade": idade,
                "notas": [nota1, nota2, nota3]
            }
            alunos.append(aluno)
            print(f"✅ Aluno {nome} cadastrado com sucesso!")

        case "2":
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado.")
            else:
                print("\n📋 Lista de Alunos:")
                for aluno in alunos:
                    media = sum(aluno["notas"]) / 3
                    situacao = "Aprovado" if media >= 7 else "Reprovado"
                    notas_str = ", ".join([str(nota) for nota in aluno["notas"]])
                    print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Notas: {notas_str} | Média: {media:.2f} | Situação: {situacao}")

        case "3":
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado para calcular as estatísticas.")
            else:
                # Calculando a média de idade
                soma_idades = 0
                maior_media = 0
                aluno_maior_media = None
                aprovados = 0
                
                for aluno in alunos:
                    soma_idades += aluno["idade"]
                    media = sum(aluno["notas"]) / 3
                    if media > maior_media:
                        maior_media = media
                        aluno_maior_media = aluno
                    if media >= 7:
                        aprovados += 1
                
                media_idade = soma_idades / len(alunos)

                # Exibindo estatísticas
                print("\n📊 Estatísticas:")
                print(f"Média de Idade dos Alunos: {media_idade:.2f}")
                print(f"Aluno com a maior média de notas: {aluno_maior_media['nome']} | Média: {maior_media:.2f}")
                print(f"Quantidade de alunos aprovados: {aprovados}")

        case "4":
            print("Encerrando o sistema...")
            break

        case _:
            print("Opção inválida. Tente novamente.")
