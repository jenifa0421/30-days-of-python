class CoffeeMachine:
    water = 300
    milk = 400
    coffee = 150
    money = 0

    def __init__(self, opt):
        self.value = opt

    def report(self, opt):
        print("Water:", self.water, "ml\nMilk:", self.milk, "ml\nCoffee:", self.coffee, "g\nMoney:$", self.money)

    def makecoffee(self, opt):
        if (opt == "latte"):
            self.water = self.water - 50
            self.milk = self.milk - 70
            self.coffee = self.coffee - 50
            self.money = self.money + 2.50
            print("Here is your latte. Enjoy!")
        elif (opt == "espresso"):
            self.water = self.water - 100
            self.milk = self.milk - 10
            self.coffee = self.coffee - 100
            self.money = self.money + 3.50
            print("Here is your espresso. Enjoy!")
        else:
            self.water = self.water - 70
            self.milk = self.milk - 50
            self.coffee = self.coffee - 70
            self.money = self.money + 4.50
            print("Here is your cappucino. Enjoy!")

    def makeTransaction(self, opt, amt):
        if (opt == "latte"):
            if (amt < 2.50):
                print("Sorry that's not enough money. Money refunded.")
            elif (amt > 2.50):
                print("Here is $", round(amt - 2.50, 2), "dollars in change.")
                self.makecoffee(opt)
            else:
                self.makecoffee(opt)
        elif (opt == "espresso"):
            if (amt < 3.50):
                print("Sorry that's not enough money. Money refunded.")
            elif (amt > 3.50):
                print("Here is $", round(amt - 3.50, 2), "dollars in change.")
                self.makecoffee(opt)
            else:
                self.makecoffee(opt)
        else:
            if (amt < 4.50):
                print("Sorry that's not enough money. Money refunded.")
            elif (amt > 4.50):
                print("Here is $", round(amt - 4.50, 2), "dollars in change.")
                self.makecoffee(opt)
            else:
                self.makecoffee(opt)

    def makeCoins(self, opt):
        quarters = 0.25
        dimes = 0.10
        nickles = 0.05
        pennies = 0.01
        print("Insert coins!")
        q = int(input("Enter number of quarters:"))
        d = int(input("Enter number of dimes:"))
        n = int(input("Enter number of nickles:"))
        p = int(input("Enter number of pennies:"))
        amt = (q * quarters) + (d * dimes) + (n * nickles) + (p * pennies)
        self.makeTransaction(opt, amt)

    def hasIngridients(self, opt):
        if (opt== "latte"):
            if (self.water < 50):
                print("Sorry there is not enough water!")
            elif (self.milk < 70):
                print("Sorry there is not enough milk!")
            elif (self.coffee < 50):
                print("Sorry there is not enough coffee!")
            else:
                self.makeCoins(opt)
        elif (opt== "espresso"):
            if (self.water < 100):
                print("Sorry there is not enough water!")
            elif (self.milk < 10):
                print("Sorry there is not enough milk!")
            elif (self.coffee < 100):
                print("Sorry there is not enough coffee!")
            else:
                self.makeCoins(opt)
        else:
            if (self.water < 70):
                print("Sorry there is not enough water!")
            elif (self.milk < 50):
                print("Sorry there is not enough milk!")
            elif (self.coffee < 70):
                print("Sorry there is not enough coffee!")
            else:
                self.makeCoins(opt)

x = "on"
Machine = CoffeeMachine(x)
while (True):
    print("\n\nLatte:$2.50\nEspresso:$3.50\nCappucino:$4.50")
    x = input("What would you like?(espresso/latte/cappucino):")
    if (x == "off"):
        break
    if (x == "report"):
        Machine.report(x)
        continue
    Machine.hasIngridients(x)


OUTPUT:

C:\Users\Home\PycharmProjects\Coffee_Machine\venv\Scripts\python.exe C:/Users/Home/PycharmProjects/Coffee_Machine/main.py


Latte:$2.50
Espresso:$3.50
Cappucino:$4.50
What would you like?(espresso/latte/cappucino):1
Insert coins!
Enter number of quarters:90
Enter number of dimes:90
Enter number of nickles:90
Enter number of pennies:90
Here is $ 32.4 dollars in change.
Here is your cappucino. Enjoy!


Latte:$2.50
Espresso:$3.50
Cappucino:$4.50
What would you like?(espresso/latte/cappucino):report
Water: 230 ml
Milk: 350 ml
Coffee: 80 g
Money:$ 4.5


Latte:$2.50
Espresso:$3.50
Cappucino:$4.50
What would you like?(espresso/latte/cappucino):3
Insert coins!
Enter number of quarters:90
Enter number of dimes:0
Enter number of nickles:90
Enter number of pennies:90
Here is $ 23.4 dollars in change.
Here is your cappucino. Enjoy!


Latte:$2.50
Espresso:$3.50
Cappucino:$4.50
What would you like?(espresso/latte/cappucino):2
Sorry there is not enough coffee!



Latte:$2.50
Espresso:$3.50
Cappucino:$4.50
What would you like?(espresso/latte/cappucino):off

Process finished with exit code 0
