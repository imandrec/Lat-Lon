
FROM python:3.8-slim

WORKDIR /task

COPY task.py .
COPY .env .

RUN pip install python-dotenv
RUN pip install requests

ENTRYPOINT ["python", "task.py"]

