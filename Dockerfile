FROM python:3.6.1-alpine
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENV PORT 8080
CMD ["python3","app.py"]