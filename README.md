# Résolution du SUDOKU
Ce programme utilise une méthode de balayage « lourde ».

Les *inputs* se font en mettant tous les chiffres sur une seule ligne (de gauche à droite, de bas en haut) et en remplaçant tous les blancs par des zéros.
`Ex: 000000012000000003002300400001800005060070800000009000008500000900040500470006000`
qui équivaut au sudoku ci-dessous


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