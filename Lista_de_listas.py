alunos = ["vitor","ana","lucas","vitinho"]
notas = [[7,8,9],[10,9,8],[7,5,6],[8,9,8]]
def adicionar_nota():
    nome = input("Qual o nome do Aluno: ")
    nota = input("Qual a nota do Aluno: ")
    if nome not in alunos:
        print("Aluno não existe.")
        return
    posicao_aluno = alunos.index(nome)
    nota_do_aluno = notas[posicao_aluno]
    if len(nota_do_aluno) >= 3:
        print("Este aluno ja contem as 03 notas")
        return
    nota_do_aluno.append(nota)
    notas[posicao_aluno] = nota_do_aluno
    print("Nota adicionada com sucesso")

def remover_aluno():
    nome = input("Qual o nome do Aluno para remover: ")
    if nome not in alunos:
        print("Aluno não existe.")
        return
    posicao_aluno = alunos.index(nome)
    alunos.pop(posicao_aluno)
    notas.pop(posicao_aluno)
    print("Aluno removido")

def remover_nota():
    nome = input("Qual o nome do Aluno: ")
    nota = int(input("Qual a nota do Aluno: "))
    if nome not in alunos:
        print("Aluno não existe.")
        return
    posicao_aluno = alunos.index(nome)
    if len(notas[posicao_aluno]) >= (nota):
        notas[posicao_aluno].pop(nota - 1)
        print("Nota Removida.")

def editar_nome_do_aluno():
    nome = input("Qual o nome do aluno para editar: ")
    novo_nome = input("Qual novo nome para adicionar:")
    if nome not in alunos:
        print("Aluno não existe.")
        return
    posicao_aluno = alunos.index(nome)
    alunos[posicao_aluno] = novo_nome
    print("Nome do Aluno modificado")

def editar_nota_do_aluno():
    nome = input("Qual o nome do aluno para editar: ")
    if nome not in alunos:
        print("Aluno não existe.")
        return
    nota = int(input("Qual a nota para editar 1, 2 ou 3?:"))

    posicao_aluno = alunos.index(nome)
    nota_do_aluno = notas[posicao_aluno]
    if len(nota_do_aluno) >= nota:
        nova_nota = input("Qual a nota para adicionar? ")
        notas[posicao_aluno][nota - 1] = nova_nota
        return

def buscar_aluno_por_nome():
    nome = input("Qual o nome de aluno que você deseja buscar:")
    contador = 0

    for nome_do_aluno in alunos:
        if nome_do_aluno.upper().startswith(nome.upper()):
            contador = contador + 1
            indice = alunos.index(nome_do_aluno)
            media = sum(notas[indice]) / 3
            print("%d. %s. Notas: %s. Média: %.2f" % (contador,nome_do_aluno, ', '.join(map(str, notas[indice])),media))
            #' , ' para separar a lista de notas com virgula / .join para juntar os itens da lista e map para transformar de inteiro para str

def calcular_media_da_turma():
    total_notas = []
    for nota in notas:
        total_notas.append(sum(nota)/3)
    media = sum(total_notas) / len(notas)
    print("A média da turma é: %.2f" % (media))

def exibir_melhor_aluno():
    melhor_media = 0
    index = 0
    contador = 0
    for nota in notas:
       media = sum(nota) / len(nota)
       if media > melhor_media:
           melhor_media = media
           index = contador

       contador = contador + 1
    print("%s. Notas: %s. Média: %.2f" % (alunos[index], ', '.join(map(str, notas[index])), melhor_media))

def exibir_alunos_em_ordem_afabetica():
    alunos.sort()












while True :
    opcao = int(input('O que você deseja fazer: \n\t1) Adicionar Aluno\n\t2) Adicionar Nota\n\t3) Remover Aluno\n\t4) Remover Nota\n\t5) Editar Nome do Aluno\n\t6) Editar Nota do Aluno\n\t7) Buscar Aluno Por Nome\n\t8) Calcular Média da Turma\n\t9) Exibir Melhor Aluno\n\t10) Exibir Alunos Em Ordem Afabética\n\t11) Exibir Alunos Ordenados Por Nota\n\t12) Exibir Aluno Aprovados Por Média (>=7)\n\t13) Exibir Alunos Na Final (>=5)\n\t14) Exibir Alunos Reprovados (<5)\n\t15) Encerrar o Programa\n Digite a Sua Opção :'))
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
        adicionar_nota()
    elif opcao == 3:
        remover_aluno()
    elif opcao == 4:
        remover_nota()
    elif opcao == 5:
        editar_nome_do_aluno()
    elif opcao == 6:
        editar_nota_do_aluno()
    elif opcao == 7:
        buscar_aluno_por_nome()
        #ok
    elif opcao == 8:
        calcular_media_da_turma()
        #ok
    elif opcao == 9:
        exibir_melhor_aluno()
        #ok
    elif opcao == 10:
        exibir_alunos_em_ordem_afabetica()
    elif opcao == 11:
        exibir_alunos_ordenados_por_nota()
    elif opcao == 12:
        exibir_aluno_aprovados_por_media()
    elif opcao == 13:
        exibir_alunos_na_final()
    else:
        exibir_alunos_reprovados()












