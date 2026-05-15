from extensions import db
from datetime import datetime

class Venta(db.Model):

    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)

    espiral_id = db.Column(
        db.Integer,
        db.ForeignKey('espirales.id'),
        nullable=False
    )

    cantidad = db.Column(
        db.Integer,
        nullable=False
    )

    total = db.Column(
        db.Numeric(10,2),
        nullable=False
    )

    fecha = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # RELACIÓN

    espiral = db.relationship(
        'Espiral',
        backref='ventas'
    )