# Image Captioning Web Application

This web application allows users to generate captions for images using a deep learning model.

## Features

- Upload images: Users can upload images through the web interface.
- Caption generation: The application generates captions for the uploaded images using a pre-trained deep learning model.
- Display captions: The generated captions are displayed on the web interface for users to see.

## Technologies Used

- Frontend: React.js
- Backend: Flask (Python)
- Deep Learning Framework: TensorFlow/Keras, Tesseract OCR, ViT
- Image Processing: PIL (Python Imaging Library)

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd image-captioning-web-app
```
2. Frontend dependencies
```
cd frontend
npm install
```
3. Backend dependencies
```
cd ../backend
python app.py
```
## Access the Web Application

Open your web browser and navigate to [http://localhost:3000](http://localhost:3000) to access the web application.

## Usage

1. **Upload Image**: Click on the "Choose File" button to select an image from your local filesystem.

2. **Generate Caption**: After selecting an image, click on the "Upload" button to generate a caption for the image.

3. **View Caption**: The generated caption will be displayed on the web page below the uploaded image.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

