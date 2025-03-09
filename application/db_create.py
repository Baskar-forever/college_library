import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application import db, create_app
from application.models import User  # Ensure this is correctly defined

app = create_app()

with app.app_context():
    db.create_all()
    print("Database created successfully!")

