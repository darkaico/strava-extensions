import json
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def load_club_activities():

    with open(f'{CURRENT_DIR}/club_activities.json') as f:
        result = json.load(f)

    return result


def load_invalid_club_activities():

    with open(f'{CURRENT_DIR}/club_activities_invalid.json') as f:
        result = json.load(f)

    return result
