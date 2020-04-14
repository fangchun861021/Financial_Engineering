
import math

s = float(input("stock price: "))
x = float(input("strike price: "))
u = float(input("upward rate: "))
d = float(input("downword rate: "))
r = float(input("riskless rate: "))
n = int(input("period: "))


#Step1 find Rate & Probability
R = math.exp(r)
prob = (R - d) / (u - d)


#Step2 find stock price for n period
stock = []
stock.append(s)
stock.append(s)

for i in range (1,n + 1):
	su = round(stock[int((i * (i - 1)) / 2 + 1)] * u,3)
	stock.append(su)
	
	for j in range(i):
		sd = round(stock[int((i * (i - 1)) / 2 + 1 + j)] * d,3)
		stock.append(sd)


#Step3 find call option price
call = []
stock_n = stock[-(n + 1) : ]
for i in stock_n:
	if i > x:
		c = i - x
	else:
		c = 0
	call.append(c)

#backward induction
while len(call) > 1:
	newcall = []
	for i in range(len(call) - 1):
		
		newc = round(((prob * call[i]) + ((1 -  prob) * call[i + 1])) / R,3)
		newcall.append(newc)
	call = newcall

print('Call Value: ' + str(call[0]))


#Step4 find put option price
put = []
stock_n = stock[-(n + 1) : ]
for i in stock_n:
	if i > x:
		p = 0
	else:
		p = x - i
	put.append(p)

#backward induction
while len(put) > 1:
	newput = []
	for i in range(len(put) - 1):
		newp = round(((prob * put[i]) + ((1 -  prob) * put[i + 1])) / R,3)
		newput.append(newp)
	put = newput
	
print('Put Value: ' + str(put[0]))















