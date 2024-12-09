# Usar una imagen base ligera
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar y preparar las dependencias
COPY requirements.txt ./
RUN python -m venv .venv \
    && .venv/bin/pip install --no-cache-dir --upgrade pip \
    && .venv/bin/pip install --no-cache-dir -r requirements.txt

# Establecer las variables de entorno para el entorno virtual
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app/src:$PYTHONPATH"

# Definir el puerto como variable de entorno para alinearse con el archivo docker-compose
EXPOSE 8000

# ejercutar
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

