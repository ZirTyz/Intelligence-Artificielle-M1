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
