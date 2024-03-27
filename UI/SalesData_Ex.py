import tkinter as tk
from tkinter import font, messagebox
from tkinter import ttk


def clicked_button1():
    monthly_investment = m_inv_text.get()
    yearly_interest = y_int_text.get()
    years = years_text.get()
    try:
        monthly_investment = float(monthly_investment)
        yearly_interest = float(yearly_interest)
        years = int(years)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a [float] value for monthly\ninvestment and yearly interest" +
                                            " and an\n[integer] value for years!")
    monthly_interest = yearly_interest / (12 * 100)
    months = years * 12
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        month_interest = future_value * monthly_interest
        future_value += month_interest
    m_after_text.set(f"${monthly_investment:.2f}")
    int_rate_text.set(f"{yearly_interest}%")
    years_prod_text.set(f"{years}")
    future_value_text.set(f"${future_value:.2f}")


window = tk.Tk()
window.title("Future Value Calculator")
window.geometry("400x400")

frame = ttk.Frame(window, padding="10 10 10 10")
frame.pack(fill="both", expand=True)

m_inv_label = ttk.Label(frame, text="Enter Monthly Investment:  ")
m_inv_label.grid(column=0, row=0, sticky=tk.E)
m_inv_text = tk.StringVar()
m_inv_entry = ttk.Entry(frame, width=25, textvariable=m_inv_text)
m_inv_entry.grid(column=1, row=0)

y_int_label = ttk.Label(frame, text="Enter Yearly Interest Rate:  ")
y_int_label.grid(column=0, row=1, sticky=tk.E)
y_int_text = tk.StringVar()
y_int_entry = ttk.Entry(frame, width=25, textvariable=y_int_text)
y_int_entry.grid(column=1, row=1)

years_label = ttk.Label(frame, text="Enter Number of Years:  ")
years_label.grid(column=0, row=2, sticky=tk.E)
years_text = tk.StringVar()
years_entry = ttk.Entry(frame, width=25, textvariable=years_text)
years_entry.grid(column=1, row=2)

gap1 = ttk.Label(frame, text="")
gap1.grid(column=0, row=3)

calculated = ttk.Label(frame, text="Calculated", font=font.Font(underline=True))
calculated.grid(column=0, row=4, columnspan=2)

m_inv_after = ttk.Label(frame, text="Monthly Investment:  ")
m_inv_after.grid(column=0, row=5, sticky=tk.E)
m_after_text = tk.StringVar()
m_after_entry = ttk.Entry(frame, width=25, textvariable=m_after_text, state="readonly")
m_after_entry.grid(column=1, row=5)

int_rate = ttk.Label(frame, text="Interest Rate:  ")
int_rate.grid(column=0, row=6, sticky=tk.E)
int_rate_text = tk.StringVar()
int_rate_entry = ttk.Entry(frame, width=25, textvariable=int_rate_text, state="readonly")
int_rate_entry.grid(column=1, row=6)

years_prod = ttk.Label(frame, text="Years:  ")
years_prod.grid(column=0, row=7, sticky=tk.E)
years_prod_text = tk.StringVar()
years_prod_entry = ttk.Entry(frame, width=25, textvariable=years_prod_text, state="readonly")
years_prod_entry.grid(column=1, row=7)

future_value_label = ttk.Label(frame, text="Future value:  ")
future_value_label.grid(column=0, row=8, sticky=tk.E)
future_value_text = tk.StringVar()
future_value_entry = ttk.Entry(frame, width=25, textvariable=future_value_text, state="readonly")
future_value_entry.grid(column=1, row=8)

gap2 = ttk.Label(frame, text="")
gap2.grid(column=0, row=9, columnspan=2)

button1 = ttk.Button(frame, text="Calculate", command=clicked_button1)
button1.grid(column=0, row=10, columnspan=2)

window.mainloop()
