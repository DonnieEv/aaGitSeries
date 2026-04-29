cart = []


def get_choice():
    choice = int(input("""
                       Next Step: 
                       1. Add item
                       2. Remove item
                       3. View Cart
                       4. View Total
                       5. View Categories
                       6. Quit
                       : """))
    return choice


def add_item():
    item = input("Choose item: ")
    price = float(input("Enter price: "))
    category = input("Enter Category: ")
    cart.append({"Item": item, "Price": price, "Category": category})
    print(f"Added {item} to cart!")

def remove_item():
    name = input("Item to remove: ")
    original_length = len(cart)
    cart[:] = [item for item in cart if item["Item"] != name]
    if len(cart) == original_length:
        print(f"'{name}' wasn't found in the cart.")
    else:
        print(f"Removed {name} from cart.")

def view_cart():
    if not cart:
        print("Your cart is empty!")
        return
    for item in cart:
        print(f" - {item['Item']} ({item['Category']}) : ${item['Price']:.2f}")

def view_total():
    total = sum(item["Price"] for item in cart)
    print(f"Your total is ${total:.2f}")

def view_categories():
    categories = set()
    for item in cart:
        categories.add(item["Category"])
    if not categories:
        print("No categories yet.")
    else:
        print("Categories:", categories)    

while True:
    choice = get_choice()
    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        view_cart()
    elif choice == 4:
        view_total()
    elif choice == 5:
        view_categories()
    elif choice == 6:
        break
