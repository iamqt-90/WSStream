# WSStream

A real-time WebSocket-based streaming application with LLM integration.

## Features

- Real-time WebSocket communication
- LLM message processing with Groq integration
- Clean web interface for chat interaction
- Lightweight and fast architecture

## Project Structure

```
wsstream/
├── README.md
├── backend/
│   ├── __init__.py
│   ├── main.py              # FastAPI application with WebSocket and LLM integration
│   ├── config.py            # Configuration settings
│   └── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html          # Web interface
├── supabase_tables.sql     # Database schema (optional)
├── .env.example            # Environment variables template
├── .gitignore
└── LICENSE
```

## Setup

1. **Clone and navigate to the project:**
   ```bash
   cd wsstream
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your Groq API key and Supabase credentials
   ```

5. **Run the application:**
   ```bash
   cd backend
   python main.py
   ```

6. **Access the application:**
   Open your browser to `http://localhost:8000`

## Configuration

Edit the `.env` file with your settings:

- `GROQ_API_KEY`: Your Groq API key (free tier available)
- `SUPABASE_URL`: Your Supabase project URL
- `SUPABASE_KEY`: Your Supabase anon/public key
- `MODEL_NAME`: LLM model to use (default: llama-3.1-8b-instant)
- `HOST` and `PORT`: Server configuration

## Usage

1. Open the web interface at `http://localhost:8000`
2. Type messages in the chat input
3. Messages are processed by Groq LLM and responses are streamed back in real-time
4. Enjoy fast, intelligent conversations powered by Llama models

## API Endpoints

- `GET /`: Serves the web interface
- `WebSocket /ws`: Main WebSocket endpoint for real-time communication

## Development

The application uses:
- **FastAPI** for the web framework
- **WebSockets** for real-time communication
- **Groq API** for fast LLM processing (Llama models)
- **Vanilla JavaScript** for the frontend
- **Minimal dependencies** for optimal performance

## License

MIT License - see LICENSE file for details.
