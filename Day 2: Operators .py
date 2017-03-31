meal_cost = float (input())
tax_percent = input()
tip_percent = input()

tip = meal_cost * tip_percent *0.01

tax = meal_cost * tax_percent * 0.01

total_cost = (meal_cost + tip + tax) 

cost = int(round(total_cost))

print("The total meal cost is " + str(cost) + " dollars.")
