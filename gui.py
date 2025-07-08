import tkinter as tk
from tkinter import messagebox
from bot import BasicBot

bot = BasicBot()

def place_order():
    symbol = symbol_entry.get().upper()
    side = side_var.get()
    order_type = type_var.get()
    quantity = float(qty_entry.get())
    price = price_entry.get() if price_entry.get() else None
    stop_price = stop_entry.get() if stop_entry.get() else None

    try:
        order = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
        if order:
            messagebox.showinfo("Success", f"Order placed: {order}")
        else:
            messagebox.showerror("Failed", "Order placement failed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Binance Testnet Trading Bot")

tk.Label(root, text="Symbol:").grid(row=0, column=0)
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=0, column=1)

tk.Label(root, text="Side:").grid(row=1, column=0)
side_var = tk.StringVar(value="BUY")
tk.OptionMenu(root, side_var, "BUY", "SELL").grid(row=1, column=1)

tk.Label(root, text="Order Type:").grid(row=2, column=0)
type_var = tk.StringVar(value="MARKET")
tk.OptionMenu(root, type_var, "MARKET", "LIMIT", "STOP_LIMIT").grid(row=2, column=1)

tk.Label(root, text="Quantity:").grid(row=3, column=0)
qty_entry = tk.Entry(root)
qty_entry.grid(row=3, column=1)

tk.Label(root, text="Price (if LIMIT/STOP):").grid(row=4, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=4, column=1)

tk.Label(root, text="Stop Price (if STOP_LIMIT):").grid(row=5, column=0)
stop_entry = tk.Entry(root)
stop_entry.grid(row=5, column=1)

tk.Button(root, text="Place Order", command=place_order).grid(row=6, column=0, columnspan=2)

root.mainloop()
