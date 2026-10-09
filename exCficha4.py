def montar_baralho(baralho):
    canideos = []
    insetos = []
    aves = []
    cervideos = []
    repteis = []

    carta_nova = input()
    n_novas = 0
    while carta_nova.lower() != "fim":
        baralho.append(carta_nova)
        n_novas += 1
        carta_nova = input()

    for carta in baralho:
        if "lobo" in carta.lower() or "coiote" in carta.lower() or "cachorro" in carta.lower():
            canideos.append(carta)

    for carta in baralho:
        if "formiga" in carta.lower() or "abelha" in carta.lower() or "louva-a-deus" in carta.lower():
            insetos.append(carta)

    for carta in baralho:
        if "corvo" in carta.lower() or "urubu" in carta.lower() or "pardal" in carta.lower():
            aves.append(carta)

    for carta in baralho:
        if "caribu" in carta.lower() or "antilocapra" in carta.lower() or "alce" in carta.lower():
            cervideos.append(carta)

    for carta in baralho:
        if "rã" in carta.lower() or "tartaruga" in carta.lower() or "víbora" in carta.lower():
            repteis.append(carta)

    print(f"{n_novas} cartas foram adicionadas ao baralho")

    return canideos, insetos, aves, cervideos, repteis

def receber_item(classe_totem):
    itens_inventario = []
    pontos_itens = 0
    classe_totem = ""

    item = input()
    while item.lower() != "fim":
        if item.lower() == "totem":
            classe_totem = input()
            classe_totem = classe_totem.capitalize()
            print(f"Totem ativo: {classe_totem}")
        else:
            pontos_itens += len(item.replace(" ", ""))
            if len(itens_inventario) < 3:
                itens_inventario.append(item)
            else:
                print("Inventario cheio")
        item = input()

    print(f"Itens no inventario: {', '.join(itens_inventario)}")

    return itens_inventario, pontos_itens, classe_totem

cartas_raras = ["urayuli", "louva-a-deus rei", "ameba", "tubarão", "urso"]

baralho = []

def coeficiente_total(baralho, pontos_itens, classe_totem, canideos, insetos, aves, cervideos, repteis):
    total = 0

    classe_totem_minuscula = classe_totem.lower()

    if classe_totem_minuscula == "canideos":
        lista_da_classe_do_totem = canideos
    elif classe_totem_minuscula == "insetos":
        lista_da_classe_do_totem = insetos
    elif classe_totem_minuscula == "aves":
        lista_da_classe_do_totem = aves
    elif classe_totem_minuscula == "cervideos":
        lista_da_classe_do_totem = cervideos
    elif classe_totem_minuscula == "repteis":
        lista_da_classe_do_totem = repteis
    else:
        lista_da_classe_do_totem = []

    for carta in baralho:
        if "pele" in carta.lower():
            coeficiente_carta = 0
        elif "filhote de" in carta.lower() or "ovo de" in carta.lower():
            coeficiente_carta = 5
        elif carta.lower() in cartas_raras:
            coeficiente_carta = 20
        else:
            coeficiente_carta = 10

        if carta in lista_da_classe_do_totem:
            coeficiente_carta = coeficiente_carta * 2

        total += coeficiente_carta

    total += pontos_itens

    return total

def batalha_garimpeiro(total):
    coeficiente_garimpeiro = 40
    total_ajustado = total // 2

    print("Garimpeiro - É o Garimpeiro! OPA!")

    if total_ajustado > coeficiente_garimpeiro:
        print("Garimpeiro - Oxe!")
        return True
    elif total_ajustado == coeficiente_garimpeiro:
        print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
        return False
    else:
        print("Garimpeiro - Mais ouro pra mim!")
        return False


def batalha_pescador(total, baralho):
    media = total // len(baralho)
    coeficiente_pescador = 90 + media

    print("Pescador - Eu sou o Pescador. Quer pescar?")

    if total > coeficiente_pescador:
        print("Pescador - Vai pescar...")
        return True
    elif total == coeficiente_pescador:
        print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
        return False
    else:
        print("Pescador - Hum. Vai pescar.")
        return False


def batalha_comerciante(total, baralho):
    coeficiente_comerciante = 160
    total_ajustado = total

    for carta in baralho:
        if "pele" in carta.lower():
            coeficiente_comerciante -= 10
            total_ajustado += 10

    print("Comerciante - Vamos negociar.")

    if total_ajustado > coeficiente_comerciante:
        print("Comerciante - Hmm... muito bem.")
        return True
    elif total_ajustado == coeficiente_comerciante:
        print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
        return False
    else:
        print("Comerciante - Você vai virar uma pele deslumbrante.")
        return False


print("Leshy - Outro desafiante. Já faz tanto tempo...")

baralho = []
classe_totem = ""

# Fase 1
print("Leshy - O sol banha os abetos sonolentos, você adentrou o... matagal.")

canideos, insetos, aves, cervideos, repteis = montar_baralho(baralho)

itens, pontos_itens, classe_totem = receber_item(classe_totem)

total = coeficiente_total(baralho, pontos_itens, classe_totem, canideos, insetos, aves, cervideos, repteis)

venceu_fase1 = batalha_garimpeiro(total)

if venceu_fase1:
    # Fase 2
    print("Leshy - O ar úmido é tomado pelo cheiro fétido de mofo e morte, você caminha cautelosamente até entrar na... charneca.")
    
    canideos, insetos, aves, cervideos, repteis = montar_baralho(baralho)

    itens, pontos_itens, classe_totem = receber_item(classe_totem)

    total = coeficiente_total(baralho, pontos_itens, classe_totem, canideos, insetos, aves, cervideos, repteis)

    venceu_fase2 = batalha_pescador(total, baralho)

    if venceu_fase2:
        # Fase 3
        print("Leshy - O alívio do ar fresco logo dá lugar a um arrepio álgido. Você escala até a... linha de neve.")

        canideos, insetos, aves, cervideos, repteis = montar_baralho(baralho)

        itens, pontos_itens, classe_totem = receber_item(classe_totem)

        total = coeficiente_total(baralho, pontos_itens, classe_totem, canideos, insetos, aves, cervideos, repteis)

        venceu_fase3 = batalha_comerciante(total, baralho)

        if venceu_fase3:
            print("Leshy - A luz cálida da cabana atravessa o denso nevoeiro... seus infortúnios acabam aqui.")