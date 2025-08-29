# import the module with coffee_shop functionality
import coffee_shop

# Output the info we know from the module
print("Welcome to", coffee_shop.shop_name)
print("Available sizes:", coffee_shop.coffee_sizes)
print("Available roasts:", coffee_shop.coffee_roasts)
print("Available milk types:", coffee_shop.milk_type)

# Get some inputs from the user
order_size = input("What size coffee would you like?")
order_roast = input("What roast would you like?")

# Send the order to the coffee_shop module
shop_says = coffee_shop.order_coffee(order_size, order_roast)
# Print whatever it gives back
print(shop_says)

# See if the user wants to add milk
add_milk_response = input("Would you like to add milk? (y/n)")
# Convert the response to lowercase, then check for a "yes" answer
if "y" in add_milk_response.lower():
    milk_fat = input("What kind of milk would you like?")
    shop_says = coffee_shop.add_milk_please(milk_fat)
    # Print out whatever it gives back
    print(shop_says)

# They better give a tip...
print("THAT'S GOOD COFFEE! Very good. Your brain is working again.")
print("You better give a tip.")
tip_amount = input("Tip amount?")
coffee_shop.give_tip(tip_amount)
