massage = """

**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************

"""
print(massage)

meals = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]
requests = {item:0 for item in meals}

while True:
    order = input("> ")

    if order in meals:
        requests[order] += 1
        print(f"\n** {requests[order]} order of {order} have been added to your meal **\n")
    elif order == "quit":
        break
    elif order == "meal":
        for j in [f"{option}: {number}" for option,number in requests.meals() if number!=0]:
            print(j)
    else:
        print(f"\"{order}\" isn't something that's on the menu\n")
        while True:
            choice = input("Is there anything else you'd want to order? (y/n) : ")
            if (choice == "y") or (choice == "n"):
                break
            else:
                print("Please make your choice \"y\" or \"n\"\n")
        if choice == "n":
            break

