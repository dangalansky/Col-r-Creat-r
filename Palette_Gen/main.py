from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import cv2


# ------------ GUI ------------- #
window = Tk()
window.title('COL\'R || CREAT\'R')
window.geometry('800x800')

# ------------Background------------- #
canvas = Canvas(height=800, width=800, bg='black', highlightthickness=0)
# background = Image.open('')
# background_sm = background.resize((740, 675), Image.ANTIALIAS)
# watermarker_app = ImageTk.PhotoImage(background_sm)
# canvas.create_image(280, 310, image=watermarker_app)
canvas.place(x=0, y=0)
frame = Frame(window, width=400, height=400)
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open('/Users/dangalansky/Documents/Headshots/linked_in_profile_pic.png'))
label = Label(frame, image=img)
label.pack()






# ----------- Functions ------------ #
# def open_photo():
#     global label
#     # filename = filedialog.askopenfilename(initialdir='/', title='Choose A File',
#     #                                       filetypes=(('png files', '*.png'), ('jpg files', '*.jpg')))
#
#     img = Image.open(f"'{filename}'")
#     re_img = img.resize((400,400))
#     img = ImageTk.PhotoImage(re_img)
#     label.config(image=img)




# photo = StringVar(None)
# photo_entry = Entry(window, textvariable=photo, width=30, highlightthickness=0)
# photo_entry.place(x=170, y=490)
# open_photo = Button(window, text='Select', borderwidth=0, highlightbackground='#000000',
#                     command=open_photo).place(x=275, y=515)







window.mainloop()
