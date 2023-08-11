import random


def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        #print(f"{i+1}Âº passo")
        #print(matriz)
        for j in range(colunas):
            matriz[i].append(",")
    return matriz

def printa_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def velha(matriz,rodadas):

    return




mapa=cria_matriz(3,3)

printa_matriz(mapa)
win=False
rodada=0

while True:

    if rodada%2==0:
        coluna = int(input("diga a coluna que deseja colocar sua marcação"))
        linha = int(input("diga a linha que deseja colocar sua marcação"))
        mapa[coluna][linha]="O"
    else:
        prioridade = []
        # quinas e centro
        if rodada == 1:
            if mapa[0][0] != "O":
                prioridade.append((0, 0))
            if mapa[0][2] != "0":
                prioridade.append((0, 2))
            if mapa[1][1] != "0":
                prioridade.append((1, 1))
            if mapa[2][0] != "0":
                prioridade.append((2, 0))
            if mapa[2][2] != "0":
                prioridade.append((2, 2))

            escolha_aleatoria = random.choice(prioridade)
            mapa[escolha_aleatoria[0]][escolha_aleatoria[1]] = "X"

        else:
            for i in range(len(mapa)):
                for j in range(len(mapa)):
                 #defesa
                    if mapa[i][j]=="O" and mapa[i][j+1]=="O":
                        mapa[i][j+2]="X"
                    elif mapa[i][j]=="O" and mapa[i+1][j]=="O":
                        mapa[i+2][j]="X"
                    elif mapa[i][i]=="O" and mapa[i+1][i+1]=="O":
                        mapa[i+2][i+2]="X"

        print("Jogada da velha")

    printa_matriz(mapa)
    if rodada>=4:
        for i in range(len(mapa)):
            j=0
            print(map)
            if mapa[i][j] == mapa[i][j+1] == mapa[i][j+2]:
                if rodada%2==0:
                    print("Jogador O ganhou")
                    win=True
                else:
                    print("jogador X ganhou")
                    win=True
        i=0
        j=0
        for j in range(len(mapa)):
             if mapa[i][j] == mapa[i+1][j] == mapa[i+2][j]:
                if rodada%2==0:
                    print("Jogador O ganhou")
                    win=True
                else:
                    print("jogador X ganhou")
                    win=True
        if mapa[i][i]== mapa[i+1][i+1]==mapa[i+2][i+2]:
            if rodada % 2 == 0:
                print("Jogador O ganhou")
                win = True
            else:
                print("jogador X ganhou")
                win = True
        elif mapa[i][i+2]==mapa[i+1][i+1]==mapa[i+2][i]:
            if rodada % 2 == 0:
                print("Jogador O ganhou")
                win = True
            else:
                print("jogador X ganhou")
                win = True



    rodada+=1

    if win==True:
        break