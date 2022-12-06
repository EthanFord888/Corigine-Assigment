FROM python:3.9

#WORKDIR /code

ADD main.py .

#COPY ./requirements.txt /code/requirements.txt

RUN pip install numpy

#COPY ./Ethan_Fibonacci.py /code/Ethan_Fibonacci.py

ENTRYPOINT ["python", "./main.py"]