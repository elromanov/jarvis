from modules.Speaker import Speaker
from modules.Transformer import Transformer

speaker = Speaker()
transformer = Transformer()

while True:
    input_text = input('Enter text: ')
    if input_text == '[exit]':
        break
    text = transformer.askTransformer(input_text)
    print(text)
    speaker.speak(text)