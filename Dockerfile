FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "cleaner_robot.py", "/app/tests/backforththensmall-21810.txt"]
