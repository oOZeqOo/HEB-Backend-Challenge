from flask import Flask
from sqlalchemy import create_engine
from utils.db import create_customers


def get_engine():
    return create_engine("sqlite:///db.sqlite", echo=False)


def get_session():
    from sqlalchemy.orm import sessionmaker

    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_app():
    from views import api

    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    api.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    create_customers()
    app.run(debug=True, host="0.0.0.0")
