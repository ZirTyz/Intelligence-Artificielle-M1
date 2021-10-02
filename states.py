

class State:



    def __init__(self, _robot):
        self.currentState = "idle"
        self.robot = _robot
        self.isCalledOnce = False


    def sCurrentState(self, state):
        if state == None:
            return self.currentState
        
        else :
            if self.currentState == state:
                None
            else:
                self.currentState = state
                self.CalledOnce = False

        

    def execute(self):
        if self.currentState == "vacuum":
            # self.robot.VacuumRoom()
            # self.robot.target = None

            self.vacuum_Update()

        elif self.currentState == "pick up":
            # self.robot.PickUp()

            self.pickup_Update()
        elif self.currentState == "move":
            self.move_Update()


        elif self.currentState == "idle":
            self.idle_update()
            # self.robot.consommation -= 1

#region vacuum

    def vacuum_Start(self):
        self.isCalledOnce = True


    def vacuum_Update(self):
        if (self.isCalledOnce == False):
            self.vacuum_Start()


        self.robot.VacuumRoom()
        self.robot.target = None

#endregion

#region pick up

    def pickup_Start(self):
        self.isCalledOnce = True


    def pickup_Update(self):
        self.robot.PickUp()

#endregion

#region movement

    def move_Start(self):
        self.isCalledOnce = True


    def move_Update(self):
        if (self.isCalledOnce == False):
            self.move_Start()
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

#endregion

#region idle

    def idle_start(self):
        self.isCalledOnce = True
        

    def idle_update(self):
        if self.isCalledOnce == False:
            self.idle_start()

        self.robot.consommation -= 1

#endregion