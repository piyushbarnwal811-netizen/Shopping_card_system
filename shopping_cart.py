# shopping_cart.py
"""
Rungta International Skills University
School of Computer Science and Engineering
Bachelor of Technology Computer Science and Engineering
PS No. 4: Shopping Cart System

Concepts Used: Lists, Dictionaries, Functions, Billing
"""

# ---------------------------------------------------------
# 1. Product Catalogue (Dictionary Requirement)
# ---------------------------------------------------------
CATALOGUE = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500
}

GST_RATE = 0.18        # 18% GST
DISCOUNT_RATE = 0.10   # 10% discount
DISCOUNT_THRESHOLD = 500  # Discount if subtotal > 500


def format_num(val):
    """Format numbers cleanly: integer if whole number, else 2 decimal places."""
    if isinstance(val, (int, float)):
        return f"{int(val)}" if val == int(val) else f"{val:.2f}"
    return str(val)


def get_canonical_name(name):
    """Find the exact product name matching case-insensitively."""
    cleaned = str(name).strip().lower()
    for product in CATALOGUE:
        if product.lower() == cleaned:
            return product
    return None


def validate_product(product_name):
    """
    Validate product existence against the catalogue.
    Returns (True, canonical_name) or (False, error_message).
    """
    canonical = get_canonical_name(product_name)
    if canonical:
        return True, canonical
    available = ", ".join(CATALOGUE.keys())
    return False, f"Invalid product. Available: {available}"


def validate_quantity(quantity):
    """
    Validate that quantity is an integer and at least 1.
    Returns (True, int_quantity) or (False, error_message).
    """
    try:
        qty = int(quantity)
        if qty < 1:
            return False, "Quantity must be at least 1."
        return True, qty
    except (ValueError, TypeError):
        return False, "Quantity must be at least 1."


def calculate_subtotal(cart):
    """Calculate the subtotal of the cart."""
    subtotal = 0
    for item in cart:
        subtotal += item["price"] * item["quantity"]
    return subtotal


def add_to_cart(cart, product_name, quantity):
    """
    Add a product with given quantity to the cart.
    Validates product name and quantity.
    Returns (success_boolean, message).
    """
    valid_prod, prod_or_err = validate_product(product_name)
    if not valid_prod:
        return False, prod_or_err

    valid_qty, qty_or_err = validate_quantity(quantity)
    if not valid_qty:
        return False, qty_or_err

    canonical_name = prod_or_err
    qty = qty_or_err
    price = CATALOGUE[canonical_name]

    # Check if product is already in cart; update quantity if found
    for item in cart:
        if item["product"] == canonical_name:
            item["quantity"] += qty
            subtotal = calculate_subtotal(cart)
            return True, f"{canonical_name} x{qty} added | Cart subtotal: {format_num(subtotal)}"

    # Otherwise add new item to cart
    cart.append({
        "product": canonical_name,
        "price": price,
        "quantity": qty
    })
    subtotal = calculate_subtotal(cart)
    return True, f"{canonical_name} x{qty} added | Cart subtotal: {format_num(subtotal)}"


def remove_from_cart(cart, product_name, quantity=None):
    """
    Remove a product (or specified quantity) from the cart.
    Returns (success_boolean, message).
    """
    valid_prod, prod_or_err = validate_product(product_name)
    if not valid_prod:
        return False, prod_or_err

    canonical_name = prod_or_err

    found_index = -1
    for i, item in enumerate(cart):
        if item["product"] == canonical_name:
            found_index = i
            break

    if found_index == -1:
        return False, f"{canonical_name} is not in the cart."

    item = cart[found_index]
    if quantity is None or quantity >= item["quantity"]:
        cart.pop(found_index)
    else:
        item["quantity"] -= quantity

    # Build cart summary string for output: e.g. "Bag x2 = 1000"
    if cart:
        cart_summary_parts = []
        for it in cart:
            total_item_price = it["price"] * it["quantity"]
            cart_summary_parts.append(f"{it['product']} x{it['quantity']} = {format_num(total_item_price)}")
        cart_summary = ", ".join(cart_summary_parts)
        return True, f"{canonical_name} removed. Cart: {cart_summary}"
    else:
        return True, f"{canonical_name} removed. Cart is empty."


