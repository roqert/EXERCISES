import myClass

mr = myClass.people("Matthew")
es = myClass.people("Elburz")

mr.tipPercent = 15
mr.total = 150

es.tipPercent = 20
es.total = 80

print(mr.getName())
print(es.getName())

print('- ' * 10)

print(getattr(mr, 'name'))
print(getattr(es, 'name'))

print('- ' * 10)

print(mr.breakout())
print(es.breakout())
