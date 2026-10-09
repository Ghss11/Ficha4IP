deuses_validos = ["AFRODITE", "ARES", "ARTEMIS", "ATENA", "DEMETER", "DIONISIO", "HERMES", "POSEIDON", "ZEUS"]


def receber_bencoes(deuses_obtidos, total_bencoes):
    deus = input()
    while deus != "PARAR":
        if deus == "COMBINADA":
            combinada_1 = input()
            combinada_2 = input()

            if combinada_1.upper() not in deuses_validos or combinada_2.upper() not in deuses_validos:
                print("Zagreu: Uma Bênção Combinada assim? Acho que você está brincando comigo.")
            elif combinada_1.upper() not in deuses_obtidos or combinada_2.upper() not in deuses_obtidos:
                print("Zagreu: Eu ainda não tenho nenhuma Bênção desse(a) Deus(a), não posso combiná-la")
            elif combinada_1.upper() == combinada_2.upper():
                print("Zagreu: Os dois Deuses precisam diferentes para realizar uma Bênção Combinada...")
            elif combinada_1.upper() == "HERMES" or combinada_2.upper() == "HERMES":
                print("Zagreu: Uma Bênção Combinada com Hermes? Acho que ele é competitivo demais pra cooperar com os outros.")
            else:
                print(f"Zagreu foi abençoado por uma Bênção Combinada de {combinada_1} e {combinada_2}.")
                total_bencoes += 1

        elif deus in deuses_validos:
            deuses_obtidos.append(deus)
            total_bencoes += 1
            print(f"Zagreu obteve uma Bênção de {deus}.")

        else:
            print(f"Zagreu: Ah, claro. A Bênção de {deus}. Como pude esquecer? Tenho certeza de que meu pai também deve ter esquecido de mencioná-lo(a)... Você está brincando comigo não é?.")

        deus = input()

    print()

    return deuses_obtidos, total_bencoes


def batalha_chefe(total_bencoes, minimo):
    if total_bencoes < minimo:
        print("Zagreu cai, derrotado mais uma vez. Seu corpo se desfaz, retornando ao lugar que conhece tão bem.")
        return False
    return True


def tartaro(deuses_obtidos, total_bencoes):
    prisioneiros = input().split(", ")

    for i in range(len(prisioneiros) - 1):
        for j in range(len(prisioneiros) - 1 - i):
            if prisioneiros[j] > prisioneiros[j + 1]:
                aux = prisioneiros[j]
                prisioneiros[j] = prisioneiros[j + 1]
                prisioneiros[j + 1] = aux

    print(f"Zagreu: Aqui está sua papelada: {', '.join(prisioneiros)}")
    print()

    deuses_obtidos, total_bencoes = receber_bencoes(deuses_obtidos, total_bencoes)

    venceu = batalha_chefe(total_bencoes, 3)

    return deuses_obtidos, total_bencoes, venceu


def asfodelo(deuses_obtidos, total_bencoes):
    matriz_a = []
    for i in range(3):
        linha = []
        for numero in input().split():
            linha.append(int(numero))
        matriz_a.append(linha)

    matriz_b = []
    for i in range(3):
        linha = []
        for numero in input().split():
            linha.append(int(numero))
        matriz_b.append(linha)

    matriz_resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    maior = matriz_resultado[0][0]
    linha_maior = 0
    coluna_maior = 0
    for i in range(3):
        for j in range(3):
            if matriz_resultado[i][j] > maior:
                maior = matriz_resultado[i][j]
                linha_maior = i
                coluna_maior = j

    print(f"Zagreu: devo lançar minha vara de pesca nesse ponto: ({linha_maior}, {coluna_maior})")
    print()

    deuses_obtidos, total_bencoes = receber_bencoes(deuses_obtidos, total_bencoes)

    venceu = batalha_chefe(total_bencoes, 6)

    return deuses_obtidos, total_bencoes, venceu


