
import tkinter as tk
from tkinter import messagebox
def show_message():
    name = entry.get()
    if name.strip() == "":
        messagebox.showerror("Ошибка", "Пожалуйста, введите ваше имя!")
    else:
        message = f"Привет, {name}!"
        messagebox.showinfo("Приветствие", message)


root = tk.Tk()
root.title("Пример с Entry и кнопкой")

root.configure(bg='light gray')
root.geometry("400x150")
entry = tk.Entry(root, width=50, bg='blue', fg='white', bd=5)  # bd - ширина границ
entry.insert(0, " ")
entry.pack(pady=10)


button = tk.Button(root, text="Показать приветствие", command=show_message, bg='beige', font=('Arial', 14))
button.pack(pady=10)
root.mainloop()
