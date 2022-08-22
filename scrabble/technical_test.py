import random



bag= 'E'*7 + 'A'*9 + 'I' * 9 + 'O'*8 + 'NRT' * 6 + 'LSUD'*4 + 'G'*3 + 'BCMPFHVWY'*2  + 'KJXQZ'
bag=[*bag]


def take_random_tiles(int):
    placerack=[]
    for i in range(int):
        index = random.randint(0,len(bag))
        tile_picked=bag.pop(index)
        placerack.append(tile_picked)
    return placerack

print(take_random_tiles(7))





points= {
    "A":1, "E": 1, "E": 1, "A":1 , "I":1 , "O":1 , "N":1 , "R":1 , "T":1 , "L":1 , "S":1 , "U":1,
    "D":2 , "G": 2 , "B":3 , "C":3, "M":3, "P":3 , "F":4, "H":4, "V":4, "W":4, "Y":4, "K":5 , "J":8, "X":8 , "Q":10,"Z":10}


def calculate_points(word):
    total_points = 0 
    for letter in word: 
        total_points+=points[letter]
    return total_points





# | Point(s) | Letter(s)                    |
# | -----    | ---------------------------- |
# | 1        | E, A, I, O, N, R, T, L, S, U |
# | 2        | D, G                         |
# | 3        | B, C, M, P                   |
# | 4        | F, H, V, W, Y                |
# | 5        | K                            |
# | 8        | J, X                         |
# | 10       | Q, Z                         |


# Distribution	Letter(s)
# 12 tiles	E
# 9 tiles	A, I
# 8 tiles	O
# 6 tiles	N, R, T
# 4 tiles	L, S, U, D
# 3 tiles	G
# 2 tiles	B, C, M, P, F, H, V, W, Y
# 1 tile	K, J, X, Q, Z

