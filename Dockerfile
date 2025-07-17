# Imagen base de Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar requerimientos e instalar
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar aplicación
COPY . .

# Puerto
EXPOSE 5000

# Ejecutar aplicación
CMD ["python", "app.py"]
