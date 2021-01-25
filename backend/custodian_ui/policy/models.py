from custodian_ui.database import Column, db, Model, CRUDMixin, SurrogatePK
import enum

class CloudProvider(enum.Enum):
    """Cloud Provider Model"""
    
    AWS = "Amazon Web Services"
    GCP = "Google Cloud Platform"
    AZU = "Microsoft Azure Cloud"


class Policy(SurrogatePK, Model):
    """Cloud Policy Model"""

    __tablename__ = 'policy'
    __bind_key__ = 'local'
    cloud = Column(db.Enum(CloudProvider))
    name = Column(db.String(50), unique=False, nullable=False)
    description = Column(db.String(350), unique=False, nullable=False)
    yaml = Column(db.VARCHAR(), unique=False, nullable=True)
    
    def __repr__(self):
        return '<Policy({})>'.format(self.id)
