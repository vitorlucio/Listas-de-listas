# coding: utf-8
import json

# Opening JSON file
with open('dados.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

alunos = json_object["alunos"]
notas = json_object["notas"]

def adicionar_nota():
    nome = input("Qual o nome do Aluno: ")
    nota = float(input("Qual a nota do Aluno: "))
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
    nota = int(input("Qual a nota do Aluno 1,2 ou 3? "))
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
        nova_nota = int(input("Qual a nota para adicionar? "))
        notas[posicao_aluno][nota - 1] = nova_nota
        print("Nota modificada")
        return

def buscar_aluno_por_nome():
    nome = input("Qual o nome de aluno que você deseja buscar:")
    contador = 0

    for nome_do_aluno in alunos:
        if nome_do_aluno.upper().startswith(nome.upper()):
            contador = contador + 1
            indice = alunos.index(nome_do_aluno)
            media = 0
            if len(notas[indice]) > 0:
                media = sum(notas[indice]) / 3
            print("%d. %s. Notas: %s. Média: %.2f" % (contador,nome_do_aluno, ', '.join(map(str, notas[indice])),media))
            #' , ' para separar a lista de notas com virgula / .join para juntar os itens da lista e map para transformar de inteiro para str

def calcular_media_da_turma():
    total_notas = []
    for nota in notas:
        if len(nota) > 0:
            total_notas.append(sum(nota)/3)
        else:
            total_notas.append[0]
    media = sum(total_notas) / len(notas)
    print("A média da turma é: %.2f" % (media))

def exibir_melhor_aluno():
    melhor_media = 0
    index = 0
    contador = 0
    for nota in notas:
       media = 0
       if len(nota) > 0:
          media = sum(nota) / 3
       if media > melhor_media:
           melhor_media = media
           index = contador

       contador = contador + 1
    print("%d. %s. Notas: %s. Média: %.2f" % (1, alunos[index], ', '.join(map(str, notas[index])), melhor_media))

def exibir_alunos_em_ordem_afabetica(alunos, notas):

    zipped_lists = zip(alunos, notas)
    sorted_pairs = sorted(zipped_lists)

    tuples = zip(*sorted_pairs)
    alunos, notas = [list(tuple) for tuple in tuples]
    for i in range(len(alunos)):
        media = 0
        if len(notas[i]) > 0:
            media = sum(notas[i]) / 3
        print("%d. %s. Notas: %s. Média: %.2f" % (i+1, alunos[i], ', '.join(map(str, notas[i])), media))


def exibir_alunos_ordenados_por_nota():
    alunos_por_media, notas_por_media = insertion_sort(alunos,notas)
    for i in range(len(notas_por_media)):
        media = 0
        if len(notas_por_media[i]) > 0:
            media = sum(notas_por_media[i]) / 3
        print("%d. %s. Notas: %s. Média: %.2f" % (i+1, alunos_por_media[i], ', '.join(map(str, notas_por_media[i])), media))

def exibir_aluno_aprovados_por_media():
    verifica_media_alunos(7,10.1)

def exibir_alunos_na_final():
    verifica_media_alunos(5,7)

def exibir_alunos_reprovados():
    verifica_media_alunos(0,5)

def verifica_media_alunos(x, y):
    index = 0
    contador = 0
    for nota in notas:

        media = 0
        if len(nota) > 0:
            media = sum(nota) / 3
        if media >= x and media < y:
            contador = contador + 1
            print("%d. %s. Notas: %s. Média: %.2f" % (contador, alunos[index], ', '.join(map(str, notas[index])), media))
        index = index + 1

def insertion_sort(alunos,notas):
    pos = 0
    while pos < len(alunos):
        pos2 = pos
        if pos2 > 0:
            media_aluno_1 = sum(notas[pos2]) / 3
            media_aluno_2 = sum(notas[pos2 - 1]) / 3
        while pos2 > 0 and media_aluno_1 > media_aluno_2:
            aux = alunos[pos2]
            alunos[pos2] = alunos[pos2 - 1]
            alunos[pos2 - 1] = aux
            aux = notas[pos2]
            notas[pos2] = notas[pos2 - 1]
            notas[pos2 - 1] = aux
            pos2 -= 1
            media_aluno_1 = 0
            media_aluno_2 = 0
            if len(notas[pos2]) > 0:
                media_aluno_1 = sum(notas[pos2]) / 3
            if len(notas[pos2 - 1]) > 0:
                media_aluno_2 = sum(notas[pos2 - 1]) / 3
        pos += 1
    return(alunos,notas)


def salvar_dados():
    dictionary = {
        "alunos": alunos,
        "notas": notas
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("dados.json", "w") as outfile:
        outfile.write(json_object)


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
            print("Aluno adicionado com sucesso!")
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
        exibir_alunos_em_ordem_afabetica(alunos, notas)
        #ok
    elif opcao == 11:
        exibir_alunos_ordenados_por_nota()
        #ok
    elif opcao == 12:
        exibir_aluno_aprovados_por_media()
        #ok
    elif opcao == 13:
        exibir_alunos_na_final()
        #ok
    else:
        exibir_alunos_reprovados()
        #ok
    salvar_dados()












