#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time

sudoku=input("Entrez un sudoku : ")
#"1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..4......7..7...3.."

# Détermine si deux cases sont dans la même ligne, la même colonne ou le même bloc
conflit=lambda i,j:i%9==j%9 or i//9==j//9 or (i%9//3==j%9//3 and i//27==j//27)

# Fonction de résolution
def resoudre(s):
    try: i=s.index(".") # Si il y a un trou
    except ValueError: return s # Renvoie le sudoku (résolu) si il n'y a plus de trou
    conflits=[int(s[j]) for j in range(81) if conflit(i,j) and s[j]!="."]
    for n in range(1,10):
        if n not in conflits:
            r=resoudre(s[:i]+str(n)+s[i+1:])
            if r!=None: return r

# Affichage du résultat sous forme d'un tableau 9x9
sep="+-------+-------+-------+"
def afficher(sol):
    grid=""
    for a in range(3):
        grid+=sep+"\n"
        for b in range(3):
            for c in range(3):
                n=a*27+b*9+c*3
                grid+="| "+" ".join(sol[n:n+3])+" "
            grid+="|\n"
    print(grid+sep)

t1=time.time()
sol=resoudre(sudoku)
t2=time.time()
afficher(sol)
print("\nSudoku résolu en %.3f s" % (t2-t1))
