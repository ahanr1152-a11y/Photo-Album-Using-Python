import tkinter as tk
import time
from PIL import Image, ImageTk

# Main Application Window
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

# List of Image Paths
image_paths = [
    r"C:\Users\AHANRAJ\OneDrive\Pictures\01 gettyimages-1129788053_resized.jpg",
    r"C:\Users\AHANRAJ\OneDrive\Pictures\IMG_20260228_011940.jpg",
    r"C:\Users\AHANRAJ\OneDrive\Pictures\IMG_20260329_125630.jpg",
    r"C:\Users\AHANRAJ\OneDrive\Pictures\IMG-20260212-WA0079.jpg",
    r"C:\Users\AHANRAJ\OneDrive\Pictures\IMG-20260212-WA0123.jpg",
    r"C:\Users\AHANRAJ\OneDrive\Pictures\IMG-20260212-WA0169.jpg"
]

# Resize images
image_size = (700, 700)
images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)

# Convert PIL Images into Tkinter Compatible Image
final_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

# Label widget to keep photo
image_label = tk.Label(root)
image_label.pack(pady=30)

# Slideshow Function
def slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image = photo
        root.update()
        time.sleep(2)

# Button
play_button = tk.Button(
    root,
    text="Play the Slideshow",
    font=("Arial", 17),
    command=slideshow
)
play_button.pack(pady=40)

root.mainloop()
