import json
from flask import app, jsonify, request
from .models import Policy
from .schema import policyschema, policyschemas
 

# @app.route('/api/policy/', methods=['GET', "OPTIONS"])
# def policies_all():
#     """Get all policies."""

#     policies = Policy.query.all()

#     data, errors = policyschemas.dump(policies)

#     if errors:
#         resp = jsonify(errors)
#         resp.status_code = 400
#         return resp
    
#     return jsonify(data)

# @app.route('/api/policy/<int:idx>', methods=['PUT', "OPTIONS"])
# def policy_put(idx):
#     if request.method == 'OPTIONS': 
#         return build_preflight_response()
    
#     elif request.method == 'PUT':
#         model, errors = policyschema.load(request.json)

#         if errors:
#             resp = jsonify(errors)
#             resp.status_code = 400
#             return resp

#         policy = Policy.query.filter_by(idx=idx).first_or_404()
#         fields = policyschema.dump(model).data
#         # Explicitly delete fields user is not supposed to update
#         del fields['idx']
#         policy.update(**fields)
        
#         data =  policyschema.jsonify(policy)
#         return build_actual_response(jsonify(data))



# @app.route('/api/policy/<int:idx>', methods=['GET', "OPTIONS"])
# def policy_get(idx):
#     if request.method == 'OPTIONS': 
#         return build_preflight_response()
#     elif request.method == 'GET':

#         policy = Policy.query.filter_by(idx=idx).first_or_404()
#         data = policyschema.jsonify(policy)

#         return build_actual_response(jsonify(data))


# @app.route('/api/policy/<int:idx>', methods=['DELETE'])
# def policy_delete(id):
#     if request.method == 'OPTIONS': 
#         return build_preflight_response()
#     elif request.method == 'DELETE':

#         model = Policy.query.filter_by(id=id).first_or_404()
#         model.delete()
#         return ('', 200)
    

# @app.route('/api/policy/', methods=['POST'])
# def policy_make():
#     import ipdb; ipdb.set_trace()
#     print(request.json)
#     model, errors = policyschema.load(request.json)
        
#     if model:
#         model.save()
#         resp = policyschema.jsonify(model)
#         resp.status_code = 201
#         print(resp)

#     return jsonify(resp)



# @app.after_request
# def after_request_func(response):
#     origin = request.headers.get('Origin')
#     if request.method == 'OPTIONS':
#         response = make_response()
#         response.headers.add('Access-Control-Allow-Credentials', 'true')
#         response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#         response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
#         response.headers.add('Access-Control-Allow-Methods',
#                             'GET, POST, OPTIONS, PUT, PATCH, DELETE')
#         if origin:
#             response.headers.add('Access-Control-Allow-Origin', origin)
#     else:
#         response.headers.add('Access-Control-Allow-Credentials', 'true')
#         if origin:
#             response.headers.add('Access-Control-Allow-Origin', origin)

#     return response
