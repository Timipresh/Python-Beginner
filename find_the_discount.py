print('Enter the Original Price')
original_price = input()
print('Enter the Discount Percentage')
discount_per = input()

original_price = int(original_price)
discount_per = int(discount_per)

def discount(price, dis_per):
    discount = price - (price * dis_per/100)
    return discount

final_price = discount(original_price, discount_per)
final_price = round(final_price, 2)

print(f"You have a discount of {discount_per}%, you are to pay {final_price}")