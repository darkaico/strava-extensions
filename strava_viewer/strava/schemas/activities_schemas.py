from marshmallow import (
    Schema,
    fields,
    post_load
)

from strava_viewer.strava.models import SummaryActivity

from .athletes_schemas import AthleteSchema


class SummaryActivitySchema(Schema):

    athlete = fields.Nested(AthleteSchema)
    resource_state = fields.Int(required=True)
    name = fields.Str(required=True)
    distance = fields.Float(required=True)
    moving_time = fields.Int(required=True)
    elapsed_time = fields.Int(required=True)
    total_elevation_gain = fields.Float(required=True)
    activity_type = fields.Str(required=True, data_key='type')
    workout_type = fields.Int(required=True)

    @post_load
    def make_model(self, data, **kwargs):
        return SummaryActivity(**data)
