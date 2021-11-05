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
        
        for box in _boxs:
            box.RemoveDomain(_value)

    def restore(self, _value, _boxs):
        for box in _boxs:
            box.RestoreDomain(_value) 