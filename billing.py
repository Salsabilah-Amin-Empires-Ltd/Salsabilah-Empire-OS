"""
Billing Module for SR Electronics Park - Salsabilah-Empire-OS.
Developed by: MD. AL AMIN SOHAG
"""

def create_professional_bill(customer, product, price, discount=0):
    """
    Calculates the final bill including 5% VAT and applies discounts.
    
    Args:
        customer (str): Name of the client.
        product (str): Name of the electronics item.
        price (float): Base price of the product.
        discount (float): Deductible amount.
        
    Returns:
        float: The final price after tax and discount.
    """
    vat_rate = 0.05  # ৫% ভ্যাট
    total_vat = price * vat_rate
    final_price = (price + total_vat) - discount
    
    print("--- SR ELECTRONICS PARK ---")
    print(f"Customer: {customer}")
    print(f"Product: {product}")
    print(f"Net Total (Incl. VAT): {final_price:.2f} BDT")
    
    return final_price

# Example Usage
if __name__ == "__main__":
    create_professional_bill("Global Client", "MyOne TV", 32500, 500)
