import tkinter as tk
from kiosk import Menu, KioskGUI, OrderProcessor, TenPercentOverTenThousand, TicketNumberService

if __name__ == "__main__":
    menu_drinks = ["Ice Americano", "Cafe Latte", "Watermelon Juice", "Ice Tea"]
    menu_prices = [2000, 3000, 4900, 3300]

    root = tk.Tk()

    # 구성 객체 생성
    menu = Menu(menu_drinks, menu_prices)
    discount_policy = TenPercentOverTenThousand()
    ticket_service = TicketNumberService()
    order_processor = OrderProcessor(menu, discount_policy, ticket_service)

    # GUI 실행
    app = KioskGUI(root, menu, order_processor)
    root.mainloop()
