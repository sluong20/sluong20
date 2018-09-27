brownies_cost = 1 #$
cookies_cost = 1.50 #$
muffins_cost = 2
brownies_expense = .75
cookies_expense = 1
muffins_expense = 1.5
total_expense = 10 * (brownies_expense + cookies_expense + muffins_expense)
total_money = 15 * (brownies_cost + cookies_cost + muffins_cost)
tips = total_money * .2
total_profit = total_money + tips - total_expense

print("school bake sale!")
print("brownies cost "+str(brownies_cost))
print("cookies cost "+str(cookies_cost))
print("muffins cost "+str(muffins_cost))
print("we had some expenses though. For ten of each of these goods, we paid "+str(total_expense))
print("however, today we made "+str(total_money))
print("we also made "+str(tips)+" in tips")
print("our total profit at the bake sale was "+str(total_profit))
