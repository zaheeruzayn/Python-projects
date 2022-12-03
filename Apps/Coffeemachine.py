MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

game_on=True

def reduce_items(resources, ingredients):
    '''takes ingredients from resources and returns the resources'''
    for items in ingredients:
        resources[items]-=ingredients[items]
    return resources

def collect_money():
    '''collects money and returns in dollars'''
    penny = int(input("How many pennies?: "))
    dime = int(input("How many dime?: "))
    nickel = int(input("How many nickel?: "))
    quarter = int(input("How many quarter?: "))
    money_in_dollar = (penny*.01)+(dime*.05)+(nickel*.1)+(quarter*.25)
    
    return round(money_in_dollar,2)

def check_ingredients(resources, coffee_ingredients):
    '''checks if ingredients are enough to make chosen coffee flavour'''
    for item in resources:
        if resources[item] < coffee_ingredients[item]:
            print(f"Not enough {item}")
            return True
        else:
            return False

def report (resources,profit):
    '''reports the remaining resources'''
    for item in resources:
        print(f"{item} : {resources[item]} ")
    print (f"money ${profit}")

def return_coffee(balance,coffee):
    print(f"Here's your {coffee} and change ${round(balance,2)}. ")

while game_on:
    choice =input("what would you like?(cappuccino, latte, espresso) or \n input report for report on ingredients: ")

    if choice =='report':
        report(resources,profit)
    elif choice =='off':
        game_on == False
    else:
        coffee_ingredients = MENU[choice]['ingredients']
    
        not_enough_ingredients = check_ingredients(resources, coffee_ingredients)
        
        if not_enough_ingredients:
           continue

        money_given = collect_money()

        resources = reduce_items(resources, coffee_ingredients)

        profit=profit+MENU[choice]['cost']
        
        balance = money_given - MENU[choice]['cost']

        return_coffee(balance, choice)

    