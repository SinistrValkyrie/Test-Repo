"""The coffee shop module contains functions and variables important to implementing a coffee shop.
"""

# set some variables
shop_name = "Valkyrie Brew House"
coffee_sizes = ["small", "medium", "large"]
coffee_roasts = ["hot chocolate", "light roast", "medium roast", "dark roast", "espresso"]
milk_type = ["whole", "2%", "skim", "almond", "oat", "coconut"]
def order_coffee(size, roast):
    """Function to order a coffee from a user
    :parameter size: a string containing one of the coffee_sizes
    :parameter roast: a string containing one of the coffee_roasts
    :return: a message about the coffee order
    """
    return "Here's your {} coffee roasted {}!".format(size, roast)

def add_milk_please(milk_type):
    """
    Pretend we're adding milk to the coffee
    :parameter fat_content: a string or integer containing the milkfat content
    :return: a message about having added the milk
    """
    return "I've added the {} milk".format(milk_type)

def give_tip(tip_amount):
    """
    Take tip from the user, then be happy about it
    :parameter tip_amount: the tip amount
    :return: nothing
    """
    print("Thank you so much! We don't make a ton of money.")
