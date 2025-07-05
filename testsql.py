from app import app
from models import db 

with app.app_context():  # 👈 this is the key
    with db.engine.connect() as connection:
        result = connection.execute(db.text("show columns from pages"))
        
        for row in result:
            print(row)