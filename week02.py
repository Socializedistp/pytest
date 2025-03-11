# 1) ICE Ammericano: 2000 2) Cafe Latte: 3000
drinks = ["Ice Americano", "Cafe Latte"]
prices = [2000, 3000]
order_list = ''
while True:
    menu = input(f"1) {drinks[0]} {prices[0]}won 2) {drinks[1]} {prices[1]}won 3) Exit: ")
    if menu == "1":
        print(f"{drinks[0]} ordered. Rrice: {prices[0]}won")
        
    elif menu == "2":
        print(f"{drinks[1]} ordered. Rrice: {prices[1]}won")
        
    elif menu == "3":
        print("Finish order")
        break