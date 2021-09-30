import time
import states

class Agent:

    def __init__(self):
        self.alive = True
        self.myState = None
        self.myPos = [0][0]
        self.dustPos = []
        self.jewelPos = []
        self.environment = None
        self.state = states.State(self)
        self.target = None
        self.consommation = 0


    def ObserveEnvironment(self):
        self.environment = self.refreshEnvironment()
        self.dustPos = []
        self.jewelPos = []
        for lin in self.environment:
            for col in lin:
                if col.hasDust():
                    self.dustPos.append([lin, col])
                if col.hasJewel():
                    self.jewelPos.append([lin, col])
                if col.hasRobot():
                    self.myPos = [lin, col]
                pass
        pass

    def UpdateMyState(self):
        if self.jewelPos.__contains__(self.myPos):
            self.state.currentState = "pick up"
        elif self.dustPos.__contains__(self.myPos):
            self.state.currentState = "vacuum"
        elif not self.dustPo:
            self.state.currentState = "move"
        else:
            self.state.currentState = "idle"


    def live(self):
        while self.alive:
            self.ObserveEnvironment()
            self.UpdateMyState()
            self.state.execute()
            self.consommation += 1
            time.sleep(1)

    def VacuumRoom(self):
        self.environment[self.myPos].jewel = False
        self.environment[self.myPos].dust = False

    def PickUp(self):
        self.environment[self.myPos].jewel = False

    def move(self, direction):
        self.environment[self.myPos].robot = False
        newPos = self.myPos + direction
        self.environment[newPos].robot = True
