FROM python:3
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 5000
COPY app.py /app
COPY . /app
CMD ["python", "app.py"]