#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Un sudoku déclaré par certains « le plus dur du monde » (pour un humain)
#sudoku="100007090030020008009600500005300900010080002600004000300000010040000007007000300"
# Le sudoku qui est le plus compliqué à résoudre pour ce programme (voir README.md)
sudoku="000000012000000003002300400001800005060070800000009000008500000900040500470006000"

# Détermine si deux cases sont dans la même ligne, la même colonne ou le même bloc
conflit=lambda i,j:i%9==j%9 or i//9==j//9 or (i%9//3==j%9//3 and i//27==j//27)

# Fonction de résolution
def resoudre(s):
    try: i=s.index("0") # Si il y a un 0
    except ValueError: return s # Renvoie le sudoku (résolu) si il n'y a plus de 0
    conflits=[int(s[j]) for j in range(81) if conflit(i,j)]
    for n in range(1,10):
        if n not in conflits:
            r=resoudre(s[:i]+str(n)+s[i+1:])
            if r!=None: return r

# Affichage du résultat sous forme d'un tableau 9x9
sep=lambda:print("+---+---+---+")
def afficher(sol):
    sep()
    print("|"+sol[0:3]+"|"+sol[3:6]+"|"+sol[6:9]+"|")
    print("|"+sol[9:12]+"|"+sol[12:15]+"|"+sol[15:18]+"|")
    print("|"+sol[18:21]+"|"+sol[21:24]+"|"+sol[24:27]+"|")
    sep()
    print("|"+sol[27:30]+"|"+sol[30:33]+"|"+sol[33:36]+"|")
    print("|"+sol[36:39]+"|"+sol[39:42]+"|"+sol[42:45]+"|")
    print("|"+sol[45:48]+"|"+sol[48:51]+"|"+sol[51:54]+"|")
    sep()
    print("|"+sol[54:57]+"|"+sol[57:60]+"|"+sol[60:63]+"|")
    print("|"+sol[63:66]+"|"+sol[66:69]+"|"+sol[69:72]+"|")
    print("|"+sol[72:75]+"|"+sol[75:78]+"|"+sol[78:81]+"|")
    sep()

afficher(resoudre(sudoku))