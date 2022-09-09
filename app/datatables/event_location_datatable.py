from flask import jsonify, request
from app import MONGO
from app.datatables import bp_datatables
from app.templates.main.models.event_location_model import EventLocation
from app.utils import format_date



@bp_datatables.route('/event-locations')
def dt_event_locations():
    draw = request.args.get('draw')
    start, length = int(request.args.get('start')), int(request.args.get('length'))
    description = request.args.get('description', '')
    date_from = request.args.get('date_from', '')
    date_to = request.args.get('date_to', '')
    
    total_records: int
    filtered_records: int
    filter: dict
    
    filter = {}
    query = MONGO.db.events.find(filter).skip(start).limit(length)
    total_records = MONGO.db.events.find(filter).count()
    filtered_records = query.count()
    
    table_data = []
    
    for row in query:
        event = EventLocation(data=row)
        table_data.append([
            event.id,
            {'name': event.name, 'description': event.description},
            event.address,
            format_date(event.date_start),
            format_date(event.date_end),
            format_date(event.date_created),
            ''
        ])

    response = {
        'draw': draw,
        'recordsTotal': filtered_records,
        'recordsFiltered': total_records,
        'data': table_data,
    }

    return jsonify(response)
