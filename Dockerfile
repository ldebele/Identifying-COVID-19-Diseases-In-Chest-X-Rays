FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./src/api/requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src/api/ /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]