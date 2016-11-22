import pylab
principal = 10000
interestRate = 0.05
toyears = 20
values = []
for i in range(years + 1):
	values.append(principal)
	principal += principal*interestRate
pylab.plot(values)	
pylab.title('5% growth compounnded annually')
pylab.xlabel('years')
pylab.ylabel('value')
