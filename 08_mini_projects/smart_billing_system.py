"""
Topic   : Mini Project — Smart Billing & Analytics System
Date    : December 2025
Author  : Chaitanya

Description : A command-line billing calculator for a small shop.
              Handles type casting, GST calculation and formatted output.
              Extracted from practiceSheet1.py where it was placed
              as a standalone project problem.
"""


def generate_bill():
    """Calculate and display a formatted bill with GST and discount."""
    print("Welcome to the Smart Billing System.")

    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price_per_item = float(input("Enter price per item: "))
    discount_percentage = float(input("Enter discount percentage (0 if none): "))

    GST_PERCENTAGE = 18

    # Calculations
    total_amount = price_per_item * quantity
    discounted_amount = (total_amount * discount_percentage) / 100
    final_amount = total_amount - discounted_amount
    gst_amount = (final_amount * GST_PERCENTAGE) / 100
    final_billed_amount = final_amount + gst_amount

    # Store in a dictionary
    bill = {
        "product": product_name,
        "quantity": quantity,
        "price_per_item": price_per_item,
        "total_amount": total_amount,
        "discounted_price": discounted_amount,
        "gst": gst_amount,
        "final_billed_amount": final_billed_amount
    }

    # Display formatted bill
    print("\n" + "=" * 40)
    print(f"Product        : {bill['product']}")
    print(f"Quantity       : {bill['quantity']}")
    print(f"Price per Item : {bill['price_per_item']}")
    print("-" * 40)
    print(f"Total Amount   : {bill['total_amount']:.2f}")
    print(f"Discount       : {bill['discounted_price']:.2f}")
    print(f"GST (18%)      : {bill['gst']:.2f}")
    print("-" * 40)
    print(f"Final Bill     : {bill['final_billed_amount']:.2f}")
    print("=" * 40)
    print("**** Thank you! ****")


if __name__ == "__main__":
    generate_bill()
