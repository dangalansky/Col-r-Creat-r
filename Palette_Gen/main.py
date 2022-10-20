from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image, ImageOps
import cv2
from collections import Counter
from sklearn.cluster import KMeans
import pyperclip as pc

# ------------ GUI ------------- #
window = Tk()
window.title('COL\'R || CREAT\'R')
window.geometry('800x800')

# ------------Background------------- #
canvas = Canvas(height=2000, width=2000, bg='#55c3f7', highlightthickness=0)
background = Image.open('bg.jpg')
bg = ImageTk.PhotoImage(background)
canvas.create_image(400, 390, image=bg)
canvas.place(x=0, y=0)

# ------------Image Uploaded---------- #
picture_frame = Frame(window, height=400, width=400)
picture_frame.place(x=200, y=180)
img = ImageTk.PhotoImage(Image.open('1.jpg'))
photo = Label(picture_frame, image=img, anchor='center')
photo.pack()

# ------------Hex Palette---------- #
hexframe = Frame(window, height=150, width=700, bg='#55c3f7')
hex0 = Frame(hexframe, height=100, width=100, bg='#FFFFFF')
hex0_txt = Button(hexframe, text="#FFFFFF", font=("Arial", 10), anchor='center', bg="#55c3f7", fg="#000000",
                  highlightbackground='#55c3f7', command=lambda: txt_print(hex0_txt.cget('text')))
hex1 = Frame(hexframe, height=100, width=100, bg='#FFFFFF')
hex1_txt = Button(hexframe, text="#FFFFFF", font=("Arial", 10), anchor='center', bg="#55c3f7", fg="#000000",
                  highlightbackground='#55c3f7', command=lambda: txt_print(hex1_txt.cget('text')))
hex2 = Frame(hexframe, height=100, width=100, bg='#FFFFFF')
hex2_txt = Button(hexframe, text="#FFFFFF", font=("Arial", 10), anchor='center', bg="#55c3f7", fg="#000000",
                  highlightbackground='#55c3f7', command=lambda: txt_print(hex2_txt.cget('text')))
hex3 = Frame(hexframe, height=100, width=100, bg='#FFFFFF')
hex3_txt = Button(hexframe, text="#FFFFFF", font=("Arial", 10), anchor='center', bg="#55c3f7", fg="#000000",
                  highlightbackground='#55c3f7', command=lambda: txt_print(hex3_txt.cget('text')))
hex4 = Frame(hexframe, height=100, width=100, bg='#FFFFFF')
hex4_txt = Button(hexframe, text="#FFFFFF", font=("Arial", 10), anchor='center', bg="#55c3f7", fg="#000000",
                  highlightbackground='#55c3f7', command=lambda: txt_print(hex4_txt.cget('text')))
hexframe.place(x=120, y=625)
hex0.grid(row=0, column=0, padx=5)
hex0_txt.grid(row=1, column=0, pady=1)
hex1.grid(row=0, column=1, padx=5)
hex1_txt.grid(row=1, column=1, pady=1)
hex2.grid(row=0, column=2, padx=5)
hex2_txt.grid(row=1, column=2, pady=1)
hex3.grid(row=0, column=3, padx=5)
hex3_txt.grid(row=1, column=3, pady=1)
hex4.grid(row=0, column=4, padx=5)
hex4_txt.grid(row=1, column=4, pady=1)


# ----------- Functions ------------ #
def open_photo():
    global photo
    filename = filedialog.askopenfilename(initialdir='/', title='Choose A File',
                                          filetypes=(('png files', '*.png'), ('jpg files', '*.jpg')))
    image_filepath.set(filename)
    image = Image.open(filename)
    if image.size[0] > 400 or image.size[1] > 400:
        image = ImageOps.pad(image, (400, 400), centering=(0.5, 0.5), color="#55c3f7")
    image = ImageTk.PhotoImage(image)
    photo.configure(image=image)
    photo.image = image


def cv_photo(img_path):
    if img_path == '':
        messagebox.showinfo(title='Error!', message='Please select Image!')
    else:
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        prep_image(image)


# taken from Behic Guven
def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation=cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0] * modified_img.shape[1], 3)
    color_analysis(modified_img)


# taken from Behic Guven
def color_analysis(img):
    clf = KMeans(n_clusters=5)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    hex_list = [hex0, hex1, hex2, hex3, hex4]
    hex_txt_list = [hex0_txt, hex1_txt, hex2_txt, hex3_txt, hex4_txt]
    for color in hex_colors:
        n = hex_colors.index(color)
        txt_edit = hex_txt_list[n]
        txt_edit.config(text=color)
        hex_edit = hex_list[n]
        hex_edit.config(bg=color)


def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color


def txt_print(text):
    pc.copy(text)
    messagebox.showinfo(title='Success!', message='Hexadecimal code copied to clipboard!')


# ----------- Buttons/Mainloop ------------ #

# Choose Photo Button
Button(window, text='Choose Photo', borderwidth=0, highlightbackground='#55c3f7',
       command=open_photo).place(x=50, y=515)

# Store Filepath in StringVar
image_filepath = StringVar(None)

# Create Palette Button
Button(window, text='Create Palette', borderwidth=2, highlightbackground='#55c3f7',
       command=lambda: cv_photo(image_filepath.get())).place(x=635, y=515)

window.mainloop()
