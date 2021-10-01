from states import State


class Room:
    
    def __init__(self, numH, numV, _hasRobot = False):
        self.m_dust = False
        self.m_jewel = False
        self.m_robot = _hasRobot
        self.m_numH = numH
        self.m_numV = numV

    #Accessors
    def hasDust(self):
        return self.m_dust

    def hasJewel(self):
        return self.m_jewel

    def hasRobot(self):
        return self.m_robot

    def getNumH(self):
        return self.m_numH

    def getNumV(self):
        return self.m_numV


    #Mutators  
    def setDust(self, bool):
        self.m_dust = bool

    def setJewel(self, bool):
        self.m_jewel = bool

    def setRobot(self, bool):
        self.m_robot = bool

#Utils

    def getStateRoom(self):
        
        if self.hasDust() and self.hasJewel() ==False:
            return 1
            
        elif self.hasJewel() and self.hasDust() == False:
            return 2

        elif self.hasDust() and self.hasJewel():
            return 3

        else:
            return 4
        