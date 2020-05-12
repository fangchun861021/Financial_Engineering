
import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np

#Step1: Input

print("Input")
s_0 = float(input("Stock price: "))
strike = float(input("Strike price: "))
sigma_stock = float(input("Stock Volatility: "))
r = float(input("Risk free rate: "))

print("")
a = float(input("a in Hull-White model: "))
sigma = float(input("sigma in Hull-White model: "))
fr = float(input("Forward rate: "))
length = float(input("Maturity(year): "))
timestep = int(input("timestep: "))
dt = float(input("dt: "))

today = ql.Date(12,5,2020)
day_count = ql.Thirty360()


#Step2: Monte Carlo simulation for short rate
ql.Settings.instance().evaluationDate = today

spot_curve = ql.FlatForward(today, ql.QuoteHandle(ql.SimpleQuote(fr)), day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)

hw_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(timestep, ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process, length, timestep, rng, False)

def generate_paths(num_paths, timestep):
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr
	
num_paths = 100
time, paths = generate_paths(num_paths, timestep)
for i in range(num_paths):
    plt.plot(time, paths[i, :], lw=0.8, alpha=0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()


#Step3: apply GBM for stock price
def genBrownPath (T, mu, sigma_stock, s_0, dt):
	W = [0] + np.random.standard_normal(size = 1) 
	W = (W + np.random.standard_normal(size = 1))*dt**(1/2)

	stock = []
	for i in range (timestep + 1):
		X = (mu[i]-0.5*sigma_stock**2)*time[i] + sigma_stock*W 
		S = s_0*np.exp(X) 
		stock.append(S)
	plt.plot(stock)
	plt.title("Stock Price Simulation")
	return np.array(stock)

stockprice = []
for i in range(num_paths):
	stockprice.append(genBrownPath(timestep, paths[i, :], sigma_stock, s_0, dt))
plt.title("Stock Price Simulation")
plt.show()

s_last = []		#stock price for last period
for i in range(num_paths):	
	sl = stockprice[i][-1]
	s_last.append(sl)


#Step4: Calculate average payoff and discount for call/put price
c = []
for i in range(num_paths): #each payoff for call option
	c.append(max(s_last[i] - strike, 0))
c_avg = np.sum(c) / num_paths
call_price = c_avg * np.exp(-timestep * r)

p = []
for i in range(num_paths): #each payoff for put option
	p.append(strike - max(s_last[i], 0))
p_avg = np.sum(p) / num_paths
put_price = p_avg * np.exp(-timestep * r)


#Step5: Output
print(" ")
print("Output")
print('Call Price: ' + str(call_price))	
print('Put Price: ' + str(put_price))






