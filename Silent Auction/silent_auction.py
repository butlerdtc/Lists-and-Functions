""" Silent Auction - V1 """


# Function to check if numbers are entered and then run error control if not
def number_checker(question):
    error = "\nSorry, you must enter a valid number\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


# Statement formatter
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Function of main menu to run other functions
def menu():
    print(formatter("*", "Robson's Silent Auction"))
    bidding()
    print("Goodbye")


# Function to ask for item to sell
def item():
    auction_item = input("What item would you like to add to the bidding: ")
    return auction_item


# Function to ask for reserve price
def reserve():
    price = number_checker("What would you like the reserve price to be: ")
    return price


# Function to ask for a bid then check if its higher and print outcome
def bidding():
    auction_item = item()
    cost = reserve()
    bid = 0
    print("The auction has started!")
    print("Please enter '-1' to exit the auction")
    print()
    while True:
        print(f"Highest bid currently is {bid}")
        new_bid = float(input("What is your bid: "))
        if new_bid < 0:
            break
        elif new_bid > bid:
            bid = new_bid
        else:
            print("Please enter higher bid")
    if bid >= cost:
        print(f"The {auction_item} sold for {bid}")
    else:
        print(f"The {auction_item} did not sell")


# Main Routine
menu()
