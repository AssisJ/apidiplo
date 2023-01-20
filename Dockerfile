FROM python:3.8-slim
ENV PORT=8000
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . ./

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port $PORT
