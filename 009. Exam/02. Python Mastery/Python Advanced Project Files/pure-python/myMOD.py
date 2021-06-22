def calcTip(total, tipPercent):
    tip = total * (tipPercent /100)
    return tip

def calcTotalWithTip(total, tipPercent):
    tip = calcTip(total, tipPercent)
    return total + tip

def breakout(total, tipPercent):
    tip = calcTip(total, tipPercent)
    calcTotal = calcTotalWithTip(total, tipPercent)

    prettyTotal = '''- - - - -
Bill Total          = ${total}
Tip Percent         = ${tipPercent}

Calculated Tip      = ${tip}
Calculated Total    = ${calcTotal}
- - - - -'''.format(total=total, 
                    tipPercent=tipPercent,
                    tip=tip,
                    calcTotal=calcTotal)
    
    return prettyTotal