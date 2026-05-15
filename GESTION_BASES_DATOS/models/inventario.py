from extensions import db
from datetime import datetime

class InventarioDetalle(db.Model):
    __tablename__ = 'inventario_detalle'

    id = db.Column(db.Integer, primary_key=True)

    espiral_id = db.Column(
        db.Integer,
        db.ForeignKey('espirales.id'),
        nullable=False
    )

    cantidad_agregada = db.Column(db.Integer, nullable=False)

    fecha_reposicion = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    operario = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<InventarioDetalle {self.id}>'