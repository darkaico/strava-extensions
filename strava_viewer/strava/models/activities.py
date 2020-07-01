from dataclasses import dataclass

from .athletes import Athlete


@dataclass
class SummaryActivity:

    athlete: Athlete
    resource_state: int
    name: str
    distance: float
    moving_time: int
    elapsed_time: int
    total_elevation_gain: float
    activity_type: str
    workout_type: int
