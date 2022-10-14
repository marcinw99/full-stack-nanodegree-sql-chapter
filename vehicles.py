from os import abort
from flask import Flask, jsonify, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@127.0.0.1:5432/vehicles'
db = SQLAlchemy(app)

db.drop_all()

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)

class Driver(db.Model):
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    issued = db.Column(db.Date, nullable=False)
    vehicles = db.relationship('Vehicle', backref='driver', lazy=True)

db.create_all()