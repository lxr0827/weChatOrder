FROM python:3.4.2

RUN apt-get update
RUN apt-get install python-setuptools
RUN easy_install pip


RUN mkdir /code
WORKDIR /code
ONBUILD COPY requirements.txt /code/
ONBUILD RUN pip install -r requirements.txt
ONBUILD COPY . /code

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
