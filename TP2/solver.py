def solveCSP(sudoku):
    variables = []
    for line in range(1, 9+1):
        for col in range(1, 9+1):
            variables.append(str(line) + str(col))
    domain = []
    for var in range(1, 9+1):
        domain.append(str(var))
    constraints = []
    #not 2 time in the same line
    for lin in range(1, 9+1):
        for var in range(1, 8+1):
            for check in range(var +1, 9+1):
                    constraints.append(str(lin) + str(var) + "!="+ str(lin)+str(check))


    # not 2 time in the same col
    for col in range(1, 9 + 1):
        for var in range(1, 8 + 1):
            for check in range(var + 1, 9 + 1):
                constraints.append(str(var) + str(col) + "!=" + str(check) + str(col))


    # not 2 time in the same square
    for linSquare in range(0, 3 ):
        for colSquare in range(0, 3):
            for ele in range(0, 8 ):
                for check in range(ele+1, 9 ):
                    constraints.append(str(int(ele/3)+1+3*linSquare) + str(ele%3+1+3*colSquare) + "!=" + str(int(check/3)+1+3*linSquare) + str(check%3+1+3*colSquare))
            #for linEle in range(1+3*linSquare, 3*linSquare + 3 + 1):
                #for colEle in range(1 + 3 * colSquare, 3 * colSquare + 3 + 1):

    print("variables : ")
    print(variables)
    print("domain : ")
    print(domain)
    print("constraints : ")
    print(constraints)
    #print(len(constraints))




