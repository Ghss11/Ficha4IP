# Recebe o nome e a intensidade e devolve os custos e o poder base
def calcular_requisitos(nome, intensidade):
    if nome == "LUA":
        custo_moli = intensidade
        custo_lotus = 1
        custo_cinzas = 0
        poder_base = 10 * intensidade
    elif nome == "SOMBRAS":
        custo_moli = 0
        custo_lotus = intensidade
        custo_cinzas = 2
        poder_base = 12 * intensidade
    else:  # FAMILIAR
        custo_moli = 1
        custo_lotus = 1
        custo_cinzas = intensidade
        poder_base = 15 * intensidade

    return custo_moli, custo_lotus, custo_cinzas, poder_base

# Verifica se tem ingredientes suficientes
def possui_ingredientes(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas):
    return moli >= custo_moli and lotus >= custo_lotus and cinzas >= custo_cinzas

# Conjura a magia, devolvendo o poder total e os ingredientes restantes
def conjurar_feitico(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas, poder_base, nome, feitico_anterior):

    # gasta os ingredientes
    moli -= custo_moli
    lotus -= custo_lotus   
    cinzas -= custo_cinzas

    # verificar sinergia
    bonus = 0
    if feitico_anterior != "" and feitico_anterior != nome:
        bonus = 5

    poder_obtido = poder_base + bonus
    return moli, lotus, cinzas, poder_obtido, bonus

# PROGRAMA PRINCIPAL
meta = int(input())
moli = int(input())
lotus = int(input())
cinzas = int(input())
quantidade_tentativas = int(input())

poder_total = 0
feitico_anterior = ""

for i in range(quantidade_tentativas):
    linha = input().split()          
    nome = linha[0]
    intensidade = int(linha[1])

    custo_moli, custo_lotus, custo_cinzas, poder_base = calcular_requisitos(nome, intensidade)

    if possui_ingredientes(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas) == True:
        moli, lotus, cinzas, poder_obtido, bonus = conjurar_feitico( moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas, poder_base, nome, feitico_anterior)

        poder_total = poder_total + poder_obtido

        print(f"Melinoë conjurou {nome} e obteve {poder_obtido} de poder.")

        if bonus > 0:
            print("Sinergia lunar ativada! Selene concedeu 5 de poder extra.")
            print("Hécate: A luz de Selene responde à sua feitiçaria. Faça-a valer.")
        elif feitico_anterior == "":
            print("Hécate: Foi para isto que treinamos todas essas noites, Melinoë.")
        else:
            print("Hécate: Disciplina, Melinoë. Uma bruxa vence antes mesmo de deixar a Encruzilhada.")

        print("Que assim seja!")

        feitico_anterior = nome   # só atualiza quando dá certo
    else:
        print(f"Ingredientes insuficientes para conjurar {nome}.")
        print("Hécate: Intenção sem preparo não basta. Reúna os ingredientes e tente outra vez.")

# RELATÓRIO
print(f"Poder acumulado: {poder_total}")
print(f"Ingredientes restantes: {moli} moli, {lotus} lotus e {cinzas} cinzas.")

if poder_total >= meta:
    print("Melinoë está pronta para enfrentar Cronos.")
    print("Hécate: Você está pronta para partir. Lembre-se do que aprendeu na Encruzilhada — e retorne para nós.")
else:
    print("Melinoë precisa se preparar melhor antes de enfrentar Cronos.")
    print("Hécate: Cronos não terá piedade de você. Eu tampouco terei durante seu treinamento.")
    