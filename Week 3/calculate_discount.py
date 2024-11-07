# Step 1: Define the function
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Step 2: Prompt the user for input
# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 3: Call the function and print the result
# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Check if the discount was applied and print the appropriate message
if final_price == price:
    print("No discount applied. The original price is:", final_price)
else:
    print("The final price after applying the discount is:", final_price)
