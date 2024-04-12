
import tkinter as tk


class InterestCalculator:
    def __init__(self, parent):
        self.parent = parent
        self.principal = tk.DoubleVar()
        self.rate = tk.DoubleVar()
        self.years = tk.IntVar()
        self.amount = tk.DoubleVar()

        principal_label = tk.Label(parent, text="Principal:")
        principal_label.pack()
        principal_entry = tk.Entry(parent, textvariable=self.principal)
        principal_entry.pack()

        rate_label = tk.Label(parent, text="Rate:")
        rate_label.pack()
        rate_entry = tk.Entry(parent, textvariable=self.rate)
        rate_entry.pack()

        years_label = tk.Label(parent, text="Years:")
        years_label.pack()
        years_entry = tk.Entry(parent, textvariable=self.years)
        years_entry.pack()

        calculate_button = tk.Button(parent, text="Calculate", command=self.updateUi)
        calculate_button.pack()

        amount_label = tk.Label(parent, text="Amount:")
        amount_label.pack()
        amount_display = tk.Label(parent, textvariable=self.amount)
        amount_display.pack()

    def updateUi(self):
        p = self.principal.get()
        r = self.rate.get()
        y = self.years.get()
        amount = round(p * (1 + r / 100) ** y, 2)
        self.amount.set(amount)

        # Всплывающее окно сообщения
        popup = tk.Toplevel(self.parent)
        popup.title("Success Message")
        popup.geometry("250x100+200+200")

        success_label = tk.Label(popup, text="Расчет успешно завершен!")
        success_label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Interest Calculator")
    calculator = InterestCalculator(root)
    root.mainloop()