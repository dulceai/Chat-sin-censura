FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Crear la carpeta del modelo y cambiar allí
RUN mkdir -p /workspace/model
WORKDIR /workspace/model

# Descargar el modelo desde HuggingFace (url directa)
RUN wget -L -O Wizard-Vicuna-30B-Uncensored.Q4_K_M.gguf \
  https://huggingface.co/nico02030/wizard-vicuna-30b-gguf/resolve/main/Wizard-Vicuna-30B-Uncensored.Q4_K_M.gguf


COPY . .

CMD ["python", "handler.py"]
