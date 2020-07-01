test:
	poetry run pytest

flask_start:
	poetry run python strava_viewer/flask-server/main.py