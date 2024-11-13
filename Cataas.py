from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from pygame.display import update


def load_image(url):
    try:
        response = requests.get(url) # получен ответ на запрос по ссылке
        response.raise_for_status() # нужно для обработки исключений (здесь определяется ошибка)
        image_data = BytesIO(response.content) # контент (картинка) ответа будет обработан в BytesIO
        img = Image.open(image_data) # image_data открывается через библиотеку PIL и передаётся в img
        img.thumbnail((600, 480), Image.Resampling.LANCZOS) # картинка "подгоняется" под размер окна
                                                                    # (LANCZOS - способ конвертации)
        return ImageTk.PhotoImage(img) # функция возвращает картинку из img
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def set_image():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


window = Tk()
window.title("Cats!")
window.geometry("600x520")

label = Label()
label.pack()

update_button = Button(text="Обновить", command=set_image)
update_button.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img # чтобы сборщик мусора python не убрал картинку

set_image()

window.mainloop()
