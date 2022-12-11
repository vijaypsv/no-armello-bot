FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app/bot
WORKDIR /app/bot

COPY . .
RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]