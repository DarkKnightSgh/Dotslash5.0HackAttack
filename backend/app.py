from flask import Flask, request, jsonify, send_file
from preprocess_caption import predict_caption
from flask_cors import CORS
import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'Empty image filename'}), 400

    try:
        upload_dir = 'uploads'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        image_path = os.path.join(upload_dir, image.filename)
        image.save(image_path)

        caption = predict_caption(image_path)

        os.remove(image_path)

        print("Generated Caption:", caption)
        
        # Convert list of caption tokens to a single string
        caption = " ".join(caption)
        # Remove square brackets if present
        caption1 = caption.strip('[]')

        # Write the caption to a text file
        with open('../frontend/public/caption.txt', 'w') as f:
            f.write(caption1)

        # Convert caption to audio
        tts = gTTS(text=caption, lang='en')
        tts_file = 'output.mp3'
        tts.save(tts_file)
        print("Audio file generated successfully.")

        # Play the audio
        audio = AudioSegment.from_mp3(tts_file)
        play(audio)

        # Return caption as part of JSON response
        return jsonify({'caption': caption}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
