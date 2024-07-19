from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Integer, Float, Table, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired
import sqlite3
from wtforms.validators import DataRequired, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime



app = Flask(__name__)
bs = Bootstrap5(app)


@app.route("/")
def home_page():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)