FROM python:alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY Definiciones.py .
CMD ["python", "Definiciones.py"]