from House import House
from agent import Agent
from Room import Room

class Training:

    def __init__(self):
        self.m_trainingHouse = House(1,5)
        self.m_robot = Agent(self.m_trainingHouse, 1)      

        #all proba
        self.p_DustVacuum = 34
        self.p_DustPick = 33
        self.p_DustMove = 33

        self.p_JewelVacuum = 34
        self.p_JewelPick = 33
        self.p_JewelMove = 33

        self.p_DustJewelVacuum = 34
        self.p_DustJewelPick = 33
        self.p_DustJewelMove = 33

        self.p_MoveVacuum = 34
        self.p_MovePick = 33
        self.p_Move = 33



    def templateHouse(self, number):
        if number == 0:
            self.m_trainingHouse.clearHouse()
            self.m_trainingHouse.m_rooms[1][3].setDust(True)
            self.m_trainingHouse.m_rooms[1][1].setDust(True)

            self.m_trainingHouse.m_rooms[1][3].setJewel(True)
            self.m_trainingHouse.m_rooms[1][4].setJewel(True)
            self.m_trainingHouse.m_rooms[2][0].setJewel(True)

        elif number == 1:
            self.m_trainingHouse.clearHouse()
            self.m_trainingHouse.m_rooms[1][3].setDust(True)
            self.m_trainingHouse.m_rooms[1][1].setDust(True)

            self.m_trainingHouse.m_rooms[1][3].setJewel(True)
        
        elif number == 2:
            self.m_trainingHouse.clearHouse()
            self.m_trainingHouse.m_rooms[1][3].setDust(True)
            self.m_trainingHouse.m_rooms[1][1].setDust(True)

            self.m_trainingHouse.m_rooms[1][3].setJewel(True)

        elif number == 3:
            self.m_trainingHouse.clearHouse()
            self.m_trainingHouse.m_rooms[1][3].setDust(True)
            self.m_trainingHouse.m_rooms[1][1].setDust(True)

            self.m_trainingHouse.m_rooms[1][3].setJewel(True)

        elif number == 4:
            self.m_trainingHouse.clearHouse()
            self.m_trainingHouse.m_rooms[1][3].setDust(True)
            self.m_trainingHouse.m_rooms[1][1].setDust(True)

            self.m_trainingHouse.m_rooms[1][3].setJewel(True)

        elif number == 5:
            self.m_trainingHouse.clearHouse()
            self.m_trainingHouse.m_rooms[1][3].setDust(True)
            self.m_trainingHouse.m_rooms[1][1].setDust(True)

            self.m_trainingHouse.m_rooms[1][3].setJewel(True)


    def training(self):
        listHouse = 5
        h1 = House(1,5)
        for i in range (listHouse):
            self.templateHouse(i)
            for j in range (15):
                print(self.m_robot.dustPos)
                self.m_robot.live()
                self.getPerformance()
            self.printAllValues()
        

        f = open("Probabilities.txt")

        f.close()

    def getPerformance(self):
        perf = 0
        room = self.m_trainingHouse.m_rooms[self.m_robot.myPos[0]][self.m_robot.myPos[1]]
        if self.m_robot.state.currentState == "vacuum":
            if room.getStateRoom == 1:
                perf = 10
            if room.getStateRoom == 2:
                perf = -30
            if room.getStateRoom == 3:
                perf = -30
            if room.getStateRoom == 4:
                perf = -10
            self.changeProba(perf, self.p_DustVacuum)
            self.changeProba(-perf/2, self.p_DustPick)
            self.changeProba(-perf/2, self.p_DustMove)

        if self.m_robot.state.currentState == "pick up":
            if room.getStateRoom == 1:
                perf = -10
            if room.getStateRoom == 2:
                perf = 10
            if room.getStateRoom == 3:
                perf = 20
            if room.getStateRoom == 4:
                perf = -10
            self.changeProba(perf, self.p_JewelPick)
            self.changeProba(-perf/2, self.p_JewelVacuum)
            self.changeProba(-perf/2, self.p_JewelMove)

        if self.m_robot.state.currentState == "Move":
            if room.getStateRoom == 1:
                perf = -10
            if room.getStateRoom == 2:
                perf = -10
            if room.getStateRoom == 3:
                perf = -30
            if room.getStateRoom == 4:
                perf = 30
            self.changeProba(perf, self.p_Move)
            self.changeProba(-perf/2, self.p_MoveVacuum)
            self.changeProba(-perf/2, self.p_MovePick)        
                        

    def changeProba(self, perf, probastate):
        probastate += perf  

    def printAllValues(self):
        print(self.p_DustVacuum )
        print(self.p_DustPick )
        print(self.p_DustMove)

        print(self.p_JewelVacuum )
        print(self.p_JewelPick )
        print(self.p_JewelMove)
        
        # print(self.p_DustJewelVacuum)
        # print(self.p_DustJewelPick)
        # print(self.p_DustJewelMove)

        print(self.p_MoveVacuum)
        print(self.p_MovePick)
        print(self.p_Move)

test = Training()
test.training()

