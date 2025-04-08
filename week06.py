import kiosk


if __name__ == "__main__":
    menu_drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice"]
    menu_prices = [2000, 3000, 4900]

    menu = kiosk.Menu(menu_drinks, menu_prices)
    order_processor = kiosk.OrderProcessor(menu)  # has-a, aggregation
    order_processor.run()