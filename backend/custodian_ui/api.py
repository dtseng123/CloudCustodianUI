 
from custodian_ui import policy
from custodian_ui.extensions import csrf_protect

base_url = '/api'

def register_api(app):
    app.register_blueprint(policy.views.blueprint,
                           url_prefix='{}/policy'.format(base_url))
    csrf_protect.exempt(policy.views.blueprint)
