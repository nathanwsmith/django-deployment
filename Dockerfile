FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8080
#CMD gunicorn -c gconfig.py --log-file=- my_openshift.wsgi:application
ENTRYPOINT ["sh", "entrypoint.sh"]