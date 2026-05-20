from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models.snack import Snack

snacks = Blueprint('snacks', __name__)

# LISTAR SNACKS
@snacks.route('/snacks')
@login_required
def listar_snacks():
    lista_snacks = Snack.query.all()
    return render_template('snacks/listar.html', snacks=lista_snacks)

# CREAR SNACK
@snacks.route('/snacks/crear', methods=['GET', 'POST'])
@login_required
def crear_snack():
    if current_user.rol != 'ADMIN':
        flash('No tienes permiso para realizar esta acción', 'danger')
        return redirect(url_for('home'))
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form.get('marca', 'Sin marca')
        precio = request.form['precio']
        gramos = request.form.get('gramos') or None
        nuevo_snack = Snack(
            nombre=nombre,
            marca=marca,
            precio=precio,
            gramos=int(gramos) if gramos else None,
        )
        db.session.add(nuevo_snack)
        db.session.commit()
        flash('Snack creado correctamente', 'success')
        return redirect(url_for('snacks.listar_snacks'))
    return render_template('snacks/crear.html')

# EDITAR SNACK
@snacks.route('/snacks/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_snack(id):
    if current_user.rol != 'ADMIN':
        flash('No tienes permiso para realizar esta acción', 'danger')
        return redirect(url_for('home'))
    snack = Snack.query.get_or_404(id)
    if request.method == 'POST':
        snack.nombre = request.form['nombre']
        snack.marca = request.form.get('marca', 'Sin marca')
        snack.precio = request.form['precio']
        gramos = request.form.get('gramos') or None
        snack.gramos = int(gramos) if gramos else None
        db.session.commit()
        flash('Snack actualizado correctamente', 'warning')
        retur
