class people:
    def __init__(self, name=None):
        self.name = name
        self.total = None
        self.tipPercent = None

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def calcTip(self):
        tip = self.total * (self.tipPercent /100)
        return tip

    def calcTotalWithTip(self):
        tip = self.calcTip()
        return self.total + tip

    def breakout(self):
        tip = self.calcTip()
        calcTotal = self.calcTotalWithTip()

        prettyTotal = '''- - - - -
Name                = {name}

Bill Total          = ${total}
Tip Percent         = {tipPercent} %

Calculated Tip      = ${tip}
Calculated Total    = ${calcTotal}
- - - - -'''
        breakoutText = prettyTotal.format(  name=self.name,
                                            total=self.total, 
                                            tipPercent=self.tipPercent,
                                            tip=tip,
                                            calcTotal=calcTotal)
        
        return breakoutText