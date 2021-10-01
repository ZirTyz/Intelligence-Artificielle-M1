import time
import states
import House

class Agent:

    def __init__(self, _house):
        self.alive = True
        self.myState = None
        self.myPos = [0][0]
        self.dustPos = []
        self.jewelPos = []
        self.environment = _house
        self.state = states.State(self)
        self.target = None
        self.consommation = 0


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
            self.state.currentState = "pick up"
        elif self.dustPos.__contains__(self.myPos):
            self.state.currentState = "vacuum"
        elif len(self.dustPos) != 0:
            self.state.currentState = "move"
        else:
            self.state.currentState = "idle"


    def live(self):
        while self.alive:
            print("agent is living")
            self.ObserveEnvironment()
            self.UpdateMyState()
            self.state.execute()
            self.consommation += 1
            time.sleep(1)

    def VacuumRoom(self):
        if self.environment[self.myPos].hasJewel():
            self.environment.removeJewel(self.myPos[0],self.myPos[1])
            self.consommation += 1
        self.environment[self.myPos].removeDust(self.myPos[0],self.myPos[1])

    def PickUp(self):
        self.environment[self.myPos].removeJewel(self.myPos[0],self.myPos[1])

    def move(self, direction):
        self.environment[self.myPos].removeRobot(self.myPos[0],self.myPos[1])
        newPos = self.myPos + direction
        self.environment[newPos].addRobot(self.myPos[0],self.myPos[1])
