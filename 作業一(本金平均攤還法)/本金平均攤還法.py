from prettytable import PrettyTable

p = int(input("請輸入本金: "))
t = int(input("請輸入期數: "))
r = int(input("請輸入年利率(%): "))
r = r / 100

p_back = int(p / (t * 12)) + 1 #平均每月攤還本金(無條件進位)
p_owe = p
sumPI = 0

x = PrettyTable()
x.field_names = ["期數", "本金(元)", "利息(元)", "本金利息累計(元)"]

for i in range(1, t * 12):
	interest = round(p_owe * r / 12) #每期償還利息 (四捨五入)
	sumPI += p_back + interest #已償還本金利息累計
	p_owe -= p_back #尚欠本金
	x.add_row(["第" + str(i) + "期", p_back, interest, sumPI])
	
#最後一期(last)
p_back_last = p_owe
interest_last = round(p_back_last * r / 12)
sumPI += p_back_last + interest_last
x.add_row(["第" + str(t * 12) + "期", p_back_last, interest_last, sumPI])


print(x)