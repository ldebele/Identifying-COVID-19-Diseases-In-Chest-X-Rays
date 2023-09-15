FROM locustio/locust:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install Pillow==9.2.0

COPY . .

# EXPOSE 8089

# CMD ["locust", "-f", "locustfile.py"]