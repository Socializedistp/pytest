# # 1) Ice Americano : 2000  2) Cafe Latte : 3000
drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
prices = [2000, 3000, 4900]
#amounts = [0, 0, 0]
amounts = lest()
for _ in range(len(drinks)):
    amounts.append(0)
total_price = 0

def order_process(idx: int):
    global total_price
    print(f"{drinks[idx]} ordered. Price : {prices[idx]}won")
    total_price = total_price + prices[idx]
    amounts[idx] = amounts[idx] + 1    

menu_lists = ""
for k in range(len(drinks)):
    menu_lists = menu_lists + f"{k+1}) {drinks[k]} {prices[k]}won  "
menu_lists = menu_lists + f"{len(drinks)+1}) Exit : "

while True:
    menu = int(input(menu_lists))
    if len(drinks) >= menu >= 1:
        order_process(menu-1)
    elif menu == len(drinks)+1:
        print("Finish order~")
        break
    else:
        print(f"{menu} menu is not exist. please choose from above menu.")

print("Product  Price  Amount  Subtotal")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")
print(f"Total price : {total_price}")
