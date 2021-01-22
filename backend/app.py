
import os
from flask import Flask, render_template, request, jsonify, make_response
from random import *
import subprocess
from flask_migrate import Migrate, MigrateCommand
from flask_script import Command, Manager, Option, Server, Shell
from flask_script.commands import Clean, ShowUrls
from flask_cors import CORS, cross_origin
from custodian_ui.settings import DevConfig
from custodian_ui.database import db
from custodian_ui.app import create_app
from custodian_ui.policy.models import Policy 
from custodian_ui.policy.schema import policyschema, policyschemas

# ------------------------------------------------------------------------
# Application Creation ( MAIN ENTRY POINT )
# ------------------------------------------------------------------------ 
app = create_app(DevConfig)

manager = Manager(app)
migrate = Migrate(app, db)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

@app.route('/api/custodian', methods=['GET'])
def custodian_help():
    process = subprocess.run(['custodian', '-h'],
        stdout=subprocess.PIPE,
        universal_newlines=True)

    response = {
        'custodian': process.stdout
    }
    return jsonify(response)

@app.route('/api/policy', methods=['POST'])
def policy_make():
    print(request.json)
    model = policyschema.load(request.json)
        
    if model:
        model.save()
        # import pdb; pdb.set_trace()
        resp = policyschema.jsonify(model)
        resp.status_code = 201
        print(resp)

    return resp

 
@app.route('/api/policy', methods=['GET','OPTIONS'])
def policies_all():
    """Get all policies."""
    policies = Policy.query.all()
    resp =  policyschemas.jsonify(policies)
    
    return resp

@app.route('/api/policy/<int:idx>', methods=['PUT', "OPTIONS"])
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



@app.route('/api/policy/<int:idx>', methods=['GET', "OPTIONS"])
def policy_get(idx):
    if request.method == 'OPTIONS': 
        return build_preflight_response()
    elif request.method == 'GET':

        policy = Policy.query.filter_by(idx=idx).first_or_404()
        data = policyschema.jsonify(policy)

        return build_actual_response(jsonify(data))


@app.route('/api/policy/<int:idx>', methods=['DELETE'])
def policy_delete(id):
    if request.method == 'OPTIONS': 
        return build_preflight_response()
    elif request.method == 'DELETE':

        model = Policy.query.filter_by(id=id).first_or_404()
        model.delete()
        return ('', 200)
    




@app.after_request
def after_request_func(response):
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response
