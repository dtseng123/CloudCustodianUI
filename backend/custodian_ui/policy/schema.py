from custodian_ui.policy.models import Policy
from custodian_ui.extensions import ma
from marshmallow_enum import EnumField
from .models import CloudProvider
class PolicySchema(ma.SQLAlchemyAutoSchema):
    cloud = EnumField(CloudProvider, by_value=True)
    class Meta:
        model = Policy
        load_instance = True
 

policyschema = PolicySchema()
policyschemas = PolicySchema(many=True)
