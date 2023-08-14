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

        print("jogada da velha")
        prioridade = []
        # quinas e centro
        if rodada == 1:
            if mapa[0][0] == ",":
                prioridade.append((0, 0))
            if mapa[0][2] == ",":
                prioridade.append((0, 2))
            if mapa[1][1] == ",":
                prioridade.append((1, 1))
            if mapa[2][0] == ",":
                prioridade.append((2, 0))
            if mapa[2][2] == ",":
                 prioridade.append((2, 2))

            escolha_aleatoria = random.choice(prioridade)
            mapa[escolha_aleatoria[0]][escolha_aleatoria[1]] = "X"


        else:

             # defesa
            if mapa[0][0]=="O" and mapa[0][2]=="O":
                mapa[0][1]="X"


            elif mapa[1][0]=="O" and mapa[1][2]=="O":
                mapa[1][1]="X"


            elif mapa[2][0]=="O" and mapa[2][2]=="O":
                 mapa[2][1]="X"


            elif mapa[0][2]=="O" and mapa[2][0]=="O":
                mapa[1][1]="X"


            elif mapa[0][2]=="O" and mapa[1][1]=="O":
                mapa[2][0]="X"


            for i in range(len(mapa)):
                for j in range(len(mapa)):
                    if mapa[i][j] == "O" and mapa[i][(j + 1) % 3] == "O" and mapa[i][(j + 2) % 3] == ",":
                        mapa[i][(j + 2) % 3] = "X"


                    elif mapa[j][i] == "O" and mapa[(j + 1) % 3][i] == "O" and mapa[(j + 2) % 3][i] == ",":
                        mapa[(j + 2) % 3][i] = "X"


                    elif mapa[i][i] == "O" and mapa[(i + 1) % 3][(i + 1) % 3] == "O" and mapa[(i + 2) % 3][(i + 2) % 3] == ",":
                        mapa[(i + 2) % 3][(i + 2) % 3] = "X"


            else:
                # jogada ofensiva
                for i in range(len(mapa)):
                    for j in range(len(mapa)):
                        if mapa[i][j] == "X" and mapa[i][(j + 1) % 3] == "X" and mapa[i][(j + 2) % 3] == ",":
                            mapa[i][(j + 2) % 3] = "X"

                        elif mapa[i][(j + 2) % 3] == "X" and mapa[i][(j + 1) % 3] == "X" and mapa[i][j] == ",":
                            mapa[i][j] = "X"

                        elif mapa[i][j] == "X" and mapa[(i + 1) % 3][j] == "X" and mapa[2][j] == ",":
                            mapa[2][j] = "X"


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