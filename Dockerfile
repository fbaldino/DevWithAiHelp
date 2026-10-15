FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pytest --version
COPY . .
CMD ["gunicorn", "-b", "0.0.0.0:5000", "hello_app:app"]
