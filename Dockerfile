FROM python:3.9-slim

WORKDIR /test_task

COPY requirements.txt /test_task

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /test_task

EXPOSE 5001

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
