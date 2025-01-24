#Importing OpenCV, Numpy, Tkinter & Pillow
import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
from PIL import Image, ImageTk

# Creating GUI Window
root = tk.Tk()
root.configure(background="#2c2f33")
root.title("Image Editor")

# Adding Logo to Window
logo = tk.PhotoImage(file = "logo.png")
root.iconphoto(False, logo)

# Creating Heading of Application
title_label = tk.Label(text = "Image Editor", bg="#2c2f33", fg="#ffffff", font = ("Laila", 30, "bold"))  
title_label.pack()  

# Creating Canvas of Size 600x600
global canvas
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Loading and Displaying Image
def load_image():
    global img
    img_path = filedialog.askopenfilename()
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (600, 600))
    display_image()

# Displaying Image on Canvas
def display_image():
    img_tk = ImageTk.PhotoImage(Image.fromarray(img))
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas.img_tk = img_tk

#Image Processing Functions

#Blurring Image
def blur_image():
    if 'img' in globals():
        global img
        img = cv2.blur(img, (3, 3))
        display_image()
    else:
        tk.messagebox.showerror("Image Error", "Image is not Loaded")

#Saving Image
def save_image():
    if 'img' in globals():
        img_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        cv2.imwrite(img_path, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    else:
        tk.messagebox.showerror("Image Error", "Image is not Loaded")

#Sharpening Image
def sharpen_image():
    if 'img' in globals():
        global img
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        img = cv2.filter2D(img, -1, kernel)
        display_image()
    else:
        tk.messagebox.showerror("Image Error", "Image is not Loaded")

#Rotating Image
def rotate_image():
    if 'img' in globals():
        global img
        (h, w) = img.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, 90, 1.0)
        img = cv2.warpAffine(img, M, (w, h))
        display_image()
    else:
        tk.messagebox.showerror("Image Error", "Image is not Loaded")

#Cropping Image
def crop_image():
    if 'img' in globals():
        global img
        r = cv2.selectROI(img)
        crop_window = tk.Toplevel(root)
        crop_canvas = tk.Canvas(crop_window, width=r[2], height=r[3])
        crop_canvas.pack()
        crop_img = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        crop_img_tk = ImageTk.PhotoImage(Image.fromarray(crop_img))
        crop_canvas.create_image(0, 0, anchor=tk.NW, image=crop_img_tk)
        crop_canvas.img_tk = crop_img_tk
        
        def apply_crop():
            global img
            nonlocal crop_window, crop_canvas
            crop_canvas.img_tk = None  # delete reference to crop_img_tk object
            crop_window.destroy()
            cropped_img = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
            img = cv2.resize(cropped_img, (400, 400))
            display_image()

        crop_button = tk.Button(crop_window, text="Done", command=apply_crop)
        crop_button.pack()
        crop_button.configure(background="#24a0ed", foreground="#ffffff", activebackground="#4bb543", font=("Laila", 15, "bold"))
    else:
        tk.messagebox.showerror("Image Error", "Image is not Loaded")
    
#Resizing Image
def resize_image():
    if 'img' in globals():
        global img
        custom_size_width = simpledialog.askinteger("Width", "Enter the new width:")
        custom_size_height = simpledialog.askinteger("Height", "Enter the new height:")
        img = cv2.resize(img, (custom_size_width, custom_size_height))
        display_image()
    else:
        tk.messagebox.showerror("Image Error", "Image is not Loaded")

#Grayscale Image
def grayscale_image():
    if 'img' in globals():
        global img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        display_image()
    else:
        tk.messagebox.showerror("Image Error", "Image is not Loaded")

#Adding Load Image Button 
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack(side=tk.LEFT, padx=10, pady=10)
load_button.configure(background="#24a0ed", foreground="#ffffff", activebackground="#4bb543", font=("Laila", 15, "bold"))

#Adding Blur Button
blur_button = tk.Button(root, text="Blur", command=blur_image)
blur_button.pack(side=tk.LEFT, padx=10, pady=10)
blur_button.configure(background="#24a0ed", foreground="#ffffff", activebackground="#4bb543", font=("Laila", 15, "bold"))

#Adding Sharpen Button
sharpen_button = tk.Button(root, text="Sharpen", command=sharpen_image)
sharpen_button.pack(side=tk.LEFT, padx=10, pady=10)
sharpen_button.configure(background="#24a0ed", foreground="#ffffff", activebackground="#4bb543", font=("Laila", 15, "bold"))

#Adding Rotate Button
rotate_button = tk.Button(root, text="Rotate", command=rotate_image)
rotate_button.pack(side=tk.LEFT, padx=10, pady=10)
rotate_button.configure(background="#24a0ed", foreground="#ffffff", activebackground="#4bb543", font=("Laila", 15, "bold"))

#Adding Crop Button
crop_button = tk.Button(root, text="Crop", command=crop_image)
crop_button.pack(side=tk.LEFT, padx=10, pady=10)
crop_button.configure(background="#24a0ed", foreground="#ffffff", activebackground="#4bb543", font=("Laila", 15, "bold"))

#Adding Resize Button
resize_button = tk.Button(root, text="Resize", command=resize_image)
resize_button.pack(side=tk.LEFT, padx=10, pady=10)
resize_button.configure(background="#24a0ed", foreground="#ffffff", activebackground="#4bb543", font=("Laila", 15, "bold"))

#Grascale Button
grayscale_button = tk.Button(root, text="Grayscale Image", command=grayscale_image)
grayscale_button.pack(side=tk.LEFT, padx=10, pady=10)
grayscale_button.configure(background="#24a0ed", foreground="#ffffff", activebackground="#4bb543", font=("Laila", 15, "bold"))

#Adding Save Button
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(side=tk.LEFT, padx=10, pady=10)
save_button.configure(background="#24a0ed", foreground="#ffffff", activebackground="#4bb543", font=("Laila", 15, "bold"))

#Running The Application
root.mainloop()