import copy

def solveCSP(sudoku):
    graph = Graph()
    variables = []
    for lin in range(0, 9):
        for col in range(0, 9):
            variables.append((lin,col))
            graph.addBox(Box(lin, col))
    domain = []
    for var in range(1, 10):
        domain.append(var)
    constraints = []

    #not 2 time in the same line
    for lin in range(0, 9):
        for var in range(0, 9):
            for check in range(0, 9):
                    if var != check:
                        constraints.append(((lin,var), ((lin),(check))))
                        graph.getBox(lin, var).addArc(graph.getBox(lin,check))


    # not 2 time in the same col
    for col in range(0, 9):
        for var in range(0, 9):
            for check in range(0, 9):
                if var != check:
                    constraints.append(((var, col), ((check), (col))))
                    graph.getBox(var, col).addArc(graph.getBox(check, col))


    # not 2 time in the same square
    for linSquare in range(0, 3 ):
        for colSquare in range(0, 3):
            for ele in range(0, 9 ):
                for check in range(0, 9 ):
                    if ele != check:
                        constraints.append(((int(ele/3)+3*linSquare, ele%3+3*colSquare), ((int(check/3)+3*linSquare), (check%3+3*colSquare))))
                        graph.getBox(int(ele/3)+3*linSquare, ele%3+3*colSquare).addArc(graph.getBox(int(check/3)+3*linSquare, check%3+3*colSquare))
            #for linEle in range(1+3*linSquare, 3*linSquare + 3 + 1):
                #for colEle in range(1 + 3 * colSquare, 3 * colSquare + 3 + 1):

    csp = CSP(variables, domain, constraints, sudoku, graph)
    result = RecursiveBacktrackingSearch(csp)
    if result:
        for i in range(0, 9):
            print(result.assignments[i])
    else:
        print("pas de solution possible")

class CSP:
    def __init__(self, _variables,_domain, _constraints, _assignments, _graph):
        self.variables = _variables
        self.domain = _domain
        self.constraints = _constraints

        self.graph = _graph

        self.assignments = _assignments
        self.possibleValues = [ [ 0 for i in range(9) ] for j in range(9) ]

        for var in self.variables:
            self.possibleValues[var[0]][var[1]] = self.domain.copy()

        for lin in range(0, 9):
            for col in range(0, 9):
                if self.assignments[lin][col]:
                    self.possibleValues[lin][col] = [self.assignments[lin][col]]
                    AC3(self, self.graph.getBox(lin, col), self.assignments[lin][col])

        for i in range(0, 9):
            print(self.assignments[i])

        for i in range(0, 9):
            print(self.possibleValues[i])

class Graph:
    def __init__(self):
        self.boxes = [ [ False for i in range(9) ] for j in range(9) ]

    def addBox(self,  box):
        self.boxes[box.x][box.y] = box

    def getBox(self, x, y):
        return self.boxes[x][y]

class Box:
    def __init__(self,_x, _y):
        self.x = _x
        self.y = _y
        self.arcs = []

    def addArc(self, box):
        try:
            self.arcs.index(box)
        except:
            self.arcs.append(box)



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

def selectUnasingnedBoxMRV(csp):
    minDomain = csp.possibleValues[0][0].__len__()
    nextBox = csp.variable[0]
    for box in csp.variables:
        if not (csp.assignments[box.x][box.y]):
            if (minDomain > possibleDomainValue(box,csp).__len__()): #csp.possibleValues[box[0]][box[1]].__len__()
                nextBox = box
                minDomain = possibleDomainValue(box,csp).__len__()
    return nextBox

def selectUnasingnedBoxEuristic(csp):
    sommeContrainte = 0
    boxEuristicList = []
    for box in csp.variables:
        if not (csp.assignements[box.x][box.y]):
            for linkBox in box.arcs:
                if not (csp.assignements[linkBox.x][linkBox.y]):
                    sommeContrainte += possibleDomainValue(linkBox,csp).__len__()

            boxEuristicList.append([sommeContrainte,box])
            sommeContrainte = 0
    boxEuristicList.sort()
    return boxEuristicList[0][1]
            


    
# todo fill

def possibleDomainValue(box, csp):
    return csp.possibleValues[box.x][box.y]

#Least constraining value
#todo will sort possible domain value by least contraining to most
def possibleDomainValueLCV(box, csp):
    # LCVBox = []
    # for nextValue in possibleDomainValue(box,csp):
    #     for nextBox in box.arcs:
    #         if not (csp.assignements[nextBox.x][nextBox.y]):
    #             LCVBox.append([(csp.possibleValues[nextBox.x][nextBox.y].__len__() - (nextValue in csp.possibleValues[nextBox.x][nextBox.y]),nextBox])
    #     LCVBox.sort()
    # return    
    LCVsommeList = []
    LCVsomme = 0
    for nextValue in possibleDomainValue(box,csp):
        for nextBox in box.arcs:
            if not (csp.assignements[nextBox.x][nextBox.y]):
                LCVsomme += (nextValue in csp.possibleValues[nextBox.x][nextBox.y])
        LCVsommeList.append([LCVsomme,nextValue])
        LCVsomme = 0
    LCVsommeList.sort()
    return LCVsommeList[0][1]

 # todo fill
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
    save = copy.deepcopy(csp.possibleValues)
    for var in possibleDomainValue(box2process, csp):
        csp.assignments[box2process[0]][box2process[1]] = var
        csp.possibleValues[box2process[0]][box2process[1]] = [var]
        if AC3(csp, csp.graph.getBox(box2process[0],box2process[1]), var) and constraintsGood(csp):
            result = RecursiveBacktrackingSearch(csp)
            if result:
                return result
            else:
                csp.assignments[box2process[0]][box2process[1]] =  False
                csp.possibleValues = copy.deepcopy(save)
        else:
            csp.assignments[box2process[0]][box2process[1]] =  False
            csp.possibleValues = copy.deepcopy(save)
    return False

def AC3(csp, box, value):
    for box2process in box.arcs:
        removed = removeValue(csp, box2process, value)
        if removed:
            if len(csp.possibleValues[box2process.x][box2process.y])<1:
                return False
            elif len(csp.possibleValues[box2process.x][box2process.y])==1:
                if not AC3(csp, box2process, csp.possibleValues[box2process.x][box2process.y][0]):
                    return False
    return True

def removeValue(csp, arc, value):
    removed = False
    if value in  csp.possibleValues[arc.x][arc.y]:
        csp.possibleValues[arc.x][arc.y].remove(value)
        removed = True
    return removed






