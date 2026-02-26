def create_professional_bill(customer, product, price, discount=0):
    vat_rate = 0.05  # ৫% ভ্যাট
    total_vat = price * vat_rate
    final_price = (price + total_vat) - discount
    print(f"--- SR ELECTRONICS PARK ---")
    print(f"Customer: {customer}")
    print(f"Product: {product}")
    print(f"Net Total (Incl. VAT): {final_price} BDT")
    return final_price
# Example Usage
# create_professional_bill("Global Client", "MyOne TV", 32500, 500)
