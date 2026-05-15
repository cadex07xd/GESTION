from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from extensions import db
from models.user import Usuario
from flask_login import current_user

auth = Blueprint('auth', __name__)

# LOGIN
@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        correo = request.form['correo']
        password = request.form['password']

        usuario = Usuario.query.filter_by(
            correo=correo
        ).first()

        if usuario and usuario.check_password(password):

            login_user(usuario)

            flash('Login exitoso', 'success')

            return redirect(url_for('home'))

        else:
            flash('Credenciales incorrectas', 'danger')

    return render_template('login.html')

# LOGOUT
@auth.route('/logout')
@login_required
def logout():

    logout_user()

    flash('Sesión cerrada', 'info')

    return redirect(url_for('auth.login'))# REGISTRO
@auth.route('/register', methods=['GET', 'POST'])
@login_required
def register():

    if current_user.rol != 'ADMIN':

        flash('Acceso denegado', 'danger')

        return redirect(url_for('home'))

    if request.method == 'POST':

        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']
        rol = request.form['rol']

        existe_usuario = Usuario.query.filter_by(
            correo=correo
        ).first()

        if existe_usuario:

            flash('El correo ya existe', 'danger')

            return redirect(url_for('auth.register'))

        nuevo_usuario = Usuario(
            nombre=nombre,
            correo=correo,
            rol=rol
        )

        nuevo_usuario.set_password(password)

        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Usuario creado correctamente', 'success')

        return redirect(url_for('home'))

    return render_template('register.html')