def greet():
    print("Welcome to the art store, customer.")
greet()

price = 51
supplies = int(input("Enter number of items: "))

def cost():
    print("$", price*supplies, "is your cost.")
    change = int(input("Enter payment: "))
    
    if change > price*supplies:
        ordecision = input("Would you like to change or tip?")
        if ordecision == "change":
            print("Your change is $", change - price*supplies)
            print()
            print()
        elif ordecision == "tip":
            print("Thank you for the extra tip!")
            print()
            print()
            
    elif change == price*supplies:
        print("Thank you!")
        print()
        print()
        
    elif change < price*supplies:
        print("Insufficient payment, please pay more.")
        print()
        print()
cost()

def reciept():
    print("RECIEPT/BILL")
    print("Total cost: ", "$", price*supplies)
    print("Total supplies bought: ", supplies)
    print("Thanky you for buying fom us!")
reciept()