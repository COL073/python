def calculate_discount(price, discount_percent):
    discount =(discount_percent/100)* price
    discount_percent = (discount / price) *100
    if discount_percent >= 20:
        final_price = price - discount
        return final_price
    else:
        return price
        
        
def main():
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percentage)
    print("Final price after discount:", final_price)

if __name__ == "__main__":
    main() 


