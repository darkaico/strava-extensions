import pytest
import requests

from strava_extensions.strava.api import StravaAPI
from tests.conftest import MockResponse


@pytest.fixture
def strava_api(monkeypatch):
    def mockreturn(url, params=None):
        return MockResponse(200, [])

    monkeypatch.setattr(requests, "get", mockreturn)

    return StravaAPI("")


@pytest.fixture
def strava_api_with_activities(monkeypatch, json_club_activities):
    def mockreturn(url, params=None):
        return MockResponse(200, json_club_activities)

    monkeypatch.setattr(requests, "get", mockreturn)

    return StravaAPI("")


@pytest.fixture
def strava_api_with_invalid_activities(monkeypatch, json_invalid_club_activities):
    def mockreturn(url, params=None):
        return MockResponse(200, json_invalid_club_activities)

    monkeypatch.setattr(requests, "get", mockreturn)

    return StravaAPI("")


@pytest.fixture
def strava_api_http_error(monkeypatch):
    def mockreturn(url, params=None):
        return MockResponse(400)

    monkeypatch.setattr(requests, "get", mockreturn)

    return StravaAPI("")


def test_get_club_activities_empty(strava_api):

    activities = strava_api.get_club_activities(4)

    assert len(activities) == 0


def test_get_club_activities(strava_api_with_activities):

    activities = strava_api_with_activities.get_club_activities(4)

    assert len(activities) == 3


def test_get_club_activities_http_error(strava_api_http_error):

    activities = strava_api_http_error.get_club_activities(4)

    assert len(activities) == 0


def test_get_club_activities_response_error(strava_api_with_invalid_activities):

    activities = strava_api_with_invalid_activities.get_club_activities(4)

    assert len(activities) == 0
