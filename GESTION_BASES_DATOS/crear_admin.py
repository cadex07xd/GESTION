from app import app, db
from models.user import Usuario

with app.app_context():

    admin = Usuario(
        nombre='Administrador',
        correo='admin@novaventa.com',
        rol='ADMIN'
    )

    admin.set_password('123456')

    db.session.add(admin)
    db.session.commit()

    print('✅ Admin creado correctamente')