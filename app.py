from flask import Flask
from database import db
from routers.routers import usuario_bp, chamado_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///help.db" 
app.config["SECRET_KEY"] = 'secretomaster'

db.init_app(app)

app.register_blueprint(usuario_bp)
app.register_blueprint(chamado_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)