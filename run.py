import vending
from summary_print import summary_printing

wallet = balance = 0

# Final calculations
def calculate(result):
        total_spent = ((vending.Lays*5) + (vending.Minute_Maid*10) + (vending.Dairy_Milk*20))
        summary_printing(vending.Lays, vending.Minute_Maid, vending.Dairy_Milk, total_spent, result)

# Calling the main functions
coins = vending.user_input(balance)
try:
    if coins == 'EXIT':
        result = 0
        calculate(result)
    else:
        result = vending.buy(coins)
        calculate(result)
finally:
    pass
