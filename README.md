[![Build Status](https://travis-ci.org/darkaico/strava-viewer.svg?branch=master)](https://travis-ci.org/darkaico/strava-viewer)
[![Coverage Status](https://coveralls.io/repos/github/darkaico/strava-viewer/badge.svg?branch=master)](https://coveralls.io/github/darkaico/strava-viewer?branch=master)

# Strava Extensions

App that fetchs information from strava and show in a simple flask application.

## Local Testing

### Strava API

First of all you need Strava API credentials could be found [here](https://developers.strava.com/).

Once you got it you should set the following environment variables

```shell
STRAVA_API_ACCESS_TOKEN=<Access Token>
STRAVA_CLUB_ID=<Club Id>
```

To make things easier to test in local env im using [python-dotenv](https://github.com/theskumar/python-dotenv) so you could create a new file called `.env` under `strava_extensions` folder (there is an `.env.example` you could us as example).

### Poetry

Im using [poetry](https://python-poetry.org/docs/) as dependency management, make sure you have it installed before following next steps.

- Install dependencies

```shell
poetry install
```

- Run Flask Project

```shell
poetry run python strava_extensions/flask-server/main.py
```

- Run tests

```shell
poetry run pytest
```

#### Makefile

Also there is a Makefile file that have the following instructions that will make more easier previous steps:

- make install: install dependencies
- make flask_start: start flask server
- make test: run unit tests
