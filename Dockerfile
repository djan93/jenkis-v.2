FROM python:3.6.7

COPY . /usr/app

WORKDIR /usr/app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]