from dataclasses import dataclass, field
from typing import Optional

import pytest

from tests.fixtures import loaders


@dataclass
class MockResponse:

    status_code: int
    json_response: Optional[dict] = field(default_factory=dict)

    def json(self):
        return self.json_response


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """No requests allowed during tests."""
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture
def json_club_activities():
    return loaders.load_club_activities()


@pytest.fixture
def json_invalid_club_activities():
    return loaders.load_invalid_club_activities()


@pytest.fixture
def json_club_activity():
    return loaders.load_valid_club_activity()
