FROM python

ARG DISCORD_TOKEN

RUN mkdir app
COPY . app
WORKDIR app

RUN pip install pipenv
RUN pipenv install
CMD pipenv run python bot.py
