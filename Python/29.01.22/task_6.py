#!/bin/python3

price_list = {"tomato": "2,5$", "cucumber": "3$", "potato": "1,5$", "onion": "1,2$", "garlic": "1$", "carrot": "1,4$", "celery": "1,3", "pumpkin": "2$", "eggplant": "1,7$", "cabbage": "1,1$"}
print("Welcome to our vegetable shop!!!\nWe sell tomatoes, cucumbers, potatoes, onions, garlic, carrots, celery, eggplants, cabbages and pumpkins\n")
print("if you want go out enter 'bye'")
while True:
    name = input("price of which product you want to know: ")
    if name.lower() == "bye":
        print("Goodbye, come back again")
        break
    if name == "":
        print("Choose something, we have everything fresh\n")
        continue
    for k in price_list:
        if k == name.lower():
            print("the price of a", k, "per kilogram is", price_list[k],"\n")
            break
    else:
        print("we do not have such a product, or you spelled its name incorrectly\n")
