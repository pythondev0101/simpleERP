from flask import jsonify, request
from flask_cors import cross_origin
from flask_login import login_required
from app import CSRF, MONGO
from app.api import bp_api
from app.templates.main.models.event_location_model import EventLocation
from app.utils import convert_to_dict, format_date


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
    

@bp_api.route('/events', methods=['GET'])
@cross_origin()
@CSRF.exempt
def events_list():
    total_records: int
    filtered_records: int
    filter: dict
    
    filter = {}
    query = MONGO.db.events.find(filter)
    total_records = MONGO.db.events.find(filter).count()
    filtered_records = query.count()
    
    events = []
    
    for row in query:
        event = EventLocation(data=row)
        events.append({
            'id': event.id,
            'name': event.name,
            'description': event.description,
            'address': event.address,
            'str_start': format_date(event.date_start),
            'str_end': format_date(event.date_end),
            'str_created': format_date(event.date_created)
        })

    response = {
        'events': events,
    }

    return jsonify(response)

    