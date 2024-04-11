import tkinter as tk
root = tk.Tk()
root.title("Пример grid")

label1 = tk.Label(root, text="Hello World", bg="red", fg="white")
label1.grid(row=0, column=0, sticky='nsew')

label2 = tk.Label(root, text="Меня зовут Хайрудинов Богдан", bg="red", fg="white")
label2.grid(row=1, column=1, sticky='nsew')

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=2)

root.mainloop()
#2