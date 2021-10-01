class Room:
    
    def __init__(self, _hasRobot = False):
        self.m_dust = False
        self.m_jewel = False
        self.m_robot = _hasRobot

    #Accessors
    def hasDust(self):
        return self.m_dust

    def hasJewel(self):
        return self.m_jewel

    def hasRobot(self):
        return self.m_robot


    #Mutators  
    def setDust(self, bool):
        self.m_dust = bool

    def setJewel(self, bool):
        self.m_jewel = bool

    def setRobot(self, bool):
        self.m_robot = bool