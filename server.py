# server.py
# Main entry point for the Flask backend API

from flask import Flask, request, jsonify           # Import Flask and helpers for API
from flask_cors import CORS                         # Import CORS for cross-origin requests
from src.gpt_api.client import GPTClient            # Import GPTClient to interact with AI API
import os                                           # For environment variable access
from dotenv import load_dotenv                      # For loading .env file

load_dotenv()                                       # Load environment variables from .env
api_key = os.getenv("GPT_API_KEY")                  # Get GPT API key from environment
gpt_client = GPTClient(api_key)                     # Initialize GPT client with API key

app = Flask(__name__)                               # Create Flask app instance

# Allow requests from your GitHub Pages frontend (CORS)
CORS(app, origins=[
    "https://krishna20072007.github.io",
    "https://krishna20072007.github.io/ai-assistant",
    "https://krishna20072007.github.io/ai-assistant/"
])

print("API KEY:", os.getenv("GPT_API_KEY"))         # Print API key for debugging (remove in prod)

@app.route('/api/chat', methods=['GET', 'POST'])    # Define /api/chat endpoint for GET and POST
def chat():
    if request.method == 'GET':
        # Simple check endpoint
        return jsonify({'reply': "GET method works!"})
    
    data = request.get_json()                       # Parse JSON from POST request
    user_message = data.get('message', '')          # Get user message from request
    if not user_message:
        return jsonify({'reply': "No message received."}), 400
    try:
        ai_reply = gpt_client.query(user_message)   # Get AI response from GPTClient
        return jsonify({'reply': ai_reply})         # Return AI reply as JSON
    except Exception as e:
        return jsonify({'reply': f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app (for local development only)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

