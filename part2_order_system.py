print("Welcome to the Food Order System")

menu = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 200,
    "Coffee": 100
}

print("\nMenu:")
for item, price in menu.items():
    print(f"{item} - ₹{price}")


orders = []

while True:
    choice = input("\nEnter item name (or 'done' to finish): ").title()

    if choice == "Done":
        break

    if choice in menu:
        orders.append(choice)
        print(f"{choice} added to your order.")
    else:
        print("Item not available.")



total = 0

for item in orders:
    total += menu[item]

print("\nOrder Summary:")
for item in orders:
    print(item, "-", menu[item])

print("Total Amount: ₹", total)




tax_rates = (0.05,)  # 5% GST

gst = total * tax_rates[0]
final_amount = total + gst

print("GST (5%): ₹", round(gst, 2))
print("Final Amount: ₹", round(final_amount, 2))




  