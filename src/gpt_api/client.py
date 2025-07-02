class GPTClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.sambanova.ai/v1/chat/completions"

    def query(self, prompt):
        import requests

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "Llama-4-Maverick-17B-128E-Instruct",  # Use exact case and spelling
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post(self.base_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")