from flask import jsonify, request
from flask_cors import cross_origin
from flask_login import login_required
from app import CSRF
from app.api import bp_api
from app.templates.main.models.event_location_model import EventLocation
from app.utils import convert_to_dict


@bp_api.route('/event-locations', methods=['POST'])
@cross_origin()
@CSRF.exempt
def create_event_location():
    print(request.form)
    if request.form is not None:
        data = request.form
    else:
        data = request.json
        
    # try:
    EventLocation.create(convert_to_dict(data))
    
    response = {
        'status': 'success',
        'code': 'success',
        'data': data,
        'message': "Succesfully!"
    }
    print(response)
    # except Exception:
    #     response = {
    #         'status': 'error',
    #         'code': 'unknown',
    #         'data': data,
    #         'message': "Failed!"
    #     }
    #     return jsonify(response), 400
    
    return jsonify(response), 201
    