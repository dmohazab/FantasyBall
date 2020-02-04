
FROM python:3.7-stretch

COPY . /fantasy_ball
WORKDIR /fantasy_ball

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["waitress_server.py"]