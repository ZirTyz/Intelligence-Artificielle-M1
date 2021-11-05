import solver

sudoku = [
    [3,5,False,    False,False,False,    9,4,False],
    [False,False,8,    1,False,False,    False,5,6],
    [False,6,False,    False,False,8,    1,False,7],

    [False,4,False,    False,7,1,    6,False,3],
    [8,False,False,    5,2,6,    False,False,4],
    [1,False,6,    8,3,False,    False,9,False],

    [5,False,4,    7,False,False,    False,6,False],
    [9,1,False,    False,False,5,    4,False,False],
    [False,8,2,    False,False,False,    False,7,9]
]
sudoku2 = [
    [False,4,False,    False,5,False,    8,False,False],
    [False,False,False,    3,False,False,    False,False,6],
    [False,False,6,    False,False,False,    False,False,False],

    [False, False, False, False, 8, False,  2, 5, False],
    [False,3,2,    False,False,False,    6,False,False],
    [False,False,False,    4,False,7,    False,False,3],

    [3, False, False, False, 9, 8, 1, False, False],
    [8,False,False,    False,False,False,    False,7,False],
    [1,False,False,    False,6,False,    False,3,8],
]
solver.solveCSP(sudoku)
solver.solveCSP(sudoku2)



