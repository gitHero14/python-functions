def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
     discount = (discount_percent/100) * price
     new_price = price - discount
     return new_price
    else:
       return price
    
print(calculate_discount(40,50))
print(calculate_discount(40,5))

def main():
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price == original_price:
        print("No discount applied. Price remains:", final_price)

    else:
        print(("Final Price after applying a", discount_percent, "% discount: ", final_price))

if __name__ == "__main__":
    main()