




def clean_board():
    return [
     [8, 9, 10, 11, 12, 10, 9, 8],
     [7, 7, 7, 7, 7, 7, 7, 7],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1],
     [2, 3, 4, 5, 6, 4, 3, 2],
     ]


def affiche(g):
    for i in range(8):
        for j in range(8):
            if g[7-i][j]==0:
                print(" 0","",end="")
            elif g[7-i][j]==1:
                print(" 1","",end="")
            elif g[7-i][j]==2:
                print(" 2","",end="")
            elif g[7-i][j]==3:
                print(" 3","",end="")
            elif g[7-i][j]==4:
                print(" 4","",end="")
            elif g[7-i][j]==5:
                print(" 5","",end="")
            elif g[7-i][j]==6:
                print(" 6","",end="")
            elif g[7-i][j]==7:
                print(" 7","",end="")
            elif g[7-i][j]==8:
                print(" 8","",end="")
            elif g[7-i][j]==9:
                print(" 9","",end="")
            elif g[7-i][j]==10:
                print("10","",end="")
            elif g[7-i][j]==11:
                print("11","",end="")
            elif g[7-i][j]==12:
                print("12","",end="")
        print()
    print()
    

g = clean_board()
affiche(g)


'''

0 --> case vide

1 --> pion blanc
2 --> tour blanc
3 --> cavalier blanc
4 --> fou blanc
5 --> dame blanc
6 --> roi blanc

7 --> pion noir
8 --> tour noir
9 --> cavalier noir
10 --> fou noir
11--> dame noir
12 --> roi noir


- mouvement de chaque pièce
- vérifier si échec
- possibilité de jouer
    - coup impossible (car échec)
        - (grand) roque
- déplacement
    - manger les pions


- pat
(- répétition 3 fois)





'''