def elisio(deuses_obtidos, total_bencoes):
    legado_total = 0

    while legado_total < 200:
        heroi = input().split()
        nome = heroi[0]
        titulo = heroi[2]

        if nome.lower() == "hércules":
            legado = 50
        elif nome.lower() == "aquiles":
            legado = 40
        elif nome.lower() == "odisseu":
            legado = 35
        else:
            legado = 20

        if titulo.lower() == "imortal":
            legado = legado * 1.5
        elif titulo.lower() == "forte":
            legado = legado * 1.2
        elif titulo.lower() == "grande":
            legado += 15
        else:
            legado += 10

        print(f"O Herói: {nome} O {titulo} adicionou {legado} pontos de Legado.")
        legado_total += legado

    print("Zagreu: Acho que já fizemos história o suficiente por hoje.")
    print()

    deuses_obtidos, total_bencoes = receber_bencoes(deuses_obtidos, total_bencoes)

    venceu = batalha_chefe(total_bencoes, 9)

    return deuses_obtidos, total_bencoes, venceu


def templo_de_estige():
    print("O Templo de Estige... o último obstáculo entre você e a superfície.")
    print()

    vida_zagreu = 100
    vida_hades = 200
    ataques_hades = 0
    segunda_fase = False

    while vida_zagreu > 0 and vida_hades > 0:
        if (ataques_hades + 1) % 3 == 0:
            print("Zagreu: Meu pai parece estar carregando um forte ataque, é melhor desviar!")

        acao = input()
        esquivou = False

        if acao.upper() == "ATACAR":
            vida_hades -= 20
            print("Zagreu golpeia Hades, causando 20 de dano.")
        elif acao.upper() == "ATAQUE ESPECIAL":
            vida_hades -= 40
            print("Zagreu golpeia Hades com um ataque especial, causando 40 de dano.")
        elif acao.upper() == "ESQUIVA":
            esquivou = True
            print("Zagreu esquiva do ataque de Hades, evitando o dano.")

        if vida_hades <= 100 and vida_hades > 0 and not segunda_fase:
            segunda_fase = True
            print()
            print("Hades: Chega! Isso acaba agora!")
            print()

        if vida_hades > 0:
            ataques_hades += 1

            if segunda_fase:
                dano_normal = 25
                dano_forte = 100
            else:
                dano_normal = 15
                dano_forte = 50

            if ataques_hades % 3 == 0:
                dano = dano_forte
                ataque_forte = True
            else:
                dano = dano_normal
                ataque_forte = False

            if not esquivou:
                if ataque_forte:
                    print("Hades: Desapareça!")
                vida_zagreu -= dano
                print(f"Hades causou {dano} de dano em Zagreu.")

    print()

    if vida_hades <= 0:
        print("O senhor do Submundo cai diante de Zagreu. Pela primeira vez, não há nada entre ele e a superfície.")
        print("O portão se abre diante de você.")
        print("Zagreu finalmente deixa o Submundo para trás e sente o calor do sol tocar seu rosto. Pela primeira vez, a superfície está diante de seus olhos.")
        print("Você conseguiu escapar. A tentativa foi concluída.")
    else:
        print("Zagreu: Me desculpe, mãe. Foi tão perto...")


print("O portão se abre diante de você, revelando o caminho para o Submundo. Uma nova tentativa começa agora.")
print()

deuses_obtidos = []
total_bencoes = 0

deuses_obtidos, total_bencoes, venceu_tartaro = tartaro(deuses_obtidos, total_bencoes)

if venceu_tartaro:
    deuses_obtidos, total_bencoes, venceu_asfodelo = asfodelo(deuses_obtidos, total_bencoes)

    if venceu_asfodelo:
        deuses_obtidos, total_bencoes, venceu_elisio = elisio(deuses_obtidos, total_bencoes)

        if venceu_elisio:
            templo_de_estige()
