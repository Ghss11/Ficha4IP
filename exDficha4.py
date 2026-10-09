curingas_existentes = ['Joker', 'Space Joker', 'Blueprint', 'Chicot']
arcanos_existentes = ['Tolo', 'Hierofante', 'Justiça', 'Força']


def verificar_mao(mao):
    copia = mao.copy()
    copia.insert(0, 'x')

    erros = 0
    indices_erro = []

    for i in range(1, len(copia) // 2):
        if copia[i] < copia[2 * i]:
            indices_erro.append(2 * i)
            erros += 1
        if copia[i] < copia[2 * i + 1]:
            indices_erro.append(2 * i + 1)
            erros += 1

    mao_filtrada = []
    for i in range(1, len(copia)):
        if i not in indices_erro:
            mao_filtrada.append(copia[i])

    return mao_filtrada, erros


def aplicar_chicot(curingas, erros):
    for i in range(len(curingas)):
        if curingas[i] == 'Chicot':
            erros -= 2
        elif curingas[i] == 'Blueprint' and i + 1 < len(curingas) and curingas[i + 1] == 'Chicot':
            erros -= 2

    return erros


def calcular_base(erros):
    if erros <= 0:
        return 40, 4, 'Full House'
    elif erros == 1:
        return 30, 3, 'Três do mesmo'
    elif erros == 2:
        return 20, 2, 'Dois pares'
    else:
        return 5, 1, 'Carta Maior'


def aplicar_curingas(curingas, chips, multiplicador):
    for i in range(len(curingas)):
        curinga = curingas[i]

        if curinga == 'Blueprint' and i + 1 < len(curingas):
            curinga = curingas[i + 1]

        if curinga == 'Joker':
            multiplicador += 4
        elif curinga == 'Space Joker':
            chips += 20
            multiplicador += 1

    return chips, multiplicador


def aplicar_arcanos(mao, multiplicador, arcanos_ativos):
    if 'Hierofante' in arcanos_ativos:
        for i in range(len(mao)):
            if mao[i] < 30:
                mao[i] = mao[i] * 2

    if 'Justiça' in arcanos_ativos:
        for carta in mao:
            if carta % 3 == 0:
                multiplicador = multiplicador * 1.1

    if 'Força' in arcanos_ativos:
        for i in range(len(mao)):
            raiz = 0
            while raiz * raiz < mao[i]:
                raiz += 1
            if raiz * raiz == mao[i]:
                mao[i] += 50

    return mao, multiplicador


def calcular_pontuacao(chips_base, mao, multiplicador):
    chips_totais = chips_base + sum(mao)
    multiplicador = round(multiplicador, 2)
    pontuacao = int(chips_totais * multiplicador)

    return chips_totais, multiplicador, pontuacao


def rodada(curingas, arcanos, trocas):
    mao = eval(input())
    arcanos_ativos = []

    acao = input()
    while acao != 'Jogar':
        if acao == 'Trocar':
            if trocas > 0:
                mao = eval(input())
                trocas -= 1

        elif acao == 'Arcano':
            if len(arcanos) > 0:
                arcano = arcanos.pop(0)

                if arcano == 'Tolo':
                    novo_arcano = input()
                    arcanos.append(novo_arcano)
                elif arcano not in arcanos_ativos:
                    arcanos_ativos.append(arcano)

                print('Arcanos: ' + ', '.join(arcanos))

        acao = input()

    mao_filtrada, erros = verificar_mao(mao)

    erros = aplicar_chicot(curingas, erros)
    chips, multiplicador, classificacao = calcular_base(erros)
    print(f'Classificação da mão: {classificacao}')

    chips, multiplicador = aplicar_curingas(curingas, chips, multiplicador)
    mao_filtrada, multiplicador = aplicar_arcanos(mao_filtrada, multiplicador, arcanos_ativos)

    chips_totais, multiplicador, pontuacao = calcular_pontuacao(chips, mao_filtrada, multiplicador)
    print(f'{chips_totais} chips x {multiplicador} = {pontuacao}')

    return arcanos, trocas, pontuacao


meta = int(input())
print(f'Jimbo: Certo, você tem que conseguir {meta} chips. Boa sorte!')

inventario = eval(input())

curingas = []
arcanos = []
for item in inventario:
    if item in curingas_existentes:
        curingas.append(item)
    elif item in arcanos_existentes:
        arcanos.append(item)

print('Curingas: ' + ', '.join(curingas))
print('Arcanos: ' + ', '.join(arcanos))

total_chips = 0
jogadas = 0
trocas = 4

while jogadas < 4 and total_chips < meta:
    arcanos, trocas, pontuacao = rodada(curingas, arcanos, trocas)
    jogadas += 1
    total_chips += pontuacao
    print(f'Total de chips: {total_chips}')

if total_chips >= meta:
    print('Jimbo: Impressionante, você bateu a aposta.')
    if jogadas == 1:
        print('Jimbo: Balatro Balatrez esta a jugar balatro')
    elif jogadas == 4:
        print('Jimbo: Por pouco você falha, calculou bem.')
    else:
        print('Jimbo: Ainda bem que não apostei contra você.')
else:
    print(f'Jimbo: Mais que flop! Faltou {meta - total_chips} chips.')
