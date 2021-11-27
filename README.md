[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=darkaico_strava-extensions&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=darkaico_strava-extensions)

# Strava Extensions

App that fetchs information from strava and show in a simple flask application.

### Strava API

First of all you need Strava API credentials could be found [here](https://developers.strava.com/).

Once you got it you should set the following environment variables

```shell
STRAVA_API_ACCESS_TOKEN=<Access Token>
STRAVA_CLUB_ID=<Club Id>
```

To make things easier to test in local env im using [python-dotenv](https://github.com/theskumar/python-dotenv) so you could create a new file called `.env` under `strava_extensions` folder (there is an `.env.example` you could us as example).
## Start the App

### Docker

Start the app by just calling

```bash
$ docker-compose up
```

or using make

```bash
$ make up
```

### Local Development
### Poetry

Im using [poetry](https://python-poetry.org/docs/) as dependency management, make sure you have it installed before following next steps.

- Install dependencies

```shell
poetry install
```

- Run Flask Project

```shell
poetry run python strava_extensions/flask_server/main.py
```

- Run tests

```shell
poetry run pytest
```
