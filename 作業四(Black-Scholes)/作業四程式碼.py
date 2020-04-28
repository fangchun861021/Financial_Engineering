from scipy.stats import norm
import math

print("Input")
s = float(input("Stock price: "))
x = float(input("Strike price: "))
sigma = float(input("Volatility: "))
d = float(input("Dividends: "))
period = int(input("How many times of dividends per year: "))

month = []
for i in range (1, period + 1):
	month.append(int(input("Which month to pay %dth dividends: " %(i))))

r = float(input("Return rate: "))
t = float(input("How long to mature (year): "))


#Step1 calculate total dividends
D = 0
for i in range(period):
	D += d * math.exp( -r * month[i] / 12)


#Step2 calculate d1 & d2
s_true = s - D
d_1 = (math.log(s_true / x) + (r + sigma**2 / 2) * t) / (sigma * t**(1/2))
d_2 = d_1 - (sigma * t**(1/2))


#Step3 calculate put value
p = round(x * math.exp(-r * t) * norm.cdf(-d_2) - s_true * norm.cdf(-d_1),2)


#Step4 calculate call value (two methods)
c = round(p - x * math.exp(-r * t) + s_true,2)
c_2 = round(s_true * norm.cdf(d_1) - x * math.exp(-r * t) * norm.cdf(d_2),2)


#Step5 print result
print(" ")
print("Calculation")
print("D: " + str(D))
print("d1: " + str(round(d_1,3)))
print("d2: " + str(round(d_2,3)))

print(" ")
print("Output")
print('Call Value: ' + str(c))	
print('Put Value: ' + str(p))



















