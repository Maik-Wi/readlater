# Verwende Python als Basisimage
FROM python:3.10-slim

# Arbeitsverzeichnis festlegen
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Anwendung kopieren
COPY . .

# Anwendung starten
CMD ["python", "app.py"]
