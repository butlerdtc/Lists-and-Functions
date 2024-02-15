""" Silent Auction - V1 """


def number_checker(question):
    error = "\nSorry, you must enter a valid number\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


def menu():
    print(formatter("*", "Robson's Silent Auction"))
    item()
    reserve()


def item():
    auction_item = input("What item would you like to add to the bidding: ")
    return auction_item


def reserve():
    price = number_checker(float(input("What would you like the reserve "
                                       "price to be: ")))
    return price


# Main Routine
menu()
