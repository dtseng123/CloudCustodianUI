# cloud-custodian-ui

> A Light UI for cloud custodian policy management

## Purpose
Locally create, manage and deploy Cloud Custodian policies. Currently WIP.  

## Pre-requisites 
[Install Cloud Custodian on your system](https://cloudcustodian.io/docs/quickstart/index.html#install-cloud-custodian)


## Install and Run backend
``` bash

cd backend

# Create & Activate virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Database setup
python manage.py db init &
python manage.py db migrate & 
python manage.py db upgrade

# Run backend server
 python manage.py runserver

# for a list of other commands 
python manage.py 

    server              Runs the Flask development server i.e. app.run()
    db                  Perform database migrations
    urls                Displays all of the url matching routes for the project
    fixtures            Generate fixtures for application models.
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()
```


## Build Setup Frontend

``` bash

cd frontend

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

With your browser go to `localhost:8080` 