# 1) Ice Americano : 2000  2) Cafe Latte : 3000
drinks = ["Ice Americano", "Cafe Latte"]
prices = [2000, 3000, 4900]
amounts = [0, 0, 0]
total_price = 0

menu_lists = ""
for k in range(len(drinks)):
    menu_lists = menu_lists + f"{k+1}) {drinks[k]} {prices[k]}won  "
menu_lists = menu_lists + f"{len(drinks)+1}) Exit : "

while True:
    # menu = input(f"1) {drinks[0]} {prices[0]}won  2) {drinks[1]} {prices[1]}won  3) {drinks[2]} {prices[2]}won  4) Exit : ")
    menu = input(menu_lists)
    if menu == "1":
        print(f"{drinks[0]} ordered. Price : {prices[0]}won")
        total_price = total_price + prices[0]
        amounts[0] = amounts[0] + 1
    elif menu == "2":
        print(f"{drinks[1]} ordered. Price : {prices[1]}won")
        total_price = total_price + prices[1]
        amounts[1] = amounts[1] + 1
    elif menu == "3":
        print(f"{drinks[2]} ordered. Price : {prices[2]}won")
        total_price = total_price + prices[2]
        amounts[2] = amounts[2] + 1
    elif menu == "4":
        print("Finish order~")
        break
    else:
        print(f"{menu} menu is not exist. please choose from above menu.")

print("Product  Price  Amount  Subtotal")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} x{amounts[i]} {prices[i] * amounts[i]}")
print(f"Total price : {total_price}")