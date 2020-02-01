FROM python:3.7-stretch

# Install Supervisord
RUN pip install uwsgi

RUN apt-get update && apt-get install -y supervisor

# Copy start.sh script that will check for a /app/prestart.sh script and run it before starting the app
COPY start.sh /start.sh
RUN chmod +x /start.sh

RUN mkdir /fantasy_ball
COPY . /fantasy_ball
WORKDIR /fantasy_ball

# Custom Supervisord config
COPY supervisord.ini /etc/supervisor.d/supervisord.ini
COPY supervisord.ini /etc/supervisord.conf
COPY supervisord.ini /etc/supervisor/conf.d/supervisord.ini

# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["waitress_server.py"]
EXPOSE 80