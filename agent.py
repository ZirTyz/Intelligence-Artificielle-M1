import states

class Agent:

    def __init__(self, _robot):
        self.alive = True
        self.myState = None
        self.myPos = [0][0]
        self.dustPos = []
        self.jewelPos = []
        self.environment = None
        self.state = states.State(self)
        self.target = None


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
            self.ObserveEnvironmentWithAllMySensors(self)
            self.UpdateMyState(self)
            self.state.execute(self)