FROM python:3

MAINTAINER Mike Peters "mike@skylake.me"

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY ./discord_world_time_bot.py /discord_world_time_bot.py
WORKDIR /

CMD ["python", "discord_world_time_bot.py"]