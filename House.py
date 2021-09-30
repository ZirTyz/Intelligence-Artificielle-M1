from Room import Room
import random
import time

class House:
    m_rooms =[  [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]   ]
    print(m_rooms)
    def __init__(self):
        self.createHouse(5,5)

    def createHouse(self, nbRoomH, nbRoomV):
        for i in range (nbRoomH):
            for j in range (nbRoomV):
                self.m_rooms[i][j] = Room()
    
    def updateHouse(self):
        proba = random.random() * 100
        nbroomH = random.randint(0, 4)
        nbroomV = random.randint(0, 4)
        if proba < 15:
            self.addDust(nbroomH,nbroomV)
        elif proba < 30:
            self.addJewel(nbroomH,nbroomV)

        print(proba)



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

# Game loop
house = House()

while (1):
    house.updateHouse()
    time.sleep(3)
  
