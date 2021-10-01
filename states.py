class State:

    def __init__(self, _robot):
        self.currentState = "idle"
        self.robot = _robot

    def execute(self):
        if self.currentState == "vacuum":
            self.robot.VacuumRoom()
            self.robot.target = None
            
        elif self.currentState == "pick up":
            self.robot.PickUp()

        elif self.currentState == "move":
            if not self.robot.target:
                self.robot.target = self.robot.dustPos[0]

            print(self.robot.target, self.robot.myPos)

            if self.robot.target[0] < self.robot.myPos[0]:
                self.robot.move([-1, 0])
            elif self.robot.target[0] > self.robot.myPos[0]:
                self.robot.move([1, 0])
            elif self.robot.target[1] < self.robot.myPos[1]:
                self.robot.move([0, -1])
            elif self.robot.target[1] > self.robot.myPos[1]:
                self.robot.move([0, 1])

        elif self.currentState == "idle":
            self.robot.consommation -= 1

        print(self.currentState)
