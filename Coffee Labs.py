print("Hello there, what's your name")
name = input()

print("Hi " + name + ", Welcome to Coffee Labs, here is a menu of all the coffee you can have")

menu = "Latte 5$, Hot Chocolate 5$, Black Coffee 5$, Cappucino 5$, Espresso 5$\n"

print("Menu:", menu)
print("What's your order " + name)

order = input()
price = 5
quantity = input("How Many " + order + " would you like?\n")
total = price * int(quantity)
print("Great, your total is in the total.txt and enjoy!")


response = open('total.txt', 'w')

response.write("Great, your total is: $" + str(total))
response.write(" ,Thank you, " + name + ", your " + quantity + " " + order + "/s will come out in just a few minutes")
response.close()