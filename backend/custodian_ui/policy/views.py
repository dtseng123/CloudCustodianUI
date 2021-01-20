import json
from flask import Blueprint, jsonify, request
from .models import Policy
from .schema import policyschema, policyschemas

blueprint = Blueprint('Policy', __name__)

@blueprint.route('/', methods=['GET', "OPTIONS"])
def policies_all():
    """Get all policies."""

    if request.method == 'OPTIONS': 
        return build_preflight_response()
    
    elif request.method == 'GET': 
        policies = Policy.query.all()

        data, errors = policyschemas.dump(policies)

        if errors:
            resp = jsonify(errors)
            resp.status_code = 400
            return resp
        
        return build_actual_response(jsonify(data))

@blueprint.route('/<int:idx>', methods=['PUT', "OPTIONS"])
def policy_put(idx):
    if request.method == 'OPTIONS': 
        return build_preflight_response()
    
    elif request.method == 'PUT':
        model, errors = policyschema.load(request.json)

        if errors:
            resp = jsonify(errors)
            resp.status_code = 400
            return resp

        policy = Policy.query.filter_by(idx=idx).first_or_404()
        fields = policyschema.dump(model).data
        # Explicitly delete fields user is not supposed to update
        del fields['idx']
        policy.update(**fields)
        
        data =  policyschema.jsonify(policy)
        return build_actual_response(jsonify(data))



@blueprint.route('/<int:idx>', methods=['GET', "OPTIONS"])
def policy_get(idx):
    if request.method == 'OPTIONS': 
        return build_preflight_response()
    elif request.method == 'GET':

        policy = Policy.query.filter_by(idx=idx).first_or_404()
        data = policyschema.jsonify(policy)

        return build_actual_response(jsonify(data))


@blueprint.route('/<int:idx>', methods=['DELETE'])
def policy_delete(id):
    if request.method == 'OPTIONS': 
        return build_preflight_response()
    elif request.method == 'DELETE':

        model = Policy.query.filter_by(id=id).first_or_404()
        model.delete()
        return ('', 200)
    


# @blueprint.route('/', methods=['POST', "OPTIONS"])
# def policy_create():
#     if request.method == 'OPTIONS': 
#         return build_preflight_response()
    
#     elif request.method == 'POST':    
#         model, errors = policyschema.load(request.json)
#         if errors:
#             resp = jsonify(errors)
#             resp.status_code = 400
#             return resp
       
#         if model:
#             model.save()

#             resp = policyschema.jsonify(model)
#             resp.status_code = 201
#             return build_actual_response(jsonify(resp))





def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
