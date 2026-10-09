small = 8
large = 12
toppings = 1
deliv_5 = 2
add_deliv = 1

# input data
pizza = str(input("Enter the size of pizza (small/large): "))
toppings = int(input("Enter the number of toppings: "))
dist = int(input("Enter the distance in km: "))

#toppings cost
if pizza == "small":
    small_cost = small + (toppings * 1)
    if dist <= 5 and dist > 0:
        print(f"The total cost of the pizza is: ${small_cost} and the delivery cost is: ${deliv_5}")
    elif dist > 5:
        rem = dist - 5
        total_delivery_cost = deliv_5 + (rem * add_deliv)
        print(f"The total cost of the pizza is: ${small_cost} and the delivery cost is: ${total_delivery_cost}")
    elif dist == 0:
        print(f"The total cost of the pizza is: ${small_cost} and there is no delivery cost.")
elif pizza == "large":
    large_cost = large + (toppings * 1)
    if dist <= 5 and dist > 0:
        print(f"The total cost of the pizza is: ${large_cost} and the delivery cost is: ${deliv_5}")
    elif dist > 5:
        rem = dist - 5
        total_delivery_cost = deliv_5 + (rem * add_deliv)
        print(f"The total cost of the pizza is: ${large_cost} and the delivery cost is: ${total_delivery_cost}")
    elif dist == 0:
        print(f"The total cost of the pizza is: ${large_cost} and there is no delivery cost.")
else:
    print("Invalid pizza size. Please enter 'small' or 'large'.")
