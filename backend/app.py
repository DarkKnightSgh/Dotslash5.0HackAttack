from flask import Flask, request, jsonify, render_template,send_file
from preprocess_caption import predict_caption
from flask_cors import CORS
import os
import webbrowser
from flask import send_file

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Create Flask application instance
app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "*"}})  
caption_global=""
# Define the path to the templates directory
# template_dir = os.path.abspath('../templates')
# app = Flask(__name__, template_folder=template_dir)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
# Define routes
@app.route('/')


@app.route('/upload', methods=['POST'])
def upload_file():
    global caption_global
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
        caption_global=predict_caption(image_path)
        # Delete the temporary image file
        os.remove(image_path)
        
        print("Generated Caption:", caption)
        
        caption="".join(caption)
        caption_global = ''.join(caption).strip('[]')

        # with open('../frontend/public/caption.txt', 'w') as f:
        #     f.write(caption1)

        tts = gTTS(text=caption, lang='en')
        tts_file = 'output.mp3'
        tts.save(tts_file)
        audio = AudioSegment.from_mp3(tts_file)
        play(audio)
        return jsonify({'caption': caption}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/caption', methods=['GET'])
def get_caption():
    # Code to retrieve the caption (e.g., from a file or database)
    caption = caption_global
    return jsonify({'caption': caption})
# @app.route('/caption', methods=['GET'])
# def get_caption():
#     try:
#         with open('caption.txt', 'r') as file:
#             caption_content = file.read()
#             print("This is the caption:", caption_content)
#         return send_file('caption.txt')
#     except FileNotFoundError:
#         return "Caption file not found"

    #conclusion: not getting called by the frontend properly
        
    

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
