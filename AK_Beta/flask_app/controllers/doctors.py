from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.doctor import Doctor
from flask_app.models.operator import Operator
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#login page

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/homescreen')
def operators():
    if 'doctor_id' not in session:
        return redirect('/')
    return render_template('homescreen.html')

#Register new user

@app.route('/register', methods = ['POST'])
def new():
    if not Doctor.validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'nickname' : request.form['nickname'],
        'email' : request.form['email'],
        'password' : pw_hash
    }
    # if Doctor.unique_email(request.form):
    #     flash("Email already exists", 'taken')
    #     return redirect('/')
    session['nickname'] = request.form['nickname']
    user_id = Doctor.save(data)
    session['doctor_id'] = user_id
    return redirect('/loggedin')

@app.route('/loggedin')
def created():
    return redirect('/homescreen')

# log in

@app.route('/login', methods = ['POST'])
def doctor():
    data = { 'email' : request.form['log_email']}
    user_in_db = Doctor.get_email(data)
    if not user_in_db:
        flash('Invalid E-mail address or password.', 'invalid')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['log_password']):
        flash('Invalid E-mail address or password.', 'invalid')
        return redirect('/')
    session['doctor_id'] = user_in_db.id
    session['nickname'] = user_in_db.nickname
    return redirect('/homescreen')

#logout

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')





