import tkinter as tk
from tkinter import ttk
from flight_api import get_flight_price
from notifier import send_email_alert
# from utils import is_price_good
def is_price_good(current_price, target_price):
    return current_price <= target_price

# ---------------- Window ----------------
window = tk.Tk()
window.title("✈️ Flight Price Tracker")
window.geometry("420x580")
window.configure(bg="#f5f7fa")
window.resizable(False, False)

# ---------------- Styles ----------------
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))
style.configure("TButton", font=("Segoe UI", 10), padding=6)

# ---------------- Card ----------------
card = tk.Frame(window, bg="white", bd=1, relief="solid")
card.place(relx=0.5, rely=0.5, anchor="center", width=360, height=460)

# ---------------- Header ----------------
tk.Label(
    card,
    text="Flight Price Alert",
    bg="white",
    fg="#2c3e50",
    font=("Segoe UI", 18, "bold")
).pack(pady=15)

# ---------------- Inputs ----------------
def input_field(label):
    tk.Label(card, text=label, bg="white").pack(anchor="w", padx=25)
    entry = ttk.Entry(card)
    entry.pack(fill="x", padx=25, pady=5)
    return entry

src_entry = input_field("From (IATA Code)")
dest_entry = input_field("To (IATA Code)")
date_entry = input_field("Date (YYYY-MM-DD)")
price_entry = input_field("Target Price (₹)")
email_entry = input_field("Your Email")

# ---------------- Action ----------------
def check_price():
    try:
        source = src_entry.get()
        destination = dest_entry.get()
        date = date_entry.get()
        target_price = int(price_entry.get())
        email = email_entry.get()

        price = get_flight_price(source, destination, date)
        result_label.config(text=f"💰 Current Price: ₹{price}")

        if is_price_good(price, target_price):
            send_email_alert(email, price, source, destination)
            status_label.config(
                text="✅ Price dropped! Email sent.",
                fg="green"
            )
        else:
            status_label.config(
                text="❌ Price too high.",
                fg="red"
            )

    except:
        status_label.config(
            text="⚠️ Invalid input / API error",
            fg="orange"
        )

# ---------------- Button ----------------
ttk.Button(
    card,
    text="Check Price",
    command=check_price
).pack(pady=20)

# ---------------- Output ----------------
result_label = tk.Label(card, text="", bg="white", font=("Segoe UI", 11))
result_label.pack()

status_label = tk.Label(card, text="", bg="white", font=("Segoe UI", 10))
status_label.pack(pady=5)

# ---------------- Footer ----------------
tk.Label(
    card,
    text="Powered by Live Flight APIs",
    bg="white",
    fg="gray",
    font=("Segoe UI", 8)
).pack(side="bottom", pady=10)

window.mainloop()
