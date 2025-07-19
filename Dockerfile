# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar requerimientos e instalar
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar aplicación
COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/service-account.json

# Puerto
EXPOSE 5001

# Ejecutar aplicación
CMD ["python", "app.py"]
