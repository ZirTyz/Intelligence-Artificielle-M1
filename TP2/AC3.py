class AC3:
# Propagation de contraintes
# 
    # m_domain = []
    # m_variables = []
    # m_constraints = []
    # def __init__(self,domain, variables, constraints):
    #     self.m_domain = domain
    #     self.m_variables = variables
    #     self.m_constraints = constraints

    def resolve(self):
        pass

    def propagate(self, _value, _boxs):
        boxContraint = []
        for box in _boxs:
            if(box.RemoveDomain(_value) == 1):
                boxContraint.append(box)
        return boxContraint


    def restore(self, _value, _boxs,_boxC):
        for box in _boxs:
            if not (box in _boxC): 
                box.RestoreDomain(_value) 