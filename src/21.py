def calculate_total_bill(amount):
    if amount <= 10:
        tax = 0.08
    elif amount <= 50:
        tax = 0.12
    else:
        tax = 0.16
    
    total_bill = amount * (1 + tax)
    
    return round(total_bill, 2)

total_amount = calculate_total_bill(45) # Example: Amount to be paid including tax
