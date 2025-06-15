# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import config_by_name

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_name='production'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes.students import students_bp
    from app.routes.auth import auth_bp
    from app.routes.events import events_bp
    from app.routes.blogs import blogs_bp

    app.register_blueprint(students_bp, url_prefix='/students')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(events_bp, url_prefix='/events')
    app.register_blueprint(blogs_bp, url_prefix='/blogs')

    with app.app_context():
        db.create_all()

    return app
