# 1) ICE Ammericano: 2000 2) Cafe Latte: 3000
drinks = ["Ice Americano", "Cafe Latte"]
prices = [2000, 3000]
order_list = ''
while True:
    menu = input("1) Ice Americano{prices[0]}won 2) Cafe Latte{prices[1]}won 3) Exit: ")
    if menu == "1":
        print("Ice Americano ordered. Rrice: {prices[0]}won")
        order_list = order_list + drinks[0] 
    elif menu == "2":
        print("Cafe Latte ordered. Rrice: {prices[1]}won")
        
    elif menu == "3":
        print("Finish order")
        break
    
    else:
        print(f"{menu} menu is not exist. please choose from above menu.")
    
print(order_list)
print("Total price: {total_price}")