import AC3, Tile


def solveCSP(sudoku):
    variables = []
    variablesTiles = [list(range(0, 9)) for i in range(9)]
    for lin in range(0, 9):
        for col in range(0, 9):
            variables.append((lin,col))
            variablesTiles[lin][col] = (Tile.Tile(lin,col,getSection(lin,col)))
    domain = []
    for var in range(1, 10):
        domain.append(var)
    constraints = []

    #not 2 time in the same line
    for lin in range(0, 9):
        for var in range(0, 8):
            for check in range(var+1, 9):
                    constraints.append(((lin,var), ((lin),(check))))


    # not 2 time in the same col
    for col in range(0, 9):
        for var in range(0, 8):
            for check in range(var+1, 9):
                constraints.append(((var, col), ((check), (col))))


    # not 2 time in the same square
    for linSquare in range(0, 3 ):
        for colSquare in range(0, 3):
            for ele in range(0, 8 ):
                for check in range(ele+1, 9 ):
                    constraints.append(((int(ele/3)+3*linSquare, ele%3+3*colSquare), ((int(check/3)+3*linSquare), (check%3+3*colSquare))))
            #for linEle in range(1+3*linSquare, 3*linSquare + 3 + 1):
                #for colEle in range(1 + 3 * colSquare, 3 * colSquare + 3 + 1):

    print("variables : ")
    print(variables)
    print("domain : ")
    print(domain)
    print("constraints : ")
    print(constraints)
    #print(len(constraints))

    csp = CSP(variablesTiles, variables, domain, constraints, sudoku)
    print(csp.assignments)
    
    result = RecursiveBacktrackingSearch(csp)
    if result:
        for i in range(0, 9):
            print(result.assignments[i])
            

    for i in range(0,9): # Pas d'assignement des valeurs d'origne du sudoku 
        for j in range(0,9):
            print(csp.variableTile[i][j].m_value)
    else:
        print("pas de solution possible")

class CSP:
    def __init__(self, _variableTile, _variables,_domain, _constraints, _assignments):
        self.variableTile = _variableTile
        self.variables = _variables
        self.domain = _domain
        self.constraints = _constraints
        self.assignments = _assignments
        self.ac3 = AC3.AC3()

def constraintsGood(csp):
    good = True
    for constraint in csp.constraints:

        a = csp.assignments[constraint[0][0]][constraint[0][1]]
        b = csp.assignments[constraint[1][0]][constraint[1][1]]
        if a and b and a == b:
            good = False
            break
    return good

def selectUnasingnedBox(csp):
    for box in csp.variables:
        if not (csp.assignments[box[0]][box[1]]):
            return box

def possibleDomainValue(box, csp):
    return csp.domain

def unasingnedBoxLinkTo(ibox, csp):
    linkBoxEmpty = []
    sectionIbox = getSection(ibox.m_line, ibox.m_column)
    for boxl in csp.variableTile:
        for box in boxl:
            if (ibox.m_line == box.m_line or  ibox.m_column == box.m_column):
                if not (csp.assignments[box.m_line][box.m_column]):
                    linkBoxEmpty.append(box)
            else :
                if (sectionIbox == getSection(box.m_line,box.m_column)):
                    linkBoxEmpty.append(box)
    return linkBoxEmpty


# def getSection(box):
    # if (box[0] in range(1,4) and box[1] in range(1,4)):
    #     return 1
    # elif (box[0] in range(4,7) and box[1] in range(1,4)):
    #     return 2
    # elif (box[0] in range(7,10) and box[1] in range(1,4)):
    #     return 3
    # elif (box[0] in range(1,4) and box[1] in range(4,7)):
    #     return 4
    # elif (box[0] in range(4,7) and box[1] in range(4,7)):
    #     return 5
    # elif (box[0] in range(7,10) and box[1] in range(4,7)):
    #     return 6
    # elif (box[0] in range(1,4) and box[1] in range(7,10)):
    #     return 7
    # elif (box[0] in range(4,7) and box[1] in range(7,10)):
    #     return 8
    # elif (box[0] in range(7,10) and box[1] in range(7,10)):
    #     return 9  
def getSection(l,c):  
    if (l in range(0,3) and c in range(0,3)):
        return 1
    elif (l in range(3,6) and c in range(0,3)):
        return 2
    elif (l in range(6,9) and c in range(0,3)):
        return 3
    elif (l in range(0,3) and c in range(3,6)):
        return 4
    elif (l in range(3,6) and c in range(3,6)):
        return 5
    elif (l in range(6,9) and c in range(3,6)):
        return 6
    elif (l in range(0,3) and c in range(6,9)):
        return 7
    elif (l in range(3,6) and c in range(6,9)):
        return 8
    elif (l in range(6,9) and c in range(6,9)):
        return 9


def AssignementIsFull(csp):
    full = True
    for lin in range(0, 9):
        for col in range(0, 9):
            if not csp.assignments[lin][col]:
                return False
    return True


def RecursiveBacktrackingSearch(csp):
    if AssignementIsFull(csp):
        return csp
    box2process = selectUnasingnedBox(csp)
    # for var in possibleDomainValue(box2process, csp):
    currentBox = csp.variableTile[box2process[0]][box2process[1]]
    for var in currentBox.getDomain():
        csp.assignments[box2process[0]][box2process[1]] = var
        currentBox.setValue(var)
        if constraintsGood(csp):
            boxContraint = csp.ac3.propagate(var, unasingnedBoxLinkTo(currentBox,csp))
            result = RecursiveBacktrackingSearch(csp)
            if result:
                return result
            else:
                csp.ac3.restore(var, unasingnedBoxLinkTo(currentBox,csp),boxContraint )
                csp.assignments[box2process[0]][box2process[1]] =  False
                csp.variableTile[box2process[0]][box2process[1]].setValue(False)
        else:
            csp.assignments[box2process[0]][box2process[1]] =  False
            csp.variableTile[box2process[0]][box2process[1]].setValue(False)
    return False







