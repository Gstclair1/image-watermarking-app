from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
from tkinter import filedialog as fd

window = Tk()
window.title('Image Watermark App')
window.minsize(height=400, width=400)
window.config(pady=30, padx=30)


def open():
    global img, filename, img_label, txt_wtm_btn, file
    open_btn.destroy()
    main_lbl.destroy()
    selected_lbl = Label(text="Image Selected:")
    selected_lbl.grid(row=0, column=1)
    filename = fd.askopenfilename(
        initialdir="/",
        title="Select A File",
        filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"))
    )
    file = Label(window, text=filename)
    file.grid(row=1, column=1)
    img = ImageTk.PhotoImage(Image.open(filename))
    img_label = Label(image=img)
    img_label.grid(row=2, columnspan=3)
    txt_wtm_btn = Button(window, text="Add Text Watermark", command=text_watermark)
    txt_wtm_btn.grid(row=3, column=1)


def text_watermark():
    txt_wtm_btn.destroy()
    watermark_text = Entry(window, font="Helvetica")
    watermark_text.grid(column=1, row=4, columnspan=2, pady=10)
    add_text_btn = Button(window, text="Add Text to Image as watermark", command=lambda: add_text(watermark_text),
                          font=("Helvetica", 8))
    add_text_btn.grid(column=1, row=5, padx=15)


def add_text(watermark_text):
    global image_to_edit
    image_to_edit = Image.open(filename)
    text_font = ImageFont.truetype("arial.ttf", 25)
    text_to_add = watermark_text.get()
    edit_img = ImageDraw.Draw(image_to_edit)
    edit_img.text((100, 175), text_to_add, "red", text_font)
    image_to_edit.save("C:/Users/Public/Pictures/wm.png")

    window.after(2000, show_pic())


def show_pic():
    file.destroy()
    new_img = ImageTk.PhotoImage(Image.open("C:/Users/Public/Pictures/wm.png"))
    img_label.config(image=new_img)
    img_label.image = new_img


main_lbl = Label(window, text="Welcome to the Image Watermark App!\nClick open image to begin!")
main_lbl.grid(row=0, column=1, columnspan=3)
open_btn = Button(window, text="Open Image", command=open)
open_btn.grid(row=2, column=1, columnspan=2, padx=20)


window.mainloop()
