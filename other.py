from PIL import Image, ImageDraw, ImageFont
from tkinter import *
from tkinter import filedialog
import PIL.Image

window = Tk()
window.title("add watermark")
window.minsize(width=600, height=300)
window.config(padx=30, pady=30)




def add_watermark(image, wm_text):
    opened_image = PIL.Image.open(image)
    image_width, image_height = opened_image.size
    Draw = ImageDraw.Draw(opened_image)
    font_size = int(image_width / 8)
    font = ImageFont.truetype('arial.ttf', font_size)
    x, y = int(image_width / 2),  int(image_height / 2)
    Draw.text((x,y), wm_text, font=font, fill="#fff", anchor="ms")
    opened_image.show()




def done():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg")])
    window.withdraw()
    add_watermark(image=filename,wm_text="Mohamed Ayman")


main_label = Label(text="add watermark to your photo")
main_label.grid(row=1, column=1, columnspan=1)

add_button = Button(text="add watermark", command=done)
add_button.grid(row=2, column=1)

window.mainloop()