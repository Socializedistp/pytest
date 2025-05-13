import tkinter as tk
from tkinter import messagebox
import sqlite3
from typing import List


# ================= Discount Policy ===================
class DiscountPolicy:
    def apply(self, total_price: int) -> int:
        return total_price


class TenPercentOverTenThousand(DiscountPolicy):
    def apply(self, total_price: int) -> int:
        if total_price >= 10000:
            return int(total_price * 0.9)
        return total_price


# ================= Ticket Number Service ===================
class TicketNumberService:
    def __init__(self, db_path: str = 'queue_number.db') -> None:
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS ticket (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def get_next_ticket_number(self) -> int:
        self.cur.execute('SELECT MAX(number) FROM ticket')
        result = self.cur.fetchone()
        next_number = (result[0] or 0) + 1

        self.cur.execute('INSERT INTO ticket (number) VALUES (?)', (next_number,))
        self.conn.commit()
        return next_number

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()


# ================= Menu Class ===================
class Menu:
    def __init__(self, drinks: List[str], prices: List[int]):
        if len(drinks) != len(prices):
            raise ValueError("Drinks and prices lists must have the same length.")
        self.drinks = drinks
        self.prices = prices

    def get_price(self, idx: int) -> int:
        return self.prices[idx]

    def get_drink_name(self, idx: int) -> str:
        return self.drinks[idx]

    def get_menu_length(self) -> int:
        return len(self.drinks)


# ================= Order Processor ===================
class OrderProcessor:
    def __init__(self, menu: Menu, discount_policy: DiscountPolicy, ticket_service: TicketNumberService):
        self.menu = menu
        self.amounts = [0] * menu.get_menu_length()
        self.total_price = 0
        self.discount_policy = discount_policy
        self.ticket_service = ticket_service

    def process_order(self, idx: int) -> None:
        price = self.menu.get_price(idx)
        self.amounts[idx] += 1
        self.total_price += price

    def get_receipt_text(self) -> str:
        receipt = f"{'Product':<15}{'Price':<10}{'Amount':<10}{'Subtotal':<10}\n"
        receipt += "-" * 50 + "\n"

        for i in range(self.menu.get_menu_length()):
            if self.amounts[i] > 0:
                name = self.menu.get_drink_name(i)
                price = self.menu.get_price(i)
                amt = self.amounts[i]
                receipt += f"{name:<15}{price:<10}{amt:<10}{price * amt} won\n"

        discounted = self.discount_policy.apply(self.total_price)
        discount = self.total_price - discounted

        receipt += "-" * 50 + "\n"
        receipt += f"{'Total before discount:':<30}{self.total_price} won\n"
        if discount > 0:
            receipt += f"{'Discount applied:':<30}{discount} won\n"
            receipt += f"{'Total after discount:':<30}{discounted} won\n"
        else:
            receipt += f"{'No discount applied.':<30}\n"
            receipt += f"{'Total:':<30}{self.total_price} won\n"

        return receipt

    def get_ticket(self) -> int:
        return self.ticket_service.get_next_ticket_number()


# ================= Kiosk GUI ===================
class KioskGUI:
    def __init__(self, root: tk.Tk, menu: Menu, order_processor: OrderProcessor):
        self.root = root
        self.menu = menu
        self.order_processor = order_processor
        self.root.title("Cafe Kiosk")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Cafe Menu", font=("Arial", 20)).pack()
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        for i in range(self.menu.get_menu_length()):
            name = self.menu.get_drink_name(i)
            price = self.menu.get_price(i)
            tk.Button(
                frame,
                text=f"{name}\n{price} won",
                command=lambda idx=i: self.add_to_order(idx),
                width=15,
                height=2
            ).grid(row=i // 2, column=i % 2, padx=5, pady=5)

        self.order_text = tk.Text(self.root, height=10, width=50)
        self.order_text.pack(pady=5)

        tk.Button(self.root, text="Complete Order", command=self.complete_order, bg="green", fg="white").pack(side="left", padx=10)
        tk.Button(self.root, text="Reset", command=self.reset_order, bg="orange").pack(side="left")
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="red", fg="white").pack(side="right", padx=10)

    def add_to_order(self, idx: int):
        self.order_processor.process_order(idx)
        self.update_order_display()

    def update_order_display(self):
        self.order_text.config(state=tk.NORMAL)
        self.order_text.delete("1.0", tk.END)
        self.order_text.insert(tk.END, self.order_processor.get_receipt_text())
        self.order_text.config(state=tk.DISABLED)

    def complete_order(self):
        if self.order_processor.total_price == 0:
            messagebox.showinfo("Notice", "Please add items before completing the order.")
            return

        receipt = self.order_processor.get_receipt_text()
        ticket = self.order_processor.get_ticket()

        messagebox.showinfo("Receipt", f"{receipt}\n\nQueue Number: {ticket}")
        self.reset_order()

    def reset_order(self):
        self.order_processor = OrderProcessor(self.menu, TenPercentOverTenThousand(), TicketNumberService())
        self.update_order_display()


# ================= Entry Point ===================
if __name__ == '__main__':
    drinks = ["Americano", "Latte", "Cappuccino", "Mocha"]
    prices = [3000, 3500, 3700, 4000]

    root = tk.Tk()
    menu = Menu(drinks, prices)
    discount = TenPercentOverTenThousand()
    ticket_service = TicketNumberService()
    order_processor = OrderProcessor(menu, discount, ticket_service)
    app = KioskGUI(root, menu, order_processor)
    root.mainloop()