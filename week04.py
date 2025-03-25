# # 1) Ice Americano : 2000  2) Cafe Latte : 3000
drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
prices = [2000, 3000, 4900]
amounts = [0] * len(drinks)
total_price = 0
DISCOUNT_TRESHOLD = 10000
DISCOUNT_RATE = 0.1

def apply_discount(price: int):
    """_summary_
    total price exceeds standard price, reflect discounted price
    Args:
        price (int): price before discount
        return: price after discount
    """
    if price >= DISCOUNT_TRESHOLD:
        discount = price * DISCOUNT_RATE
        return (price - discount)
    return price
    
def order_process(idx: int):        #documentation
    """
    Processes a drink order by updating the total price and quantity.

    Params:
        idx (int): The index of the selected drink in the menu.
    
    Updates:
        - Prints the ordered drink and its price.
        - Adds the price of the selected drink to the total price.
        - Increments the count of the selected drink.
    """
    global total_price
    print(f"{drinks[idx]} ordered. Price : {prices[idx]}won")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1    

menu_lists = "".join([f"{k+1}) {drinks[k]} {prices[k]}won  " for k in range(len(drinks))])
menu_lists = menu_lists + f"{len(drinks)+1}) Exit : "

while True:
    try:
        menu = int(input(menu_lists))
        if len(drinks) >= menu >= 1:
            order_process(menu-1)
        elif menu == len(drinks)+1:
            print("Finish order~")
            break
        else:
            print(f"{menu} menu is not valid. please choose from above menu.")
    except ValueError as err:
        print(f"cannot enter characters. Please enter a valid number.")
print("Product  Price  Amount  Subtotal")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")

deiscounted_price = apply_discount(total_price)
discount_amount = total_price - deiscounted_price
if(discount_amount > 0):
    print(f"discount_amount: {discount_amount}won")
else: 
    print(f"Discount is not been applied")
print(f"Total price : {deiscounted_price}won")