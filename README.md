# AI Assistant Project

This project is an AI assistant similar to Jarvis that utilizes a free GPT API and has the capability to respond verbally.

## Features

- Voice recognition to capture user commands.
- Text-to-speech functionality to respond to users.
- Integration with a GPT API for intelligent responses.
- Simple command-line interface for user interaction.

## Project Structure

```
ai-assistant
├── src
│   ├── main.py          # Entry point of the application
│   ├── assistant.py     # Contains the Assistant class
│   ├── speech
│   │   ├── recognizer.py # Handles voice input
│   │   └── synthesizer.py # Handles voice output
│   ├── gpt_api
│   │   └── client.py     # Interacts with the GPT API
│   └── utils
│       └── config.py     # Configuration settings
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-assistant
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Follow the on-screen instructions to interact with the AI assistant.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.