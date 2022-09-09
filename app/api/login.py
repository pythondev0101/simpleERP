from flask import jsonify, abort, request
from flask_cors import cross_origin
from app.api import bp_api
from app import CSRF, MONGO
from app.auth.models.user_model import User

@bp_api.route('/auth/login',methods=['POST'])
@cross_origin()
@CSRF.exempt
def api_login():
    username = request.json['username']
    password = request.json['password']

    # try:
    query = MONGO.db.auth_users.find_one({'username': username})
    print(username)
    print(query)
    user = User(data=query)

    if user is None or not user.check_password(password):
        response = {
            'status': 'error',
            'message': "Invalid username or password"
        }
        return jsonify(response), 401
    
    data = {
        '_id': user.id,
        'username': user.username,
        'fname': user.fname,
        'lname': user.lname,
        'email': user.email,
        'type': user.type
    }
    
    response = jsonify({
        'status': 'success',
        'data': data,
        'message': 'Login successfully!'
        })
        
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # except Exception as err:
    #     return jsonify({
    #         'status': 'error',
    #         'message': str(err)
    #     }), 500
