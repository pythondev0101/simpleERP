from flask import jsonify, request
import pymongo
from app.auth.models.user_model import User
from app.datatables import bp_datatables



@bp_datatables.route('/users')
def dt_users():
    draw = request.args.get('draw')
    start, length = int(request.args.get('start')), int(request.args.get('length'))
    description = request.args.get('description', '')
    date_from = request.args.get('date_from', '')
    date_to = request.args.get('date_to', '')
    
    total_records: int
    filtered_records: int
    filter: dict
    
    filter = {}
    query: User = User.find_many(filter, skip=start, limit=length)
    total_records = len(User.find_many(filter))
    filtered_records = len(query)
    
    table_data = []
    
    x: User
    for x in query:
        table_data.append([
            x.id,
            x.full_name,
            str(x.date_created),
            ''
        ])

    response = {
        'draw': draw,
        'recordsTotal': filtered_records,
        'recordsFiltered': total_records,
        'data': table_data,
    }

    return jsonify(response)
