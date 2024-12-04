from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url) # Отправляем GET-запрос с использованием requests.get() и получаем ответ на запрос по ссылке
        response.raise_for_status() # Проверяем успешность запроса (код ответа 200) - нужно для обработки исключений
        image_data = BytesIO(response.content) # Читаем байты из ответа в объект BytesIO, контент (картинка) ответа обрабатывается в BytesIO
        img = Image.open(image_data) # image_data открывается через библиотеку PIL и передаётся в img
        img.thumbnail((600, 480), Image.Resampling.LANCZOS) # картинка "подгоняется" под размер окна (LANCZOS - способ конвертации)
        return ImageTk.PhotoImage(img) # функция возвращает картинку из img
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def open_new_window():
    img = load_image(url)
    if img:
        # Создаем новое вторичное окно
        new_window = Toplevel()
        new_window.title("Фото кошки (кота)")
        new_window.geometry("600x480")

        # Добавляем изображение в новое окно
        label = Label(new_window, image=img)
        label.image = img  # Сохраняем ссылку на изображение
        label.pack()


def exit_app():
    window.destroy()


window = Tk()
window.title("Cats!")
window.geometry("200x100")

# Создаем меню
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Добавляем пункты меню
file_menu = Menu(menu_bar, tearoff=0) # tearoff - чтобы зафиксировать меню
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)

# кнопка вызова функции загрузки
update_button = Button(text="Загрузить", pady=20, command=open_new_window)
update_button.pack()

url = "https://cataas.com/cat"

window.mainloop()
