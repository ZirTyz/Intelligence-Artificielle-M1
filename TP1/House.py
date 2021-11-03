from TP1.Room import Room
import random
import time

class House:


    def __init__(self, _speed, _size):
        self.size = _size
        self.m_rooms = [list(range(0, self.size)) for i in range(self.size)]
        self.createHouse(self.size)
        self.alive = True
        self.speed = _speed

    def createHouse(self, size):
        for i in range (size):
            for j in range (size):
                self.m_rooms[i][j] = Room(i,j)
        self.m_rooms[0][0].setRobot(True)

    
    def updateHouse(self):
        proba = random.random() * 100
        nbroomH = random.randint(0, self.size-1)
        nbroomV = random.randint(0, self.size-1)
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

    def clearHouse(self):
        for i in range (5):
            for j in range (5):
                self.m_rooms[i][j].setDust(False)
                self.m_rooms[i][j].setJewel(False)
                self.m_rooms[i][j].setRobot(False)
        self.m_rooms[2][2].setRobot(True)


    def live(self):
        while self.alive:
            self.updateHouse()
            time.sleep(self.speed)
