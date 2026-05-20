from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models.espiral import Espiral
from models.maquina import Maquina
from models.snack import Snack

espirales = Blueprint('espirales', __name__)

@espirales.route('/espirales')
@login_required
def listar_espirales():
    lista_espirales = Espiral.query.all()
    return render_template('espirales/listar.html', espirales=lista_espirales)

@espirales.route('/espirales/crear', methods=['GET', 'POST'])
@login_required
def crear_espiral():
    if current_user.rol not in ['ADMIN', 'OPERARIO']:
        flash('No tienes permiso', 'danger')
        return redirect(url_for('home'))
    maquinas = Maquina.query.all()
    snacks = Snack.query.all()
    if request.method == 'POST':
        nuevo_espiral = Espiral(
            codigo=request.form['codigo'],
            capacidad=request.form['capacidad'],
            stock_actual=request.form['stock_actual'],
            maquina_id=request.form['maquina_id'],
            snack_id=request.form['snack_id']
        )
        db.session.add(nuevo_espiral)
        db.session.commit()
        flash('Espiral creado correctamente', 'success')
        return redirect(url_for('espirales.listar_espirales'))
    return render_template('espirales/crear.html', maquinas=maquinas, snacks=snacks)

@espirales.route('/espirales/eliminar/<int:id>')
@login_required
def eliminar_espiral(id):
    if current_user.rol not in ['ADMIN', 'OPERARIO']:
        flash('No tienes permiso', 'danger')
        return redirect(url_for('home'))
    espiral = Espiral.query.get_or_404(id)
    db.session.delete(espiral)
    db.session.commit()
    flash('Espiral eliminado', 'danger')
    return redirect(url_for('espirales.listar_espirales'))
