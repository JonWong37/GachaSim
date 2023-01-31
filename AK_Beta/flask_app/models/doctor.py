from operator import truediv
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request, redirect, session
from flask_app.models.operator import Operator
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



DATABASE = 'Arknights'
class Doctor:
    def __init__( self , data ):
        self.id = data['id']
        self.nickname = data['nickname']
        self.email = data['email']
        self.password = data['password']
        self.operators = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO doctors (nickname, email, password) VALUES (%(nickname)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def saveop(cls, data):
        data = {'operator_id' : data[0].id,
            'operator_name' : data[0].operator_name,
            'operator_class' : data[0].operator_class,
            'doctor_id' : session['doctor_id'],
            'rarity' : data[0].rarity
            }
        query = "INSERT INTO manage (doctor_id, operator_id, rarity, operator_name, operator_class) VALUE (%(doctor_id)s, %(operator_id)s, %(rarity)s, %(operator_name)s, %(operator_class)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # Get Email

    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM doctors WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        doctor = Doctor(results[0])
        return doctor

    # unique OPERATOR checker 

    @classmethod
    def unique_operator(cls,data):
        data = {
        'operator_id' : data[0].id,
        'doctor_id' : session['doctor_id'],
        }
        query = "SELECT * FROM manage WHERE doctor_id = %(doctor_id)s AND operator_id = %(operator_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) == 0:
            pass
        elif len(results) > 0:
            return True
        else:
            return False

    # VALIDATION

    @staticmethod
    def validate(doctor):
        is_valid = True
        if len(doctor['nickname']) < 2:
            flash("First name needs to be at least 2 characters.", 'nickname')
            is_valid = False
        if not EMAIL_REGEX.match(doctor['email']):
            flash("Invalid email address!!", 'email')
            is_valid = False
        if len(doctor['password']) == 0 or len(doctor['password']) < 3 :    
            flash("Please enter a password", 'password')
            is_valid = False
        if doctor['password'] != doctor['password_confirm']:
            flash("Passwords do not match", 'password_confirm')
            is_valid = False
        return is_valid


