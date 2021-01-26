import os
from flask import Flask, render_template, request, jsonify, make_response
from random import *
import subprocess
from flask_migrate import Migrate, MigrateCommand
from flask_script import Command, Manager, Option, Server, Shell
from flask_script.commands import Clean, ShowUrls
from flask_cors import CORS, cross_origin
from custodian_ui.app import create_app
from custodian_ui.database import db
from custodian_ui.settings import DevConfig
from custodian_ui.fixtures import generate
import requests
from app import *



class Fixtures(Command):
    """Generate fixtures for application models."""

    def run(self):
        print("Generating Fixtures")
        generate()
         
server = Server(host="0.0.0.0", port=5000, use_reloader=True)

manager.add_command('server', server)
manager.add_command('db', MigrateCommand)
manager.add_command('urls', ShowUrls())
manager.add_command('fixtures', Fixtures())
manager.add_command('urls', ShowUrls())

if __name__ == '__main__':
    manager.run()

# FLASK_APP=run.py FLASK_DEBUG=1 flask run
