
#Part1: YTM
#Reference: https://www.calkoo.com/en/ytm-calculator
pv = float(input("Current Bond Price: "))
fv = float(input("Bond Par Value: "))
c = float(input("Bond Coupon Rate(%): "))/100
t = int(input("Years to Maturity: "))
payment = int(input("How many coupon payment per year: "))

ytm = 0.2 #先假設一個較高的YTM
ytm_min = 0

#確定真實YTM的範圍介在 ytm_min 與 ytm_max 之間
pvTest = sum([c / payment * fv/(1 + ytm / payment)**(i) for i in range(1, payment * t + 1)]) + fv/(1 + ytm / payment)**(t * payment)
while pvTest > pv:
	ytm_min = ytm
	ytm += 0.1
	pvTest = sum([c / payment * fv/(1 + ytm / payment)**(i * payment) for i in range(1, payment * t + 1)]) + fv/(1 + ytm / payment)**(t * payment)	
ytm_max = ytm	

#每次都取範圍裡的中間值，不斷縮小範圍
ytm = (ytm_min + ytm_max) / 2	
pvTest = sum([c / payment * fv/(1 + ytm / payment)**(i * payment) for i in range(1, payment * t + 1)]) + fv/(1 + ytm / payment)**(t * payment)
while abs(pvTest - pv) > 0.001:
	if pvTest < pv:
		ytm_max = ytm
		ytm = (ytm_min + ytm) / 2
	elif pvTest > pv:
		ytm_min = ytm
		ytm = (ytm_max + ytm) / 2
	pvTest = sum([c / payment * fv/(1 + ytm / payment)**(i * payment) for i in range(1, payment * t + 1)]) + fv/(1 + ytm / payment)**(t * payment)

#四捨五入到小數點第二位

ytm = (1 + ytm) ** (1 / payment) - 1
ytm_str = str(round(ytm * 100, 2))	
print('YTM:' + ytm_str + '%')



#-----------------------------------------------------------------------------------------------------------------------------------------------------------

#Part2: Spot Rate
#Reference: https://www.trignosource.com/finance/spot%20rate.html

pv = float(input("Current Bond Price: "))
fv = float(input("Bond Par Value: "))
t = int(input("Years to Maturity: "))

sp = (fv / pv)**(1 / t) - 1
sp_str = str(round(sp * 100, 2))	
print('Spot Rate:' + sp_str + '%')


#-----------------------------------------------------------------------------------------------------------------------------------------------------------


#Part3: Forward Rate
#Reference: https://www.trignosource.com/finance/Forward%20rate.html#Calculator

from prettytable import PrettyTable

period = int(input("Duration of forward rate (years): "))
fv = float(input("Par Value of zero coupon bond: "))

price = []
number = []
number.append(" ")
number.append(0)

x = PrettyTable()

#輸入不同期限 zero coupon 的價格
for i in range (1, period + 1):
	pv = float(input("Price of " + str(i) + " year zero coupon bond: "))
	price.append(pv)
	number.append(i)
x.field_names = number

spotrate = []
spotrate.append(0)
spotrate.append('0%')

#計算從現在出發到各期的forward rate: 相當於各期的 spot rate
for i in range(1, period + 1):
	spot = (fv / price[i - 1])**(1 / i) - 1
	spot_str = str(round(spot * 100, 2))
	spotrate.append(spot_str + '%')
x.add_row(spotrate)

#計算其他期間的 forward rate
row = []
for i in range(period):
	row.append(i+1)
	row.append('-')
	for j in range(period):
		if i == j:
			row.append('0%')
		elif i > j:
			row.append('-')
		else:
			forward = (price[i] / price[j])**(1 / (j - i)) - 1
			forward_str = str(round(forward * 100, 2))
			row.append(forward_str + '%')
	x.add_row(row)
	row = []
		
print(x)









