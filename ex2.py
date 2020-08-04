class OTHERCLASS():
    def __init__(self,variable1,variable2,variable3):
        self.variable1=variable1
        self.variable2=variable2
        self.variable3=variable3
    def someotherfunction(self):
        something=somecode(self.variable3)
        self.variable2.append(something)
        print(self.variable2)
    def somemorefunctions(self):
        self.variable2.append(variable1)
        
class INITIALCLASS():
    def __init__(self):
        self.variable1=value1
        self.variable2=[]
        self.variable3=''
        self.DoIt=OTHERCLASS(variable1,variable2,variable3)

    def somefunction(self):
        variable3=Somecode
        #tried this
        self.DoIt.someotherfunctions()
        #and this
        DoIt.someotherfunctions()