from app import app
from extensions import db

with app.app_context():
    with db.engine.connect() as conn:
        conn.execute(db.text("ALTER TABLE snacks ADD COLUMN IF NOT EXISTS marca VARCHAR(100) DEFAULT 'Sin marca'"))
        conn.execute(db.text("ALTER TABLE snacks ADD COLUMN IF NOT EXISTS gramos INTEGER"))
        conn.commit()
    print("Columnas agregadas correctamente")
