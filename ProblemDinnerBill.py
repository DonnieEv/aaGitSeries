# start of file

order = []

def rorder():
    name = input("Person is: ")
    item = input("Item is: ")
    item_price = float(input("Item price is: "))
    drink = input("Drink is: ")
    drink_price = float(input("Drink price is: " ))
    total = item_price + drink_price
    tax = total * 0.13
    order_total = total + tax  

    order.append({
        "Name": name,
        "Item": item,
        "Item Price": item_price,
        "Drink": drink,
        "Drink price": drink_price,
        "Total": total,
        "Tax": tax,
        "Order Total": order_total
    })

while True:
    rorder()
    another = input("Add another order? (y/n): ")
    if another.lower() != "y":
        break

for person in order:
    tip_percent = float(input(f"Tip % for {person['Name']}: "))
    tip = person['Total'] * (tip_percent / 100)
    person['Tip'] = tip                                    # update tip
    person['Order Total'] = person['Order Total'] + tip 

grand_total = sum(p['Order Total'] for p in order)

for person in order:
    print(f"{person['Name']:<12} Subtotal=${person['Total']:<8.2f} Tax=${person['Tax']:<7.2f} Tip=${person['Tip']:<7.2f} Total=${person['Order Total']:<7.2f}")


print(f"Total:   ${grand_total:.2f}")