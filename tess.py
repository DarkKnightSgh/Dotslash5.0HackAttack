import pytesseract
from PIL import Image

# Open an image file
image = Image.open('text.png')

# Perform OCR on the image and get detailed results
ocr_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

# Filter out text below a certain confidence threshold
filtered_text = [word for word, conf in zip(ocr_data['text'], ocr_data['conf']) if conf >= 80]  # Adjust confidence threshold as needed

# Print the extracted captions
for word in filtered_text:
    print(word)
