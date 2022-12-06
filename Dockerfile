FROM python:3.9

ADD main.py .

RUN pip install numpy

ENTRYPOINT ["python", "./main.py"]