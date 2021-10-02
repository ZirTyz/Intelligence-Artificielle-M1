import random
import time
import states
import House

class Agent:

    def __init__(self, _house, _speed):
        self.alive = True
        self.myState = None
        self.myPos = [0][0]
        self.dustPos = []
        self.jewelPos = []
        self.dustJewelPos = []
        self.environment = _house
        self.state = states.State(self)
        self.target = None
        self.consommation = 0
        self.speed = _speed
        

        #astar part
        self.probVacuum = 30
        self.probPickUp = 30
        self.probMove   = 40
        self.target = [0, 0]
        self.scoreDust = 8
        self.scoreJewel = 6


    def ObserveEnvironment(self):
        self.dustPos = []
        self.jewelPos = []
        self.dustJewelPos = []
        self.environment.m_rooms
        for x in range(0, len(self.environment.m_rooms)):
            for y in range(0, len(self.environment.m_rooms[x])):
                room = self.environment.m_rooms[x][y]
                if room.getStateRoom() == 1:
                    self.dustPos.append([x, y])
                if room.getStateRoom() == 2:
                    self.jewelPos.append([x, y])
                if room.getStateRoom() == 3:
                    self.dustJewelPos.append([x,y])
                if room.hasRobot():
                    self.myPos = [x, y]
                pass
        pass

    def UpdateMyState(self):
        # if self.jewelPos.__contains__(self.myPos):
        #     self.state.sCurrentState("pick up")
        # elif self.dustPos.__contains__(self.myPos):
        #     self.state.sCurrentState("vacuum")
        # elif len(self.dustPos) != 0:
        #     self.state.sCurrentState("move")
        # else:
        #     self.state.sCurrentState("idle")
        self.getAction()


    def live(self):
        while self.alive:
            # print(self.state.currentState)
            self.ObserveEnvironment()
            self.UpdateMyState()
            self.state.execute()
            self.consommation += 1
            time.sleep(self.speed)
            # if self.consommation == 1:      # Zone Training but not working at time
            #     self.alive = False
            #     self.consommation = 0

    def VacuumRoom(self):
        if self.environment.m_rooms[self.myPos[0]][self.myPos[1]].hasJewel():
            self.environment.removeJewel(self.myPos[0],self.myPos[1])
            self.consommation += 1
        self.environment.removeDust(self.myPos[0],self.myPos[1])

    def PickUp(self):
        self.environment.removeJewel(self.myPos[0],self.myPos[1])

    def move(self, direction):
        self.environment.removeRobot(self.myPos[0],self.myPos[1])
        x = self.myPos[0] + direction[0]
        y = self.myPos[1] + direction[1]
        self.environment.addRobot(x, y)




    def getScore(self, room):
        if room.getStateRoom() == 1: #Dust
            return self.scoreDust
        
        if room.getStateRoom() == 2: #Jewel
            return self.scoreJewel
        
        if room.getStateRoom() == 3: #Dust and Jewel
            return self.scoreDust + self.scoreJewel

        if room.getStateRoom() == 4: #Nothing
            return 0

    def setScore(self):
        f = open("Probabilites.txt")
        f.close()
    
    def getDistance(self, numH, numV ):
        return abs(self.myPos[0] - numH) + abs(self.myPos[1] - numV)
    
    def getTarget(self):
        priorities = []
        weight = 0
        for i in (self.dustJewelPos):
            room = self.environment.m_rooms[i[0]][i[1]]
            weight = self.getScore(room) - self.getDistance(room.getNumH(),room.getNumV())
            priorities.append([room.getNumH(), room.getNumV(),weight])

        for i in (self.dustPos):
            room = self.environment.m_rooms[i[0]][i[1]]
            weight = self.getScore(room) - self.getDistance(room.getNumH(),room.getNumV())
            priorities.append([room.getNumH(), room.getNumV(),weight])

        for i in (self.jewelPos):
            room = self.environment.m_rooms[i[0]][i[1]]
            weight = self.getScore(room) - self.getDistance(room.getNumH(),room.getNumV())
            priorities.append([room.getNumH(), room.getNumV(),weight])

        if priorities.__len__() == 0:
            self.target = None
        else:
            bestTarget = [priorities[0][0], priorities[0][1],priorities[0][2]]
            for j in priorities:
                if bestTarget[2] < j[2]:
                    bestTarget = j

            self.target = [bestTarget[0],bestTarget[1]]
            

    def setProbabilities(self, target):
        targetState = target.getStateRoom()
        if targetState == 1 : #Dust if in position => vacuum near 100% else movement near 100%
            if self.getDistance(self.target[0],self.target[1]) == 0:
                self.probVacuum = 95
                self.probPickUp = 5
                self.probMove = 0
            else:
                self.probVacuum = 5
                self.probPickUp = 5
                self.probMove = 90

        elif targetState == 2: #Jewel
            if self.getDistance(self.target[0],self.target[1]) == 0:
                self.probVacuum = 5
                self.probPickUp = 95
                self.probMove = 0
            else:
                self.probVacuum = 5
                self.probPickUp = 5
                self.probMove = 90

        #Not totally usefull
        elif targetState == 3: #Dust and Jewel
            if self.getDistance(self.target[0],self.target[1]) == 0:
                self.probVacuum = 50
                self.probPickUp = 50
                self.probMove = 0
            else:
                self.probVacuum = 5
                self.probPickUp = 5
                self.probMove = 90
        #

    
    def getAction(self): #target equal to pos of room "Durty"
        self.getTarget()
        if self.target == None:
            self.state.sCurrentState("idle")
        else:
            target = self.environment.m_rooms[self.target[0]][self.target[1]]
            self.setProbabilities(target)
            proba = random.random() * 100
            if proba <= self.probMove:
                self.state.sCurrentState("move")
            elif proba - self.probMove <= self.probPickUp:
                self.state.sCurrentState("pick up")
            elif proba - (self.probMove + self.probPickUp) <= self.probVacuum:
                self.state.sCurrentState("vacuum")
            else:
                self.state.sCurrentState("idle")


        

