from flask import Flask, request, jsonify
from flask_cors import CORS
from src.gpt_api.client import GPTClient
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GPT_API_KEY")
gpt_client = GPTClient(api_key)

app = Flask(__name__)
CORS(app)

print("API KEY:", os.getenv("GPT_API_KEY"))

@app.route('/api/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return jsonify({'reply': "GET method works!"})
    
    data = request.get_json()
    user_message = data.get('message', '')
    if not user_message:
        return jsonify({'reply': "No message received."}), 400
    try:
        ai_reply = gpt_client.query(user_message)
        return jsonify({'reply': ai_reply})
    except Exception as e:
        return jsonify({'reply': f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()

