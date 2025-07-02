class SpeechSynthesizer:
    def __init__(self):
        # Initialize the text-to-speech engine
        import pyttsx3
        self.engine = pyttsx3.init()

    def speak(self, text):
        # Convert the text to speech
        self.engine.say(text)
        self.engine.runAndWait()