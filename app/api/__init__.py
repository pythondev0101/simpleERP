from flask import Blueprint



bp_api = Blueprint('api', __name__)


from . import events_api
from . import login