FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir  -r requirements.txt
COPY 04_JSON ./04_JSON
CMD ["python", "04_JSON/jsonexperiment.py"]