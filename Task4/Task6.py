import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

# Создаем главное окно
root = tk.Tk()
root.title("Галерея фотографий")
file = Path("test_axe.ico").resolve()
root.iconbitmap(file)
# Создаем список файлов изображений
image_files = ["image1.jpg", "image2.jpg", "image3.jpg"]

# Создаем список объектов-фотографий
photos = []
for file in image_files:
    image = Image.open(file)  # Открываем изображение
    photo = ImageTk.PhotoImage(image)  # Создаем объект PhotoImage
    photos.append(photo)

# Функция для пролистывания фотографий вперед
def forward(image_number):
    global photo_label
    global button_forward
    global button_back

    photo_label.grid_forget()  # Убираем текущее изображение с сетки
    photo_label = tk.Label(image=photos[image_number - 1])  # Создаем новый Label с новым изображением
    button_forward = tk.Button(root, text=">", command=lambda: forward(image_number + 1))
    button_back = tk.Button(root, text="<", command=lambda: back(image_number - 1))

    if image_number == len(photos):
        button_forward = tk.Button(root, text=">", state=tk.DISABLED)

    photo_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    button_back.grid(row=1, column=0, padx=5, pady=5)
    button_forward.grid(row=1, column=2, padx=5, pady=5)
    update_info(image_number)

# Функция для пролистывания фотографий назад
def back(image_number):
    global photo_label
    global button_forward
    global button_back

    photo_label.grid_forget()  # Убираем текущее изображение с сетки
    photo_label = tk.Label(image=photos[image_number - 1])  # Создаем новый Label с новым изображением
    button_forward = tk.Button(root, text=">", command=lambda: forward(image_number + 1))
    button_back = tk.Button(root, text="<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = tk.Button(root, text="<", state=tk.DISABLED)

    photo_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    button_back.grid(row=1, column=0, padx=5, pady=5)
    button_forward.grid(row=1, column=2, padx=5, pady=5)
    update_info(image_number)

# Функция для обновления информации о текущей фотографии
def update_info(image_number):
    info_label.config(text=f"Фотография {image_number} из {len(photos)}")

# Создаем виджет Label для отображения текущей фотографии
photo_label = tk.Label(root, image=photos[0])
photo_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Создаем кнопки для пролистывания фотографий и выхода из программы
button_back = tk.Button(root, text="<", command=lambda: back(1), state=tk.DISABLED)
button_back.grid(row=1, column=0, padx=5, pady=5)

button_forward = tk.Button(root, text=">", command=lambda: forward(2))
button_forward.grid(row=1, column=2, padx=5, pady=5)

button_quit = tk.Button(root, text="Выход", command=root.quit)
button_quit.grid(row=2, column=1, pady=10)

# Создаем виджет Label для отображения информации о текущей фотографии
info_label = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.E)
info_label.grid(row=2, column=0, columnspan=3, sticky=tk.W+tk.E, padx=10, pady=5)
update_info(1)

# Запускаем главный цикл обработки событий
root.mainloop()