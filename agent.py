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


    def ObserveEnvironment(self):
        self.dustPos = []
        self.jewelPos = []
        self.environment.m_rooms
        for x in range(0, len(self.environment.m_rooms)):
            for y in range(0, len(self.environment.m_rooms[x])):
                room = self.environment.m_rooms[x][y]
                if room.hasDust():
                    self.dustPos.append([x, y])
                if room.hasJewel():
                    self.jewelPos.append([x, y])
                if room.hasRobot():
                    self.myPos = [x, y]
                pass
        pass

    def UpdateMyState(self):
        if self.jewelPos.__contains__(self.myPos):
            self.state.sCurrentState("pick up")
        elif self.dustPos.__contains__(self.myPos):
            self.state.sCurrentState("vacuum")
        elif len(self.dustPos) != 0:
            self.state.sCurrentState("move")
        else:
            self.state.sCurrentState("idle")


    def live(self):
        while self.alive:
            print(self.state.currentState)
            self.ObserveEnvironment()
            self.UpdateMyState()
            self.state.execute()
            self.consommation += 1
            time.sleep(self.speed)

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
            return 6
        
        if room.getStateRoom() == 2: #Jewel
            return 8
        
        if room.getStateRoom() == 3: #Dust and Jewel
            return 14

        if room.getStateRoom() == 4: #Nothing
            return 0
    def getDistance(self, numH, numV ):
        
        return abs(self.myPos[0] - numH) + abs(self.myPos[1] - numV)

    def getAction(self, target): #target equal to pos of room durty
        setProbabilities()

    def setProbabilities(self, target):
        if target == 1 : #Dust if in position => vacuum near 100% else movement near 100%
            if self.getDistance(self.target[0],self.target[1]) == 0:
                self.probVacuum = 95
                self.probPickUp = 5
                self.probMove = 0
            else:
                self.probVacuum = 5
                self.probPickUp = 5
                self.probMove = 90

        #if target == 2
        #
        #

