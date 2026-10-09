def selecionar_personagem(hpmax):
    if personagem == 'Cavaleiro':
        hpmax = 55
    elif personagem == 'Paladino':
        hpmax = 80
    elif personagem == 'Sacerdotisa':
        hpmax = 60
    elif personagem == 'Necromante':
        hpmax = 40
    elif personagem == 'Assassino':
        hpmax = 45
    elif personagem == 'Bruxa':
        hpmax = 50
    print(f'O(A) {personagem} é o(a) herói(na) lendário(a) escolhido(a)!')
    return hpmax

personagem = input()

matriz = []
for i in range(5):
    linha = input().split()
    matriz.append(linha)

direcoes = input()
passos = 0

i, j = 0, 0

def movimentar_personagem(i, j, passos, direcoes):
    if direcoes == '>':
        if j < 4:
            j += 1
            passos += 1

    elif direcoes == '<':
        if j > 0:
            j -= 1
            passos += 1

    elif direcoes == '^':
        if i > 0:
            i -= 1
            passos += 1

    elif direcoes == 'v':
        if i < 4:
            i += 1
            passos += 1
    return i, j, passos


def aplicar_efeito_sala(hpatual, hpmax):  #calcula o ganho e perda de HP do personagem
    pedra_magica = False
    efeito = matriz[i][j]
    if efeito == 'c':
        hpatual -= 15
    elif efeito == '+':
        hpatual += 20
        if hpatual > hpmax:
            hpatual = hpmax
    elif efeito == '@':
        hpatual -= 25
        if hpatual > 0:
            pedra_magica = True
    return hpatual, pedra_magica, hpmax

print('A jornada pela Pedra Mágica tem início! O destino do reino está selado, e esta guerra finalmente encontrará o seu fim.')
print()

hpmax= 0
hpmax = selecionar_personagem(hpmax)
hpatual = hpmax

mortes = 0
pedra_magica = False
terminou = False 

while terminou == False:
    pos = 0
    tentativa_acabou = False

    while pos < len(direcoes) and tentativa_acabou == False:
        comando = direcoes[pos]
        pos += 1
        passos_antes = passos
        i, j, passos = movimentar_personagem(i, j, passos, comando)

        if passos != passos_antes: #aplica efeito se realmente andou
            sala = matriz[i][j]
            hpatual, pedra_magica, hpmax = aplicar_efeito_sala(hpatual, hpmax)

            if sala == 'c' and hpatual > 0:
                print(f"O(A) {personagem} prevalece no combate, mantendo-se firme com {hpatual} HP!")

            if hpatual <= 0 or pedra_magica == True:
                tentativa_acabou = True

    if pedra_magica == True:
        print("A profecia se cumpriu e a paz reina mais uma vez!")
        print(f"Cruzando as profundezas da masmorra em {passos} passos de pura bravura, o(a) nosso(a) herói(na) ergue-se triunfante com {hpatual} HP.")
        terminou = True

    elif hpatual <= 0:
        mortes += 1
        if mortes == 1:
            print("Ainda não é o fim! A jornada continua…")
            print()
            personagem = input()
            direcoes = input()

            transposta = []
            for c in range(5):
                linha_nova = []
                for l in range(5):
                    linha_nova.append(matriz[l][c])
                transposta.append(linha_nova)
            matriz = transposta

            i, j, passos = 0, 0, 0
            hpmax = selecionar_personagem(hpmax)    
            hpatual = hpmax
        else:
            print("Sem heróis. Sem esperança. O Reino caiu.")
            terminou = True

    else:
        terminou = True
        