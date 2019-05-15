FROM python:3.6.7

COPY ./app /app/

WORKDIR /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]