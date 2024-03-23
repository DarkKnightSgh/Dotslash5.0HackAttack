import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch

# Load pre-trained model and tokenizer
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# Set device (GPU if available, otherwise CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Generation parameters
max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

def predict_caption(image_path):
    # Load image and preprocess
    image = Image.open(image_path)
    if image.mode != "RGB":
        image = image.convert("RGB")
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values.to(device)
    
    # Generate caption
    output_ids = model.generate(pixel_values, **gen_kwargs)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds[0] if preds else "Unable to generate caption"

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        caption = predict_caption(file_path)
        return caption
    else:
        return None

def update_caption():
    caption = select_image()
    if caption is not None:
        caption_label.config(text="Caption: " + caption)
    else:
        caption_label.config(text="")

# Create GUI
root = tk.Tk()
root.title("Image Captioning App")

# GUI elements
label = tk.Label(root, text="Select an image to generate a caption", padx=10, pady=10)
label.pack()

button = tk.Button(root, text="Select Image", command=update_caption)
button.pack()

caption_label = tk.Label(root, text="", padx=10, pady=10, wraplength=400)
caption_label.pack()

root.mainloop()
