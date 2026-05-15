from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from extensions import db

from models.venta import Venta
from models.espiral import Espiral

ventas = Blueprint('ventas', __name__)

# ======================================
# LISTAR VENTAS
# ======================================

@ventas.route('/ventas')
@login_required
def listar_ventas():

    lista_ventas = Venta.query.order_by(Venta.fecha.desc()).all()

    return render_template(
        'ventas/listar.html',
        ventas=lista_ventas
    )

# ======================================
# CREAR VENTA
# ======================================

@ventas.route('/ventas/crear', methods=['GET', 'POST'])
@login_required
def crear_venta():

    espirales = Espiral.query.all()

    if request.method == 'POST':

        espiral_id = request.form['espiral_id']
        cantidad = int(request.form['cantidad'])

        espiral = Espiral.query.get(espiral_id)

        # VALIDAR STOCK

        if espiral.stock_actual < cantidad:

            flash('Stock insuficiente', 'danger')

            return redirect(url_for('ventas.crear_venta'))

        # CALCULAR TOTAL

        total = cantidad * espiral.snack.precio

        # CREAR VENTA

        nueva_venta = Venta(
            espiral_id=espiral_id,
            cantidad=cantidad,
            total=total
        )

        # DESCONTAR STOCK

        espiral.stock_actual -= cantidad

        db.session.add(nueva_venta)
        db.session.commit()

        flash('Venta registrada correctamente', 'success')

        return redirect(url_for('ventas.listar_ventas'))

    return render_template(
        'ventas/crear.html',
        espirales=espirales
    )