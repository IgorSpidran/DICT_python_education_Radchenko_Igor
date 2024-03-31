class CoffeeMachine:
    def __init__(self):
        self.state = "choosing_action"
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def process_input(self, user_input):
        if self.state == "choosing_action":
            self.process_action(user_input)
        elif self.state == "buying_coffee":
            self.process_buy(user_input)
        elif self.state == "filling_machine":
            self.process_fill(user_input)
        elif self.state == "taking_money":
            self.take_money()
            self.state = "choosing_action"
        elif self.state == "exit":
            return

    def process_action(self, action):
        if action == "buy":
            self.state = "buying_coffee"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
        elif action == "fill":
            self.state = "filling_machine"
            print("Write how many ml of water do you want to add:")
        elif action == "take":
            self.state = "taking_money"
            self.take_money()
        elif action == "remaining":
            self.display_status()
        elif action == "exit":
            self.state = "exit"
        else:
            print("Invalid action!")

    def process_buy(self, choice):
        if choice == "back":
            self.state = "choosing_action"
            return
        choice = int(choice)
        if choice in [1, 2, 3]:
            self.buy_coffee(choice)
            self.state = "choosing_action"
        else:
            print("Invalid choice!")

    def process_fill(self, amount):
        if self.state == "filling_machine":
            if amount.isdigit():
                self.fill_machine(int(amount))
                self.state = "filling_machine_milk"
                print("Write how many ml of milk do you want to add:")
            else:
                print("Invalid input!")

    def process_fill(self, amount):
        if self.state == "filling_machine_milk":
            if amount.isdigit():
                self.fill_machine_milk(int(amount))
                self.state = "filling_machine_coffee_beans"
                print("Write how many grams of coffee beans do you want to add:")
            else:
                print("Invalid input!")

    def process_fill(self, amount):
        if self.state == "filling_machine_coffee_beans":
            if amount.isdigit():
                self.fill_machine_coffee_beans(int(amount))
                self.state = "filling_machine_disposable_cups"
                print("Write how many disposable cups of coffee do you want to add:")
            else:
                print("Invalid input!")

    def process_fill(self, amount):
        if self.state == "filling_machine_disposable_cups":
            if amount.isdigit():
                self.fill_machine_disposable_cups(int(amount))
                self.state = "choosing_action"
            else:
                print("Invalid input!")

    def buy_coffee(self, choice):
        if choice == 1:  # espresso
            if self.water < 250 or self.coffee_beans < 16 or self.disposable_cups < 1:
                print("Sorry, not enough resources!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
        elif choice == 2:  # latte
            if self.water < 350 or self.milk < 75 or self.coffee_beans < 20 or self.disposable_cups < 1:
                print("Sorry, not enough resources!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
        elif choice == 3:  # cappuccino
            if self.water < 200 or self.milk < 100 or self.coffee_beans < 12 or self.disposable_cups < 1:
                print("Sorry, not enough resources!")
                return
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6
        self.disposable_cups -= 1

    def fill_machine(self, amount):
        self.water += amount
        print("Write how many ml of milk do you want to add:")
        self.state = "filling_machine_milk"

    def fill_machine_milk(self, amount):
        self.milk += amount
        print("Write how many grams of coffee beans do you want to add:")
        self.state = "filling_machine_coffee_beans"

    def fill_machine_coffee_beans(self, amount):
        self.coffee_beans += amount
        print("Write how many disposable cups of coffee do you want to add:")
        self.state = "filling_machine_disposable_cups"

    def fill_machine_disposable_cups(self, amount):
        self.disposable_cups += amount
        self.state = "choosing_action"

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def display_status(self):
        print(f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
${self.money} of money
        """)


def main():
    coffee_machine = CoffeeMachine()

    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        coffee_machine.process_input(action)

if __name__ == "__main__":
    main()
