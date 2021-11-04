import solver

print("hello world")
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
print(sudoku)
solver.solveCSP(sudoku)



