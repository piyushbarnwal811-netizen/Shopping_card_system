# Shopping Cart System (Python 3)

**Institution:** Rungta International Skills University  
**Department:** School of Computer Science and Engineering  
**Degree:** Bachelor of Technology in Computer Science and Engineering  
**Problem Statement No.:** PS No. 4  
**Project Title:** Shopping Cart System  

---

## 📌 Problem Overview
Develop a console shopping cart in Python 3 where the user can view products, add or remove items, and generate a final bill with discount and GST.

### Product Catalogue:
- **Pen:** Rs. 10
- **Notebook:** Rs. 50
- **Bag:** Rs. 500

### Billing Rules:
- **GST Rate:** 18%
- **Discount:** 10% discount if subtotal is strictly greater than Rs. 500 (`subtotal > 500`).
- Taxable amount for GST calculation = `subtotal - discount`.
- Grand Total = `taxable_amount + GST`.

---

## 🚀 Features & Requirements Covered
1. **Single Python File:** Entire core system implemented in `shopping_cart.py`.
2. **Product Catalogue in Dictionary:** Implemented as `CATALOGUE = {"Pen": 10, "Notebook": 50, "Bag": 500}`.
3. **Modular Functions:**
   - `view_products()`: Displays available items.
   - `add_to_cart()`: Validates and adds items to the cart.
   - `remove_from_cart()`: Removes items or updates quantities.
   - `view_cart()`: Displays current items and subtotal.
   - `calculate_bill()`: Computes subtotal, discount, GST, and grand total.
   - `checkout()`: Prints the formatted final bill.
4. **Input Validation:**
   - Product name validation (`validate_product()`).
   - Quantity validation (`validate_quantity()`, requires integer ≥ 1).
5. **Exact Match Test Cases:** Passes all 4 specified test cases identically.

---

## 🧪 Test Cases & Expected vs Actual Output

| Test Case | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| **Test Case 1 (Normal Input)** | `Notebook, Quantity: 2` | `Notebook x2 added \| Cart subtotal: 100` | `Notebook x2 added \| Cart subtotal: 100` | ✅ PASSED |
| **Test Case 2 (Boundary Input)** | `Bag, Quantity: 1`<br>`Checkout` | `Subtotal: 500 \| Discount: 0 \| GST: 90`<br>`Grand Total: 590` | `Subtotal: 500 \| Discount: 0 \| GST: 90`<br>`Grand Total: 590` | ✅ PASSED |
| **Test Case 3 (Invalid Input)** | `(a) Laptop`<br>`(b) Pen, Quantity: -1` | `(a) Invalid product. Available: Pen, Notebook, Bag`<br>`(b) Quantity must be at least 1.` | `(a) Invalid product. Available: Pen, Notebook, Bag`<br>`(b) Quantity must be at least 1.` | ✅ PASSED |
| **Test Case 4 (Different Valid)** | `(a) Add Bag x2`<br>`(b) Add Pen x5`<br>`(c) Remove Pen`<br>`(d) Checkout` | `(c) Pen removed. Cart: Bag x2 = 1000`<br>`(d) Subtotal: 1000 \| Discount: 100 \| GST: 162`<br>`Grand Total: 1062` | `(c) Pen removed. Cart: Bag x2 = 1000`<br>`(d) Subtotal: 1000 \| Discount: 100 \| GST: 162`<br>`Grand Total: 1062` | ✅ PASSED |

---

## 💻 How to Run

### 1. Interactive Console Mode
Run the main program:
```bash
python shopping_cart.py
```
This opens an interactive menu:
```text
===============================
     SHOPPING CART SYSTEM      
===============================
1. View Products
2. Add Item to Cart
3. Remove Item from Cart
4. View Cart
5. Checkout
6. Run Automated Test Cases (All 4)
7. Exit
===============================
```

### 2. Run Test Cases Directly
To verify all 4 problem-statement test cases instantly:
```bash
python shopping_cart.py --test
```

### 3. Run Unit Test Suite
To run formal Python `unittest` suite:
```bash
python -m unittest test_shopping_cart.py
```

---

## 📂 Project Structure
```text
piyush room/
│
├── shopping_cart.py       # Main Python 3 solution (single .py file)
├── test_shopping_cart.py  # Unit test suite (7 tests)
├── PROJECT_REPORT.md      # Formal academic project report
└── README.md              # Project documentation and guide
```

---

## 📤 How to Upload to GitHub
1. Open terminal/PowerShell in this folder:
   ```bash
   git init
   git add .
   git commit -m "feat: complete shopping cart system with test cases and report"
   ```
2. Create a new repository on your GitHub account (e.g., `shopping-cart-system`).
3. Link your remote repository and push:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<your-username>/shopping-cart-system.git
   git push -u origin main
   ```
