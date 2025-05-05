# LLM-stream

A minimal Python-based application for streaming interactions with Large Language Models (LLMs) via a simple API. This project is designed for easy local deployment and experimentation with LLM streaming outputs.

## Features

- Stream LLM responses in real-time
- Lightweight and easy to deploy (Docker support included)
- Simple API interface for sending prompts and receiving streamed completions

## Repository Structure

- `app.py` - Main application code (likely a FastAPI or Flask app exposing the streaming endpoint)
- `Dockerfile` - Containerization support for easy deployment
- `README.md` - Project documentation

## Getting Started

### Prerequisites

- Python 3.8+
- (Optional) Docker

### Running Locally

1. **Clone the repository:**
```bash
1. git clone https://github.com/GitAvi001/LLM-stream.git
2. cd LLM-stream
```

2. **Install dependencies:**
```bash
1. pip install -r requirements.txt
```

3. **Start the application:**
```bash
python app.py
```

4. **Access the API:**  
The API will typically be available at `http://localhost:8000` or as specified in `app.py`.

### Running with Docker

1. **Build the Docker image:**
```bash
docker build -t llm-stream .
```

2. **Run the container:**
```bash
docker run -p 8000:8000 llm-stream
```

## Usage

- Send a POST request to the API endpoint (e.g., `/stream`) with your prompt.
- The server will stream the LLM's response as it generates output.

Example command:
```bash
curl -X POST "http://localhost:8000/stream" -H "Content-Type: application/json" -d '{"prompt": "Tell me a joke."}'
```


