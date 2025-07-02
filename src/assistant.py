class Assistant:
    def __init__(self, gpt_client, speech_recognizer, speech_synthesizer):
        self.gpt_client = gpt_client
        self.speech_recognizer = speech_recognizer
        self.speech_synthesizer = speech_synthesizer

    def start(self):
        print("AI: Hello, I am your AI assistant. How can I help you today?")  # Print to terminal
        self.speech_synthesizer.speak("Hello, I am your AI assistant. How can I help you today?")
        while True:
            user_input = self.speech_recognizer.listen()
            if user_input.lower() in ["exit", "quit"]:
                self.speech_synthesizer.speak("Goodbye!")
                break
            response = self.respond(user_input)
            print(f"AI: {response}")  # <-- Show AI message in terminal
            self.speech_synthesizer.speak(response)

    def respond(self, user_input):
        response = self.gpt_client.query(user_input)
        return response