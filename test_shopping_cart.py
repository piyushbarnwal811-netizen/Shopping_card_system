"""
Unit Tests for Shopping Cart System
Bachelor of Technology Computer Science and Engineering
Rungta International Skills University
"""

import unittest
from shopping_cart import (
    CATALOGUE,
    validate_product,
    validate_quantity,
    add_to_cart,
    remove_from_cart,
    calculate_bill,
    calculate_subtotal,
    format_num
)


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = []

    def test_catalogue_initialization(self):
        """Verify product catalogue dictionary requirements."""
        self.assertEqual(CATALOGUE["Pen"], 10)
        self.assertEqual(CATALOGUE["Notebook"], 50)
        self.assertEqual(CATALOGUE["Bag"], 500)

    def test_case_1_normal_input(self):
        """
        Test Case 1: Normal Input
        Input: Add to cart: Notebook, Quantity: 2
        Expected Output: Notebook x2 added | Cart subtotal: 100
        """
        success, msg = add_to_cart(self.cart, "Notebook", 2)
        self.assertTrue(success)
        self.assertEqual(msg, "Notebook x2 added | Cart subtotal: 100")
        self.assertEqual(calculate_subtotal(self.cart), 100)

    def test_case_2_boundary_minimum_input(self):
        """
        Test Case 2: Boundary / Minimum Input
        Input: Add to cart: Bag, Quantity: 1 -> Checkout
        Expected Output:
        Subtotal: 500 | Discount: 0 | GST: 90
        Grand Total: 590
        """
        add_to_cart(self.cart, "Bag", 1)
        bill = calculate_bill(self.cart)
        self.assertEqual(bill["subtotal"], 500)
        self.assertEqual(bill["discount"], 0)
        self.assertEqual(bill["gst"], 90)
        self.assertEqual(bill["grand_total"], 590)

    def test_case_3_invalid_inputs(self):
        """
        Test Case 3: Invalid Input
        (a) Add to cart: Laptop -> Invalid product. Available: Pen, Notebook, Bag
        (b) Add to cart: Pen, Quantity: -1 -> Quantity must be at least 1.
        """
        # (a)
        success_a, msg_a = add_to_cart(self.cart, "Laptop", 1)
        self.assertFalse(success_a)
        self.assertEqual(msg_a, "Invalid product. Available: Pen, Notebook, Bag")

        # (b)
        success_b, msg_b = add_to_cart(self.cart, "Pen", -1)
        self.assertFalse(success_b)
        self.assertEqual(msg_b, "Quantity must be at least 1.")

    def test_case_4_different_valid_scenario(self):
        """
        Test Case 4: Different Valid Scenario
        (a) Add Bag x2
        (b) Add Pen x5
        (c) Remove Pen -> Pen removed. Cart: Bag x2 = 1000
        (d) Checkout ->
        Subtotal: 1000 | Discount: 100 | GST: 162
        Grand Total: 1062
        """
        add_to_cart(self.cart, "Bag", 2)
        add_to_cart(self.cart, "Pen", 5)
        
        # (c) Remove Pen
        success_c, msg_c = remove_from_cart(self.cart, "Pen")
        self.assertTrue(success_c)
        self.assertEqual(msg_c, "Pen removed. Cart: Bag x2 = 1000")

        # (d) Checkout
        bill = calculate_bill(self.cart)
        self.assertEqual(bill["subtotal"], 1000)
        self.assertEqual(bill["discount"], 100)
        self.assertEqual(bill["gst"], 162)
        self.assertEqual(bill["grand_total"], 1062)

    def test_case_insensitivity(self):
        """Test product lookup handles lower/upper case cleanly."""
        success, _ = add_to_cart(self.cart, "notebook", 1)
        self.assertTrue(success)
        self.assertEqual(self.cart[0]["product"], "Notebook")

    def test_zero_quantity_rejected(self):
        """Test quantity of 0 is rejected."""
        valid, msg = validate_quantity(0)
        self.assertFalse(valid)
        self.assertEqual(msg, "Quantity must be at least 1.")


if __name__ == "__main__":
    unittest.main()
