# Purchase Invoice Received Quantity Validation

## Description

This module prevents users from billing quantities greater than the received quantities for Purchase Orders using 3-way matching.

The validation is applied on vendor bills linked to Purchase Order lines to ensure invoice quantities never exceed quantities received from stock operations.

---

## Features

- Prevent over billing on vendor bills
- Support 3-way matching purchase orders
- Validate billed quantity against received quantity
- Clear validation error messages
- Seamless integration with Purchase and Inventory modules

---

## Requirements

To make this validation work properly, the Purchase Order must use:

> Bill Control = Received quantities

Technical value:

```python
purchase_method = 'receive'
```

The validation only runs for Purchase Orders configured with received quantity billing.

---

## Dependencies

- account
- purchase
- purchase_stock

---

## Installation

1. Add the module to your custom addons directory
2. Restart Odoo
3. Update Apps List
4. Install the module from the Apps menu

---

## Usage

### Purchase Order Configuration

Create a Purchase Order with:

- Products that require receiving
- Bill Control set to **Received quantities**

---

### Validation Process

When posting a vendor bill:

- Odoo checks the related Purchase Order line
- The system compares:
  - Vendor Bill Quantity
  - Received Quantity
- If billed quantity exceeds received quantity, validation is blocked

---

## Example Validation Error

```text
You cannot bill more than the received quantity.

Product: Product A
PO: PO0001
Received Qty: 5.0
Remaining Qty To Invoice: 5.0
Bill Qty: 10.0
```

## Technical Details

Main validation method:

```python
_validate_received_quantity_vendor_bill()
```

The module extends:

```python
account.move
```

---

## Author

Siti Mayna

GitHub:
https://github.com/stmayna
