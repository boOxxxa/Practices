import tkinter as tk
from MainWindow import MainWindow

# Создаем объект Tk
root = tk.Tk()
root.title("Integerst")  # Устанавливаем заголовок окна

# Устанавливаем иконку окна
#icon = tk.PhotoImage(file="interest.ico")
#root.iconphoto(True, icon)

# Создаем объект MainWindow
window = MainWindow(root)

# Запускаем главный цикл обработки событий
root.mainloop()