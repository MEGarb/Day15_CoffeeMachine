def generate_report(res):
    print(f"\nWater:   {res.get('water')}ml")
    print(f"Milk:    {res.get('milk')}ml")
    print(f"Coffee:  {res.get('coffee')}g")
    print(f"Money:  ${'{:.2f}'.format(round(res.get('money'), 2))}\n")


def adjust_resources(selection, res):
    res["water"] -= MENU[selection]["ingredients"]["water"]
    res["milk"] -= MENU[selection]["ingredients"]["milk"]
    res["coffee"] -= MENU[selection]["ingredients"]["coffee"]


def make_coffee(selection, res):
    if selection_available(selection, res):
        if process_payment(MENU[selection]["cost"], res):
            adjust_resources(selection, res)
            print(f"Dispensing your {selection}.  Enjoy!\n")
    else:
        print("Selection unavailable due to one or more ingredients out of stock.\n")


def selection_available(selection, res):
    return MENU[selection]["ingredients"]["water"] <= res["water"] and MENU[selection]["ingredients"]["milk"] <= \
            res["milk"] and MENU[selection]["ingredients"]["coffee"] <= res["coffee"]


def process_payment(price, res):
    print("\nPlease enter your payment.")
    num_q = int(input("Quarters:  "))
    num_d = int(input("Dimes:  "))
    num_n = int(input("Nickles:  "))
    num_p = int(input("Pennies:  "))
    total_paid = (num_q * .25) + (num_d * .10) + (num_n * .05) + (num_p * .01)

    if total_paid > price:
        print(f"\nYour change is ${'{:.2f}'.format(round(total_paid - price, 2))}")
        res["money"] += price
        return True
    elif total_paid == price:
        print("\nPayment accepted.  Thank you.")
        res["money"] += price
        return True
    else:
        print("\nInsufficient funds.  Payment returned.")
        return False


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

machine_power = True
while machine_power:

    user_input = input("\nWhat would you like? (espresso/latte/cappuccino):  ").lower()

    if user_input == "off":
        machine_power = False
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        make_coffee(user_input, resources)
    elif user_input == "report":
        generate_report(resources)
