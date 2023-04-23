FROM python:3.11.3

WORKDIR /outageapp

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python","./main.py"]
