menu = {
    'pizza': 40,
    'burger': 60,
    'pasta': 50,
    'salad': 20,
    'coffee': 80
}

print("Welcome to PYTHON Restaurant!")
print("Pizza: Rs.40\nBurger: Rs.60\nPasta: Rs.50\nSalad: Rs.20\nCoffee: Rs.80")

order_total = 0
items_ordered = []

while True:
    item = input("\nEnter the name of item you want to order: ").strip().lower()
    
    if item in menu:
        order_total += menu[item]
        items_ordered.append(item.capitalize())
        print(f"Your item {item.capitalize()} (Rs.{menu[item]}) has been added to your order")
    else:
        print(f"Sorry, {item} is not available!")

    another_order = input("Do you want to order another item? (yes/no): ").strip().lower()
    
    if another_order != "yes":
        break

if items_ordered:
    print(f"\n--- Order Summary ---")
    print(f"Items: {', '.join(items_ordered)}")
    print(f"Total amount to pay: Rs.{order_total}")
else:
    print("\nNo items ordered. Thank you for visiting!")