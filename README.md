# Résolution du sudoku
Ce programme utilise une méthode de balayage « lourde ».

Les *inputs* se font en mettant tous les chiffres sur une seule ligne (de gauche à droite, de bas en haut) et en remplaçant tous les blancs par des zéros.


```
Entrée :
.......12........3..23..4....18....5.6..7.8.......9.....85.....9...4.5..47...6...
qui correspond au sudoku ci-dessous :

+-----------------------+
|       |       |   1 2 |  
|       |       |     3 |
|     2 | 3     | 4     |
|-------+-------+-------|
|     1 | 8     |     5 | 
|   6   |   7   | 8     |
|       |     9 |       |
|-------+-------+-------|
|     8 | 5     |       |   
| 9     |   4   | 5     |
| 4 7   |     6 |       |
+-----------------------+

------------
Sortie :

+-------+-------+-------+
| 8 3 9 | 4 6 5 | 7 1 2 |
| 1 4 6 | 7 8 2 | 9 5 3 |
| 7 5 2 | 3 9 1 | 4 8 6 |
+-------+-------+-------+
| 3 9 1 | 8 2 4 | 6 7 5 |
| 5 6 4 | 1 7 3 | 8 2 9 |
| 2 8 7 | 6 5 9 | 3 4 1 |
+-------+-------+-------+
| 6 2 8 | 5 3 7 | 1 9 4 |
| 9 1 3 | 2 4 8 | 5 6 7 |
| 4 7 5 | 9 1 6 | 2 3 8 |
+-------+-------+-------+

------------
Résolution en 46,8 secondes (sur un Intel Core i5 à 1,8 GHz)
N.B : Ceci est le sudoku qui a mis le plus de temps a être résolu :
      normalement le temps de résolution ne dépasse pas 5 secondes.
```