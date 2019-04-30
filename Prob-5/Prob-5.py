# Module 2
#   Programming Assignment 3
#     Prob-5.py

# Trevor Bromley

def main():
    slice = 2.0
    largeDrink = 1.5
    donut = .56
    sum = 0
    print("Pizza @ 2:\t", slice * 2)
    sum = slice * 2
    print("Drink:\t\t", largeDrink)
    sum = sum + largeDrink
    print("Donut @ 2:\t", donut * 2)
    sum = sum + donut

    print("---------")

    tax = .56
    print("Tax:\t\t", tax)
    sum = sum + tax
    print("\nTotal:\t\t", sum)
    
    print()
    tendered = eval(input("Please enter an amount: "))
    print("Tendered:\t{0:.2f} xyz {1:.2f}".format(tendered, sum))
    change = tendered - sum
    print("Change:\t\t{0:.2f}".format(change))
    
main()

