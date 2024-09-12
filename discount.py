def calculate_discount(price, discount_percent):
  
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Example usage
original_price = 100.0
discount = 25.0
final_price = calculate_discount(original_price, discount)
print(f"The final price after a {discount}% discount is: ${final_price:.2f}")
