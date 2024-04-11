import tkinter as tk

def myClick():
    label.config(text=label.cget("text") + "\nНажата кнопка!")

# Создаем главное окно
root = tk.Tk()
root.title("Мое окно")

# Создаем кнопку с обработчиком myClick
button = tk.Button(root, text="Нажми меня", bg="beige", fg="blue", command=myClick)
button.pack(pady=20)

# Создаем Label для отображения текста
label = tk.Label(root, text="")
label.pack()

# Запускаем главный цикл обработки событий
root.mainloop()