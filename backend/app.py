from flask import Flask, request, jsonify, render_template
from preprocess_caption import predict_caption
from flask_cors import CORS
import os
import webbrowser

# Create Flask application instance
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Corrected the syntax here

# Define the path to the templates directory
template_dir = os.path.abspath('../templates')
app = Flask(__name__, template_folder=template_dir)

# Define routes
@app.route('/')
def index():
    return render_template('mock.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'Empty image filename'}), 400

    try:
        # Save the uploaded image to a temporary directory
        upload_dir = 'uploads'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        image_path = os.path.join(upload_dir, image.filename)
        image.save(image_path)

        # Get the caption for the uploaded image
        caption = predict_caption(image_path)

        # Delete the temporary image file
        os.remove(image_path)

        print("Generated Caption:", caption)
        return jsonify({'caption': caption}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    # Open the default web browser and navigate to the appropriate URL
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)
