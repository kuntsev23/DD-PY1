money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
grow = 1.05
d = salary - spend
while money_capital + d >=spend :
    money_capital += d
    spend = spend * grow
    month += 1


print(month)
