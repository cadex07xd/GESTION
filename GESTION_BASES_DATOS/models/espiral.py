from extensions import db

class Espiral(db.Model):

    __tablename__ = 'espirales'

    id = db.Column(db.Integer, primary_key=True)

    maquina_id = db.Column(
        db.Integer,
        db.ForeignKey('maquinas.id'),
        nullable=False
    )

    snack_id = db.Column(
        db.Integer,
        db.ForeignKey('snacks.id'),
        nullable=True
    )

    codigo = db.Column(db.String(10), nullable=False)  # Ej: A1, B2

    capacidad = db.Column(db.Integer, nullable=False, default=10)

    stock_actual = db.Column(db.Integer, default=0)

    maquina = db.relationship('Maquina', back_populates='espirales')

    snack = db.relationship('Snack')

    def __repr__(self):
        return f'<Espiral {self.codigo}>'