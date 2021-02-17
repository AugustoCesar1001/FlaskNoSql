from flask import request, jsonify



def error():
    response = jsonify({
        'message': 'Resource Not Found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response