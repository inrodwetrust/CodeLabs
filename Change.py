cost = float(input("Enter the cost in cents of the product you're buying: $0."))
amount_tendered = float(input("Enter the amount tendered: $0."))
if cost > amount_tendered:
    print("This is not enough money to buy this product.")
    end()
elif cost < amount_tendered:
    quarters = int(amount_tendered - cost) // 25
    dimes = int(amount_tendered - cost) % 25 // 10
    nickels = int(amount_tendered - cost) % 25 % 10 // 5
    pennies = int(amount_tendered - cost) % 25 % 10 % 5 // 1

print("Total change will be", amount_tendered - cost, "cents.")
print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickels: ", nickels)
print("Pennies: ", pennies)
