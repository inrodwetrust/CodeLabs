# this was entered with "pip install py-money" into Powershell first
from money.money import Money
from money.currency import Currency
import math

# variables
wall_area = float(input("Enter the height of the wall in feet: ")) * float(input("Enter the width of the wall in feet: "))
gallon_price_raw = float(input("How much does a gallon of paint cost?: $"))
# define gallon price in currency
gallon_price = Money(gallon_price_raw, Currency.USD)
coats = int(input("How many coats of paint will the wall need?: "))
gallon_area = 400

gallons_needed_raw = (wall_area / gallon_area)
# round up to the nearest integer
gallons_needed = math.ceil(gallons_needed_raw)
print("Buy", (gallons_needed), "gallon(s) of paint.")

wall_price = gallons_needed * gallon_price * coats
print("The total cost to paint the wall is:$",wall_price)
