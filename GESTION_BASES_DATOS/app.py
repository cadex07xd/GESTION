from flask import Flask, render_template
from sqlalchemy import text
from config import Config
from flask_login import login_required, current_user
from extensions import db, migrate, login_manager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)

login_manager.login_view = 'auth.login'

# IMPORTAR MODELOS
from models.user import Usuario
from models.maquina import Maquina
from models.snack import Snack
from models.espiral import Espiral
from models.venta import Venta
from models.inventario import InventarioDetalle

# IMPORTAR RUTAS
from routes.auth import auth
from routes.snacks import snacks
from routes.maquinas import maquinas
from routes.espirales import espirales
from routes.ventas import ventas

app.register_blueprint(auth)
app.register_blueprint(snacks)
app.register_blueprint(maquinas)
app.register_blueprint(espirales)
app.register_blueprint(ventas)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route("/")
@login_required
def home():
    from datetime import datetime, timedelta
    hoy = datetime.utcnow().date()
    en_10_dias = hoy + timedelta(days=10)

    total_maquinas = Maquina.query.count()
    total_snacks = Snack.query.count()
    total_ventas = Venta.query.count()

    # Espirales con stock bajo (menos de 3)
    stock_bajo = Espiral.query.filter(Espiral.stock_actual < 3).count()

    # Ventas recientes
    ventas_recientes = Venta.query.order_by(Venta.fecha.desc()).limit(5).all()

    return render_template(
        'dashboard.html',
        usuario=current_user,
        total_maquinas=total_maquinas,
        total_snacks=total_snacks,
        total_ventas=total_ventas,
        stock_bajo=stock_bajo,
        ventas_recientes=ventas_recientes,
    )


import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
