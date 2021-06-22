import myMOD

total = 50.00
tipPercent = 20

totalWithTip = myMOD.calcTotalWithTip(total, tipPercent)
tipTotal = myMOD.calcTip(total, tipPercent)
breakout = myMOD.breakout(total, tipPercent)

print(tipTotal)
print(totalWithTip)

print(breakout)