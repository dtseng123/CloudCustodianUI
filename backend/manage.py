import os
from flask import Flask, render_template, request, jsonify, make_response
from random import *
import subprocess
from flask_migrate import Migrate, MigrateCommand
from flask_script import Command, Manager, Option, Server, Shell
from flask_script.commands import Clean, ShowUrls
from flask_cors import CORS

from custodian_ui.app import create_app
from custodian_ui.database import db
from custodian_ui.settings import DevConfig
from custodian_ui.policy.schema import policyschema, policyschemas

import requests
 

# ------------------------------------------------------------------------
# Application Creation ( MAIN ENTRY POINT )
# ------------------------------------------------------------------------ 
app = create_app(DevConfig)

manager = Manager(app)
migrate = Migrate(app, db)


# @app.route('/api/custodian', methods=['OPTIONS','GET'])
# def custodian_help():
#     if request.method == 'OPTIONS': 
#         return build_preflight_response()
    
#     elif request.method == 'GET': 
#         process = subprocess.run(['custodian', '-h'],
#             stdout=subprocess.PIPE,
#             universal_newlines=True)

#         response = {
#             'custodian': process.stdout
#         }
#         return build_actual_response(jsonify(response))

@app.route('/api/custodian', methods=['GET'])
def custodian_help():
    process = subprocess.run(['custodian', '-h'],
        stdout=subprocess.PIPE,
        universal_newlines=True)

    response = {
        'custodian': process.stdout
    }
    return jsonify(response)

@app.route('/api/custodian', methods=['POST'])
def policy_make():
    print(request.json)
    model, errors = policyschema.load(request.json)
        
    if model:
        model.save()
        resp = policyschema.jsonify(model)
        resp.status_code = 201
        print(resp)

    return jsonify(resp)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")



def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


class Fixtures(Command):
    """Generate fixtures for application models."""

    def run(self, rpc):
        print("Generating Fixtures")
         
server = Server(host="0.0.0.0", port=5000, use_reloader=True)

manager.add_command('server', server)
manager.add_command('db', MigrateCommand)
manager.add_command('urls', ShowUrls())
manager.add_command('fixtures', Fixtures())
manager.add_command('urls', ShowUrls())

if __name__ == '__main__':
    manager.run()

# FLASK_APP=run.py FLASK_DEBUG=1 flask run
