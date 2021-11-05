class Tile:
    def __init__(self,line,column,section):
        self.m_line = line
        self.m_column = column
        self.m_section = section
        self.m_domain = [1,2,3,4,5,6,7,8,9]
        self.m_value = False


    def RemoveDomain(self, value):
        if (value in self.m_domain):
            self.m_domain.remove(value)
        else: 
            return 1 # return value for least constraining value
    def RestoreDomain(self, value):
        self.m_domain.append(value)
    def setValue(self, value):
        self.m_value = value
    def getDomain(self):
        return self.m_domain