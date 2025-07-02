# This is the entry point of the AI assistant application.

from assistant import Assistant
from gpt_api.client import GPTClient
from speech.recognizer import SpeechRecognizer
from speech.synthesizer import SpeechSynthesizer
import os
from dotenv import load_dotenv  # Add this import

def main():
    load_dotenv()  # Load variables from .env file
    api_key = os.getenv("GPT_API_KEY")
    if not api_key:
        raise ValueError("GPT_API_KEY environment variable not set.")
    gpt_client = GPTClient(api_key)
    speech_recognizer = SpeechRecognizer()
    speech_synthesizer = SpeechSynthesizer()
    assistant = Assistant(gpt_client, speech_recognizer, speech_synthesizer)
    assistant.start()

if __name__ == "__main__":
    main()