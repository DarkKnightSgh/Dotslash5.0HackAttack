from flask import Flask, request, jsonify
from preprocess_caption import predict_caption
from flask_cors import CORS
import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Create Flask application instance
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Define routes
@app.route('/')
def index():
    return "Hello, World!"

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

        # Convert caption to audio
        caption = "".join(caption)
        tts = gTTS(text=caption, lang='en')
        tts_file = 'output.mp3'
        tts.save(tts_file)
        print("Audio file generated successfully.")

        # Play the audio
        audio = AudioSegment.from_mp3(tts_file)
        play(audio)
        
        return jsonify({'caption': caption}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
