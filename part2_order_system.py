# ============================================
# Part 2: Order System using Data Structures
# Demonstrates dictionary, list, tuple, loops,
# and conditional logic
# ============================================

print("Welcome to the Food Order System")

# Dictionary to store menu items and prices
menu = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 200,
    "Coffee": 100
}

# Display available menu items
print("\nMenu:")
for item, price in menu.items():
    print(f"{item} - ₹{price}")

# List to store items ordered by the user
orders = []

# Take user input until 'done' is entered
while True:
    choice = input("\nEnter item name (or 'done' to finish): ").title()

    # Exit loop if user is done ordering
    if choice == "Done":
        break

    # Check if selected item exists in the menu
    if choice in menu:
        orders.append(choice)
        print(f"{choice} added to your order.")
    else:
        print("Item not available.")

# Calculate total order cost
total = 0
for item in orders:
    total += menu[item]

# Display order summary
print("\nOrder Summary:")
for item in orders:
    print(f"{item} - ₹{menu[item]}")

print("Total Amount: ₹", total)

# Tuple for fixed tax rate (immutable data)
tax_rate = (0.05,)  # 5% GST

# Calculate tax and final amount
gst = total * tax_rate[0]
final_amount = total + gst

print("GST (5%): ₹", round(gst, 2))
print("Final Amount: ₹", round(final_amount, 2))