def view_products():
    """Display product catalogue."""
    print("\n--- Available Products ---")
    for prod, price in CATALOGUE.items():
        print(f"• {prod}: Rs. {format_num(price)}")
    print("--------------------------\n")


def view_cart(cart):
    """Display items currently in the cart."""
    if not cart:
        print("\nYour cart is empty.\n")
        return

    print("\n--- Current Cart ---")
    for item in cart:
        item_total = item["price"] * item["quantity"]
        print(f"• {item['product']} x{item['quantity']} @ Rs. {item['price']} = Rs. {format_num(item_total)}")
    subtotal = calculate_subtotal(cart)
    print(f"Subtotal: Rs. {format_num(subtotal)}")
    print("--------------------\n")


def calculate_bill(cart):
    """
    Calculate subtotal, discount, GST, and grand total.
    Returns a dict with all computed billing fields.
    """
    subtotal = calculate_subtotal(cart)
    # Discount: 10% if subtotal is strictly MORE THAN 500
    if subtotal > DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE
    else:
        discount = 0.0

    taxable_amount = subtotal - discount
    gst = taxable_amount * GST_RATE
    grand_total = taxable_amount + gst

    return {
        "subtotal": subtotal,
        "discount": discount,
        "taxable_amount": taxable_amount,
        "gst": gst,
        "grand_total": grand_total
    }


def checkout(cart):
    """
    Perform checkout, print final bill matching expected format,
    and return bill details.
    """
    if not cart:
        print("Cart is empty. Nothing to checkout.")
        return None

    bill = calculate_bill(cart)
    print(f"Subtotal: {format_num(bill['subtotal'])} | Discount: {format_num(bill['discount'])} | GST: {format_num(bill['gst'])}")
    print(f"Grand Total: {format_num(bill['grand_total'])}")
    return bill


