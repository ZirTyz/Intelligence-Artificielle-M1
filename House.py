from Room import Room
import random
import time

class House:
    m_rooms =[  [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]   ]

    def __init__(self):
        self.createHouse(5,5)
        self.alive = True

    def createHouse(self, nbRoomH, nbRoomV):
        for i in range (nbRoomH):
            for j in range (nbRoomV):
                if i == 2 and j == 2:
                    self.m_rooms[i][j] = Room(True)
                else:
                    self.m_rooms[i][j] = Room()
    
    def updateHouse(self):
        proba = random.random() * 100
        nbroomH = random.randint(0, 4)
        nbroomV = random.randint(0, 4)
        if proba < 15:
            self.addDust(nbroomH,nbroomV)
        elif proba < 30:
            self.addJewel(nbroomH,nbroomV)



    #Mutators

    def addDust(self, nRoomH, nRoomV):
        self.m_rooms[nRoomH][nRoomV].setDust(True)

    def addJewel(self, nRoomH, nRoomV):
        self.m_rooms[nRoomH][nRoomV].setJewel(True)

    def addRobot(self, nRoomH, nRoomV):
        self.m_rooms[nRoomH][nRoomV].setRobot(True)

    def removeDust(self, nRoomH, nRoomV):
        self.m_rooms[nRoomH][nRoomV].setDust(False)

    def removeJewel(self, nRoomH, nRoomV):
        self.m_rooms[nRoomH][nRoomV].setJewel(False)

    def removeRobot(self, nRoomH, nRoomV):
        self.m_rooms[nRoomH][nRoomV].setRobot(False)

    def live(self):
        while self.alive:
            self.updateHouse()
            time.sleep(1)
