{
    "name": "Purchase Invoice Received Quantity Validation",
    "version": "18.0.1.0.0",
    "category": "Purchase",
    "summary": "Prevent vendor bills from exceeding received quantities on 3-way matching purchase orders",
    "description": """
Purchase Invoice Received Quantity Validation
=============================================

This module prevents users from creating vendor bills with quantities
greater than the received quantities for purchase orders using
3-way matching ('Based on received quantities').

Features
--------
* Validate vendor bill quantities against received quantities
* Support 3-way matching purchase orders
* Prevent over billing before posting vendor bills
* Clear validation error messages for users

Technical
---------
The module extends account.move validation logic for vendor bills
linked to purchase order lines.
    """,
    "author": "mayna,diandra",
    "website": "https://github.com/stmayna",
    "license": "LGPL-3",
    "depends": [
        "account",
        "purchase",
        "purchase_stock",
    ],
    "data": [],
    "installable": True,
    "application": False,
    "auto_install": False,
}