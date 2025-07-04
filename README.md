# AI Assistant Chat

A modern, mobile-friendly AI chat assistant web app with a Flask backend and a static HTML/Tailwind frontend.  
Frontend is deployable on GitHub Pages, backend on Render or any cloud Python host.

---

## Features

- **Monochrome, responsive UI** with dark/light mode toggle
- **Mobile-optimized** with hamburger menu for sidebar
- **Typewriter effect** for AI messages
- **Multi-chat support** (sidebar)
- **Backend**: Flask API with CORS, ready for cloud deployment
- **Frontend**: Static HTML/JS, deployable anywhere

---

## Folder Structure

```
ai-assistant/
│
├── index.html           # Main frontend (static)
├── requirements.txt     # Backend Python dependencies
├── Procfile             # For Render/Heroku deployment
├── .env                 # (local only) API keys
├── server.py            # Flask backend
└── src/
    ├── gpt_api/
    │   └── client.py    # GPTClient class for AI API
    └── utils/
        └── config.py    # (optional) config
```

---

## 1. Frontend (Static)

### How to Run Locally

1. Open `index.html` in your browser (double-click or use Live Server in VS Code).

### How to Deploy (GitHub Pages)

1. Push `index.html` to a public GitHub repo.
2. Go to **Settings > Pages** in your repo.
3. Set source to `main` branch, `/ (root)`.
4. Your site will be live at:  
   `https://your-username.github.io/your-repo/`

### Configuration

- **Backend URL**:  
  In `index.html`, update the fetch URL to your deployed backend:
  ```js
  fetch('https://your-backend-service.onrender.com/api/chat', { ... })
  ```

---

## 2. Backend (Flask API)

### How to Run Locally

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Set your API key in `.env`:
   ```
   GPT_API_KEY=your-key-here
   ```
3. Run the server:
   ```sh
   python server.py
   ```
4. Test:  
   Visit [http://127.0.0.1:5000/api/chat](http://127.0.0.1:5000/api/chat)

### How to Deploy (Render)

1. Push your backend code to a new GitHub repo.
2. Go to [Render](https://render.com/), create a new **Web Service**.
3. Connect your repo.
4. Set **build command**: *(leave blank for Python)*
5. Set **start command**:  
   ```
   gunicorn server:app
   ```
6. Add environment variable:  
   - Key: `GPT_API_KEY`
   - Value: your API key
7. Deploy!

### CORS

- The backend uses:
  ```python
  CORS(app, origins=[
      "https://your-username.github.io",
      "https://your-username.github.io/your-repo",
      "https://your-username.github.io/your-repo/"
  ])
  ```
- Adjust to match your frontend URL.

---

## 3. Connecting Frontend & Backend

- The frontend sends POST requests to `/api/chat` on your backend.
- The backend expects JSON: `{ "message": "your text" }`
- The backend replies with `{ "reply": "AI response" }`

---

## 4. Mobile Optimization

- Sidebar is hidden on mobile, toggled with a hamburger menu.
- Responsive paddings and layout for all screen sizes.

---

## 5. Customization

- **AI Model**:  
  Edit `src/gpt_api/client.py` to use your preferred AI API.
- **Welcome Message**:  
  Change in the `chats` array in `index.html`.

---

## 6. Troubleshooting

- **"Could not reach backend"**:  
  - Check your fetch URL in `index.html`.
  - Make sure your backend is deployed and CORS allows your frontend.
  - Check browser console and Render logs for errors.

- **CORS errors**:  
  - Update the `origins` list in `server.py` to match your frontend URL.

- **API key issues**:  
  - Ensure `GPT_API_KEY` is set in Render's environment variables.

---

## 7. Example `.env` (for local dev only)

```
GPT_API_KEY=your-api-key-here
```

---

## 8. Example `requirements.txt`

```
flask
flask-cors
python-dotenv
requests
gunicorn
```

---

## 9. Example `Procfile`

```
web: gunicorn server:app
```

---

## 10. License

MIT

---