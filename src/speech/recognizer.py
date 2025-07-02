class SpeechRecognizer:
    def __init__(self):
        pass  # No need to initialize sr.Recognizer for text input
        self.base_url = "https://api.sambanova.ai/v1/chat/completions"

    def listen(self):
        command = input("You: ")
        return command