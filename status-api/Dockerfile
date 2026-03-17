
FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir flask flask-cors
COPY status_api.py .
ENV JUICY_PUBLIC_IP=104.8.77.206
ENV JUICY_PI_IP=192.168.1.73
CMD ["python", "status_api.py"]
