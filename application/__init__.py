from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:baskarceo444@localhost:3306/library_management'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "your_secret_key"

    db.init_app(app)

    from application.models import User, Book
    from application.routes import routes  # Import routes

    with app.app_context():
        db.create_all()

    app.register_blueprint(routes)  # Register routes

    return app
