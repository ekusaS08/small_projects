from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
# resources = {
#     "water": 0,
#     "milk": 5,
#     "coffee": 10,
#     "money": 0
# }
accepted_coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}

# functions
def print_report(resource_dict):
    for key in resource_dict:
        print(f"{key}: {resource_dict[key]}")

def check_suff_resources( coffee :str, menu: dict, resource_dict) -> bool:
    sufficient = True
    recipe = menu[coffee]["ingredients"]
    for ingredient in recipe:
        if recipe[ingredient] > resource_dict[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            sufficient = False
    return sufficient

def receive_payment(coin_dict) -> float:
    print("Please insert coins.")
    total_payment = 0
    for coin in coin_dict:
        total_payment += int(input(f"How many {coin}?: "))*coin_dict[coin]
    return total_payment

def calculate_change(given_money, coffee, menu):
    return given_money - menu[coffee]["cost"]

def make_coffe(coffee:str, menu:dict, resource_dict):
    ingredients = menu[coffee]["ingredients"]
    price = menu[coffee]["cost"]
    for ingredient in ingredients:
        resource_dict[ingredient]-= ingredients[ingredient]
    resource_dict["money"] += price




# body
on = True
available_coffee = ""
for key in MENU:
    available_coffee += f"{key}/"
available_coffee = available_coffee[:-1]
while on:
    selection = input( f"What would you like? {available_coffee}: ").lower()
    if selection == "off":
        on = False
    elif selection == "report":
        print_report(resources)
    else:
        if check_suff_resources(selection,MENU,resources):
            received_money = receive_payment(accepted_coins)
            change = round(calculate_change(received_money, selection, MENU),2)
            if change >= 0:
                make_coffe(selection,MENU,resources)
                print(f"Here is ${change} in change.")
                print(f"Here is your {selection}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")



