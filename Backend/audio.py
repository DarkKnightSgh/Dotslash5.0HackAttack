from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts_file = 'output.mp3'
    tts.save(tts_file)
    audio = AudioSegment.from_mp3(tts_file)
    play(audio)
text = "Hello, how are you?"
text_to_speech(text)
#run in virtual env
#virtualenv env
#source venv/bin/activate
#deactivate
