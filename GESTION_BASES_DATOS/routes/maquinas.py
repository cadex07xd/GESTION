from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from extensions import db
from models.maquina import Maquina

maquinas = Blueprint('maquinas', __name__)

# LISTAR MAQUINAS
@maquinas.route('/maquinas')
@login_required
def listar_maquinas():

    lista_maquinas = Maquina.query.all()

    return render_template(
        'maquinas/listar.html',
        maquinas=lista_maquinas
    )

# CREAR MAQUINA
@maquinas.route('/maquinas/crear', methods=['GET', 'POST'])
@login_required
def crear_maquina():

    if request.method == 'POST':

        nombre = request.form['nombre']
        ubicacion = request.form['ubicacion']
        estado = request.form['estado']

        nueva_maquina = Maquina(
            nombre=nombre,
            ubicacion=ubicacion,
            estado=estado
        )

        db.session.add(nueva_maquina)
        db.session.commit()

        flash('Máquina creada correctamente', 'success')

        return redirect(url_for('maquinas.listar_maquinas'))

    return render_template('maquinas/crear.html')

# EDITAR MAQUINA
@maquinas.route('/maquinas/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_maquina(id):

    maquina = Maquina.query.get_or_404(id)

    if request.method == 'POST':

        maquina.nombre = request.form['nombre']
        maquina.ubicacion = request.form['ubicacion']
        maquina.estado = request.form['estado']

        db.session.commit()

        flash('Máquina actualizada correctamente', 'warning')

        return redirect(url_for('maquinas.listar_maquinas'))

    return render_template(
        'maquinas/editar.html',
        maquina=maquina
    )

# ELIMINAR MAQUINA
@maquinas.route('/maquinas/eliminar/<int:id>')
@login_required
def eliminar_maquina(id):

    maquina = Maquina.query.get_or_404(id)

    db.session.delete(maquina)
    db.session.commit()

    flash('Máquina eliminada correctamente', 'danger')

    return redirect(url_for('maquinas.listar_maquinas'))