amount = int(input("How many products you like? "))

total = float(0.00)

for side in range(amount):

        product = str(input("Product: "))
        price = float(input("Price: $"))

        print(product + " $" + str(price))

        total = total + price

print("Your total is " + " $" + str(total))