from extensions import db

class Snack(db.Model):

    __tablename__ = 'snacks'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    marca = db.Column(
        db.String(100),
        nullable=False,
        default='Sin marca'
    )

    precio = db.Column(
        db.Numeric(10, 2),
        nullable=False
    )

    gramos = db.Column(
        db.Integer,
        nullable=True
    )

    def __repr__(self):
        return f'<Snack {self.nombre}>'