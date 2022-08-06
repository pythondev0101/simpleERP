from flask import jsonify, request
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
    query: EventLocation = EventLocation.find_many(filter, skip=start, limit=length)
    total_records = len(EventLocation.find_many(filter))
    filtered_records = len(query)
    
    table_data = []
    
    x: EventLocation
    for x in query:
        table_data.append([
            x.id,
            {'name': x.name, 'description': x.description},
            x.address,
            format_date(x.date_start),
            format_date(x.date_end),
            format_date(x.date_created),
            ''
        ])

    response = {
        'draw': draw,
        'recordsTotal': filtered_records,
        'recordsFiltered': total_records,
        'data': table_data,
    }

    return jsonify(response)
