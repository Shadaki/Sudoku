# Résolution du sudoku
Ce programme utilise une méthode de balayage « lourde ».

Les *inputs* se font en mettant tous les chiffres sur une seule ligne (de gauche à droite, de bas en haut) et en remplaçant tous les blancs par des zéros.

`
Ex: .......12........3..23..4....18....5.6..7.8.......9.....85.....9...4.5..47...6...`

qui équivaut au sudoku ci-dessous :

```
Le sudoku qui a demandé le plus de temps :
46,8 secondes sur un Intel Core i5 à 1,8 GHz

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
```