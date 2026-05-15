from extensions import db

class Maquina(db.Model):

    __tablename__ = 'maquinas'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    ubicacion = db.Column(
        db.String(200),
        nullable=False
    )

    estado = db.Column(
        db.String(50),
        nullable=False
    )

    espirales = db.relationship(
        'Espiral',
        back_populates='maquina',
        cascade='all, delete'
    )

    def __repr__(self):
        return f'<Maquina {self.nombre}>'