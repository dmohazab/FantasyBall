
FROM python:3.7-stretch

COPY . /fantasy_ball
WORKDIR /fantasy_ball

#supervisord is used when we need to run multiple process within the container, omitted for now

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["waitress_server.py"]