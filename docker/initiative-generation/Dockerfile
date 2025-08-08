FROM python:3.11-slim
WORKDIR /app
COPY requirements/backend.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
CMD ["uvicorn", "src.agents.cyber.initiative_generation_service:app", "--host", "0.0.0.0", "--port", "8000"]
