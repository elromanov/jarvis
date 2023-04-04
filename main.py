from modules.Speaker import Speaker

speaker = Speaker()

while True:
    text = input('Enter text: ')
    if text == '[exit]':
        break
    speaker.speak(text)