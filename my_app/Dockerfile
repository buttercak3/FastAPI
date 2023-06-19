FROM python:3.11.4

WORKDIR /fastapi/app
COPY ./requirements.txt /fastapi/requirements.txt
COPY ./app /fastapi/app

RUN pip install --no-cache-dir -r ../requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]