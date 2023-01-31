from ast import operator
from dataclasses import dataclass
from pydoc import Doc
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.operator import DATABASE, Operator
from flask_app.models.doctor import Doctor
from flask_bcrypt import Bcrypt
import random
bcrypt = Bcrypt(app)

# Star AK stuff here




# Button that takes us from Home page to the headhunt page

@app.route('/headhunt')
def headhunt():
    return render_template("headhunt.html")


# Rolling button
@app.route('/headhunt1')
def headhunt1():
    rarity = [Operator.rollsix(), Operator.rollfive()]
    rates = [0.25,0.75]
    operator = random.choices(rarity, rates, k=1)
    if not Doctor.unique_operator(operator):
        Doctor.saveop(operator)
    return render_template("headhunt1.html", operator = operator[0])



# Rolling button
@app.route('/headhunt10')
def headhunt10():
    operators = []
    for i in range(10):
        operator = Operator.roll()
        operators.append(operator)
    return render_template("headhunt10.html", operators = operators)


# SHOW OPERATOR CARD / ID

@app.route('/operator_management/<int:id>')
def opmanagement(id):
    data = {'id' : id}
    return render_template('operator_management.html', operators = Operator.get_all(data))

@app.route('/operators/<int:id>')
def show(id):
    if 'doctor_id' not in session:
        return redirect('/')
    data = {'id': id}
    operator = Operator.get_one(data)
    return render_template("show.html", operator = operator)


    # SELECT * FROM doctors join doctors all items on docotor_id = manage.doctor_id join six_star on manage.six_star_id = six_star.id

    # INSERT INTO manage (six_star_id, rarity, operator_name, operator_class) SELECT id, rarity, operator_name, operator_class FROM six_stars where id = "3";