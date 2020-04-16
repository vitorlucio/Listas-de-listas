alunos = []
notas = []

while True :
    opcao = int(input('O que você deseja fazer: \n\t1) Adicionar Aluno\n\t2) Adicionar Nota\n\t3) Remover Aluno\n\t4) Remover Nota\n\t5) Editar Nome do Aluno\n\t6) Editar Nota do Aluno\n\t7) Buscar Aluno Por Nome\n\t8) Calcular Média da Turma\n\t9) Exibir Melhor Aluno\n\t10) Exibir Alunos Em Ordem Afabética\n\t11) Exibir Aluno Por Ordenados Por Nota\n\t12) Exibir Aluno Aprovados Por Média (>=7)\n\t13) Exibir Alunos Na Final (>=5)\n\t14) Exibir Alunos Reprovados (<5)\n\t15) Encerrar o Programa\n Digite a Sua Opção :'))
    if opcao == 15:
        print("Bye.")
        break
    elif opcao == 1:
        nome = input("Adicione o nome do Aluno: ")
        if nome in alunos:
            print("Aluno já existe")
        else:
            alunos.append(nome)
            notas.append([])
    elif opcao == 2:
        nome_do_aluno = input("Qual o nome do Aluno: ")
        nota_do_aluno = input("Qual a nota do Aluno: ")
        if nome_do_aluno not in nota_do_aluno:
            print("Aluno não existe.")
        posicao_aluno = alunos.index(nome_do_aluno)
        nota_do_aluno = notas[posicao_aluno]
        if len(nota_do_aluno)







