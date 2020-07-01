import requests

from strava_extensions.strava.services import BuilderService
from strava_extensions.utils.mixins import LoggerMixin


class StravaAPI(LoggerMixin):

    API_URL = 'https://www.strava.com/api/v3'
    access_token = None

    def __init__(self, access_token: str):
        self.access_token = access_token

    def get(self, resource_url: str):
        url = f'{self.API_URL}/{resource_url}'

        response = requests.get(
            url, params={'access_token': self.access_token})

        if response.status_code != 200:
            self.logger.error(response)
            return

        return response.json()

    def get_club_activities(self, club_id: int):
        resource_url = f'clubs/{club_id}/activities'

        json_activities = self.get(resource_url)

        return BuilderService.build_summary_activities(json_activities)
