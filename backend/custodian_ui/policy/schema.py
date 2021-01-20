from custodian_ui.policy.models import Policy
from custodian_ui.extensions import ma

class PolicySchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Policy
        load_instance = True
 

policyschema = PolicySchema()
policyschemas = PolicySchema(many=True)
