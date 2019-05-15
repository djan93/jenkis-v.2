FROM python:3.6.7

COPY . /app

WORKDIR /app

RUN pip3 install -r /app/requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
