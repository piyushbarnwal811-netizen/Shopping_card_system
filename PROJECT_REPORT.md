# PROJECT REPORT
## PS No. 4: SHOPPING CART SYSTEM

**Institution:** Rungta International Skills University  
**Department:** School of Computer Science and Engineering  
**Program:** Bachelor of Technology in Computer Science and Engineering  
**Course:** Python Programming Laboratory  
**Problem Statement Number:** 4  
**Project Title:** Shopping Cart System  

---

## 1. ABSTRACT
The Shopping Cart System is a console-based e-commerce simulation developed in Python 3. It models core retail transactions including product catalog browsing, input validation, cart management (adding and removing items), and financial calculations involving tiered discounts and Goods and Services Tax (GST). The application demonstrates proficiency in foundational computer science concepts: data structures (Lists and Dictionaries), modular functional programming, defensive programming through input validation, and billing algorithms.

---

## 2. PROBLEM DEFINITION & SCOPE

### 2.1 Problem Statement
Develop a console shopping cart where the user can view products, add or remove items, and generate a final bill with discount and GST.

### 2.2 System Specifications
- **Programming Language:** Python 3 (Single `.py` file requirement)
- **Concepts Implemented:** Lists, Dictionaries, Functions, Billing Logic
- **Product Catalogue:**
  - Pen: Rs. 10
  - Notebook: Rs. 50
  - Bag: Rs. 500
- **Taxation & Discounts:**
  - GST: 18% applied to the taxable subtotal
  - Discount: 10% discount if the subtotal strictly exceeds Rs. 500 (`subtotal > 500`)

### 2.3 Bare Minimum Requirements Checklist
- [x] **Req 1:** Written in Python 3 as a single `.py` file executable from the console.
- [x] **Req 2:** Product catalogue stored and maintained in a dictionary.
- [x] **Req 3:** Add, remove, and view cart items implemented using modular functions.
- [x] **Req 4:** Accurate calculation of subtotal, discount, GST, and grand total.
- [x] **Req 5:** Robust validation of product names and quantities.

---

## 3. SYSTEM DESIGN & ARCHITECTURE

### 3.1 Data Structures
1. **Product Catalogue (Dictionary):**
   ```python
   CATALOGUE = {
       "Pen": 10,
       "Notebook": 50,
       "Bag": 500
   }
   ```
   *Purpose:* $O(1)$ constant time lookup for item prices and available inventory.

2. **Cart Storage (List of Dictionaries):**
   ```python
   cart = [
       {"product": "Bag", "price": 500, "quantity": 2},
       {"product": "Notebook", "price": 50, "quantity": 1}
   ]
   ```
   *Purpose:* Preserves order of addition, easily iterable for subtotal calculation, and straightforward mutation when items are removed or updated.

---

### 3.2 Modular Function Architecture

| Function Name | Parameters | Return Type | Description |
|---|---|---|---|
| `validate_product(name)` | `product_name: str` | `tuple(bool, str)` | Validates item against catalog (case-insensitive) |
| `validate_quantity(qty)` | `quantity: any` | `tuple(bool, int/str)` | Validates quantity is an integer $\ge 1$ |
| `calculate_subtotal(cart)` | `cart: list` | `float/int` | Sums $\sum (\text{price} \times \text{quantity})$ |
| `add_to_cart(cart, prod, qty)` | `cart, prod, qty` | `tuple(bool, str)` | Adds item to cart and returns formatted message |
| `remove_from_cart(cart, prod)` | `cart, prod, qty=None` | `tuple(bool, str)` | Removes item and returns updated cart summary |
| `view_products()` | *None* | `None` | Displays catalogue on console |
| `view_cart(cart)` | `cart: list` | `None` | Displays current cart items and subtotal |
| `calculate_bill(cart)` | `cart: list` | `dict` | Computes subtotal, discount, GST, grand total |
| `checkout(cart)` | `cart: list` | `dict` | Prints formatted final bill |

---

### 3.3 Flowchart of Billing Logic

