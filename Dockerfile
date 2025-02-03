FROM python:3.9-slim

WORKDIR /app

COPY app.py /app

RUN pip install uvicorn openai fastapi pydantic

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]