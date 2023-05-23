FROM python:3.9

COPY ./src /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt --no-deps

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--port", "8000", "--reload"]