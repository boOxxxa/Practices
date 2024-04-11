import tkinter as tk

def myClick():
    label.config(text=label.cget("text") + "\nНажата кнопка!")

root = tk.Tk()
root.title("Мое окно")

button = tk.Button(root, text="Нажми меня", bg="beige", fg="blue", command=myClick)
button.pack(pady=20)

label = tk.Label(root, text="")
label.pack()
root.mainloop()
