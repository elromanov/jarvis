from gtts import gTTS
from playsound import playsound
import pygame
from io import BytesIO

# pygame.mixer.init()

class Speaker:
    def __init__(self):
        pygame.mixer.init()
    
    def generate_file(self, text, lang='en'):
        mp3_fp = BytesIO()
        tts = gTTS(text, lang=lang)
        tts.write_to_fp(mp3_fp)
        self.mp3_fp = mp3_fp
    
    def speak(self, text, lang='en'):
        self.generate_file(text, lang)
        pygame.mixer.music.load(self.mp3_fp, 'mp3')
        pygame.mixer.music.play()