def run_all_test_cases():
    """Run and display all 4 test cases specified in the project problem sheet."""
    print("=" * 60)
    print("RUNNING ALL 4 TEST CASES FROM PROJECT SPECIFICATION")
    print("=" * 60)

    # Test Case 1: Normal Input
    print("\n[Test Case 1: Normal Input]")
    print("Input: Add to cart: Notebook, Quantity: 2")
    cart1 = []
    success, msg = add_to_cart(cart1, "Notebook", 2)
    print("Actual Output  :", msg)
    print("Expected Output: Notebook x2 added | Cart subtotal: 100")
    assert msg == "Notebook x2 added | Cart subtotal: 100", "Test Case 1 Failed!"
    print(">>> STATUS: PASSED (MATCHED)")

    # Test Case 2: Boundary / Minimum Input
    print("\n[Test Case 2: Boundary / Minimum Input]")
    print("Input: Add to cart: Bag, Quantity: 1 -> Checkout")
    cart2 = []
    _, _ = add_to_cart(cart2, "Bag", 1)
    bill2 = calculate_bill(cart2)
    line1 = f"Subtotal: {format_num(bill2['subtotal'])} | Discount: {format_num(bill2['discount'])} | GST: {format_num(bill2['gst'])}"
    line2 = f"Grand Total: {format_num(bill2['grand_total'])}"
    print("Actual Output  :")
    print(line1)
    print(line2)
    print("Expected Output:")
    print("Subtotal: 500 | Discount: 0 | GST: 90")
    print("Grand Total: 590")
    assert line1 == "Subtotal: 500 | Discount: 0 | GST: 90", "Test Case 2 Line 1 Failed!"
    assert line2 == "Grand Total: 590", "Test Case 2 Line 2 Failed!"
    print(">>> STATUS: PASSED (MATCHED)")

    # Test Case 3: Invalid Input
    print("\n[Test Case 3: Invalid Input]")
    print("Input: (a) Add to cart: Laptop")
    cart3 = []
    _, msg3a = add_to_cart(cart3, "Laptop", 1)
    print("Actual (a)  :", msg3a)
    print("Expected (a): Invalid product. Available: Pen, Notebook, Bag")
    assert msg3a == "Invalid product. Available: Pen, Notebook, Bag", "Test Case 3a Failed!"

    print("Input: (b) Add to cart: Pen, Quantity: -1")
    _, msg3b = add_to_cart(cart3, "Pen", -1)
    print("Actual (b)  :", msg3b)
    print("Expected (b): Quantity must be at least 1.")
    assert msg3b == "Quantity must be at least 1.", "Test Case 3b Failed!"
    print(">>> STATUS: PASSED (MATCHED)")

    # Test Case 4: Different Valid Scenario
    print("\n[Test Case 4: Different Valid Scenario]")
    print("Input: (a) Add Bag x2, (b) Add Pen x5, (c) Remove Pen, (d) Checkout")
    cart4 = []
    add_to_cart(cart4, "Bag", 2)
    add_to_cart(cart4, "Pen", 5)
    _, msg4c = remove_from_cart(cart4, "Pen")
    print("Actual (c)  :", msg4c)
    print("Expected (c): Pen removed. Cart: Bag x2 = 1000")
    assert msg4c == "Pen removed. Cart: Bag x2 = 1000", "Test Case 4c Failed!"

    bill4 = calculate_bill(cart4)
    line4d1 = f"Subtotal: {format_num(bill4['subtotal'])} | Discount: {format_num(bill4['discount'])} | GST: {format_num(bill4['gst'])}"
    line4d2 = f"Grand Total: {format_num(bill4['grand_total'])}"
    print("Actual (d)  :")
    print(line4d1)
    print(line4d2)
    print("Expected (d):")
    print("Subtotal: 1000 | Discount: 100 | GST: 162")
    print("Grand Total: 1062")
    assert line4d1 == "Subtotal: 1000 | Discount: 100 | GST: 162", "Test Case 4d Line 1 Failed!"
    assert line4d2 == "Grand Total: 1062", "Test Case 4d Line 2 Failed!"
    print(">>> STATUS: PASSED (MATCHED)")

    print("\n" + "=" * 60)
    print("ALL 4 TEST CASES PASSED SUCCESSFULLY!")
    print("=" * 60 + "\n")


def interactive_menu():
    """Interactive console menu for user interaction."""
    cart = []
    while True:
        print("\n===============================")
        print("     SHOPPING CART SYSTEM      ")
        print("===============================")
        print("1. View Products")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Run Automated Test Cases (All 4)")
        print("7. Exit")
        print("===============================")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            view_products()

        elif choice == "2":
            prod = input("Enter product name (Pen, Notebook, Bag): ").strip()
            qty_input = input("Enter quantity: ").strip()
            success, msg = add_to_cart(cart, prod, qty_input)
            print(">>", msg)

        elif choice == "3":
            if not cart:
                print(">> Cart is already empty.")
                continue
            prod = input("Enter product name to remove: ").strip()
            success, msg = remove_from_cart(cart, prod)
            print(">>", msg)

        elif choice == "4":
            view_cart(cart)

        elif choice == "5":
            if not cart:
                print(">> Cart is empty! Add products first.")
                continue
            print("\n--- FINAL BILL ---")
            checkout(cart)
            cart.clear()
            print("Thank you for shopping!\n")

        elif choice == "6":
            run_all_test_cases()

        elif choice == "7":
            print("\nThank you for using Shopping Cart System. Goodbye!\n")
            break

        else:
            print(">> Invalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t", "test"):
        run_all_test_cases()
    else:
        interactive_menu()
