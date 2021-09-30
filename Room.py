class Room:
    m_dust = False
    m_jewel = False
    m_robot = False
    
    def __init__(self):
        self.m_dust = False
        self.m_jewel = False

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