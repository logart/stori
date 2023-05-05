FROM python:alpine3.17

COPY main.py /home/main.py
COPY requirements.txt /home/requirements.txt

RUN pip3 install -r /home/requirements.txt

EXPOSE 8000
WORKDIR /home
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
