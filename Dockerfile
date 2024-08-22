FROM python:3.9-slim

WORKDIR /testTask

COPY requirements.txt /testTask

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /testTask

EXPOSE 5001

ENV FLASK_APP=index.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