```
          [Start Checkout]
                 │
          Calculate Subtotal
                 │
        Is Subtotal > 500?
           /            \
       YES               NO
       /                  \
Discount = 10%       Discount = 0
       \                  /
        \                /
     Taxable = Subtotal - Discount
                 │
          GST = 18% of Taxable
                 │
     Grand Total = Taxable + GST
                 │
           [Print Bill]
```

---

## 4. MATHEMATICAL BILLING FORMULAS

$$\text{Subtotal} = \sum_{i=1}^{n} (\text{price}_i \times \text{quantity}_i)$$

$$\text{Discount} = \begin{cases} 
0.10 \times \text{Subtotal} & \text{if } \text{Subtotal} > 500 \\ 
0 & \text{if } \text{Subtotal} \le 500 
\end{cases}$$

$$\text{Taxable Amount} = \text{Subtotal} - \text{Discount}$$

$$\text{GST} = 0.18 \times \text{Taxable Amount}$$

$$\text{Grand Total} = \text{Taxable Amount} + \text{GST}$$

---

## 5. TEST CASES VERIFICATION & RESULTS

### Test Case 1: Normal Input
- **Input:** Add to cart: `Notebook`, Quantity: `2`
- **Calculation:** $50 \times 2 = 100$
- **Expected Output:** `Notebook x2 added | Cart subtotal: 100`
- **Actual Output:** `Notebook x2 added | Cart subtotal: 100`
- **Result:** **PASSED**

---

### Test Case 2: Boundary / Minimum Input
- **Input:** Add to cart: `Bag`, Quantity: `1`, followed by `Checkout`
- **Calculation:**
  - Subtotal = $500 \times 1 = 500$
  - Since $500 \ngtr 500$, Discount = $0$
  - Taxable = $500$
  - GST = $18\% \times 500 = 90$
  - Grand Total = $500 + 90 = 590$
- **Expected Output:**
  ```text
  Subtotal: 500 | Discount: 0 | GST: 90
  Grand Total: 590
  ```
- **Actual Output:**
  ```text
  Subtotal: 500 | Discount: 0 | GST: 90
  Grand Total: 590
  ```
- **Result:** **PASSED**

---

### Test Case 3: Invalid Input
- **Input (a):** Add to cart: `Laptop`
  - **Expected:** `Invalid product. Available: Pen, Notebook, Bag`
  - **Actual:** `Invalid product. Available: Pen, Notebook, Bag`
  - **Result:** **PASSED**
- **Input (b):** Add to cart: `Pen`, Quantity: `-1`
  - **Expected:** `Quantity must be at least 1.`
  - **Actual:** `Quantity must be at least 1.`
  - **Result:** **PASSED**

---

### Test Case 4: Different Valid Scenario
- **Input:**
  1. Add `Bag x2`
  2. Add `Pen x5`
  3. Remove `Pen`
  4. `Checkout`
- **Calculation:**
  - After removing Pen, Cart has: `Bag x2 = 1000`
  - Subtotal = $1000$
  - Since $1000 > 500$, Discount = $10\% \times 1000 = 100$
  - Taxable = $1000 - 100 = 900$
  - GST = $18\% \times 900 = 162$
  - Grand Total = $900 + 162 = 1062$
- **Expected Output:**
  ```text
  (c) Pen removed. Cart: Bag x2 = 1000
  (d) Subtotal: 1000 | Discount: 100 | GST: 162
      Grand Total: 1062
  ```
- **Actual Output:**
  ```text
  Pen removed. Cart: Bag x2 = 1000
  Subtotal: 1000 | Discount: 100 | GST: 162
  Grand Total: 1062
  ```
- **Result:** **PASSED**

---

## 6. SOURCE CODE LISTING
Refer to the primary file [`shopping_cart.py`](file:///c:/Users/piyus/OneDrive/Desktop/piyush%20room/shopping_cart.py) for the complete implementation.

---

## 7. CONCLUSION
The Shopping Cart System was successfully engineered according to all given academic criteria and industry practices. It validates all user inputs, adheres strictly to the single-file constraint, correctly manages memory using standard data structures, and passes 100% of the required test cases with zero defects.
