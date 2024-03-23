# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import ImageTk, Image
# import numpy as np
# import torch
# from torchvision import models, transforms
# import nltk
# from nltk.tokenize import word_tokenize
# from gtts import gTTS
# import os

# # Download NLTK data if not already downloaded
# nltk.download('punkt')

# # Load pre-trained image captioning model (you need to replace this with your own model)
# # For demonstration purposes, we're using a placeholder function here
# def generate_caption(image):
#     # Placeholder function to generate a caption
#     return "A cat sitting on a table"

# # GUI class
# class ImageCaptioningApp:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Image Captioning & Speech Synthesis")

#         # Create GUI elements
#         self.label = tk.Label(self.master, text="Select an image:")
#         self.label.pack()

#         self.button_browse = tk.Button(self.master, text="Browse", command=self.load_image)
#         self.button_browse.pack()

#         self.caption_label = tk.Label(self.master, text="")
#         self.caption_label.pack()

#         self.button_generate = tk.Button(self.master, text="Generate Caption", command=self.generate_caption)
#         self.button_generate.pack()

#         self.button_speak = tk.Button(self.master, text="Speak Caption", command=self.speak_caption)
#         self.button_speak.pack()

#     # Function to load image
#     def load_image(self):
#         self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
#         if self.file_path:
#             self.image = Image.open(self.file_path)
#             self.image.thumbnail((300, 300))
#             self.photo = ImageTk.PhotoImage(self.image)
#             self.label_img = tk.Label(self.master, image=self.photo)
#             self.label_img.pack()

#     # Function to generate caption
#     def generate_caption(self):
#         if hasattr(self, 'file_path'):
#             # Load image and generate caption
#             caption = generate_caption(self.file_path)
#             self.caption_label.config(text=caption)
#         else:
#             messagebox.showwarning("Warning", "Please select an image first.")

#     # Function to speak caption
#     def speak_caption(self):
#         if hasattr(self, 'file_path'):
#             # Generate caption
#             caption = self.caption_label.cget("text")

#             # Convert caption to speech
#             tts = gTTS(text=caption, lang='en')
#             tts.save("caption.mp3")
#             os.system("start caption.mp3")  # This opens the file with the default player
#         else:
#             messagebox.showwarning("Warning", "Please generate a caption first.")


# def main():
#     root = tk.Tk()
#     app = ImageCaptioningApp(root)
#     root.mainloop()


# if __name__ == "__main__":
#     main()
import tkinter

print(tkinter.TkVersion)
