FROM python

ENV DISCORD_TOKEN=nothing

RUN mkdir app
COPY . app
WORKDIR app

RUN pip install pipenv
RUN pipenv install
CMD pipenv run python bot.py
