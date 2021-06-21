#!/bin/sh

echo DISCORD_TOKEN="${1}" > .envrc
pipenv run python bot.py