from curses import panel
from distutils.errors import LinkError
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request, redirect, session
import random
import re


DATABASE = 'Arknights'
class Operator:
    def __init__( self , data ):
        if 'id' in data:
            self.id = data['id']
        self.operator_name = data['operator_name']
        self.rarity = data['rarity']
        self.operator_class = data['operator_class']
        if 'image' in data :
            self.image = data['image']
        if 'doctor_id' in data :
            self.doctor_id = data['doctor_id']
        if 'voice' in data:
            self.voice = data['voice']
        if 'created_at' in data:
            self.created_at = data['created_at']
        if 'updated_at' in data:
            self.updated_at = data['updated_at']
        if 'charaicon' in data:
            self.charaicon = data['charaicon']
        if 'text' in data:
            self.text = data['text']

    # READ ALL

    @classmethod
    def get_all(cls, data):
        query = "SELECT manage.*, operators.id, operators.image, operators.charaicon FROM operators LEFT JOIN manage ON manage.operator_id = operators.id WHERE doctor_id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        operators = []
        for operator in results:
            operators.append(cls(operator))
        print(operator)
        return operators

    # GET ONE OPERATOR TO DISPLAY OWNER NAME

    @classmethod
    def rollsix(cls):
        query = "SELECT * FROM operators WHERE rarity = 6 ORDER BY RAND() LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        operators = Operator(results[0])
        return operators

    @classmethod
    def rollfive(cls):
        query = "SELECT * FROM operators WHERE rarity = 5 ORDER BY RAND() LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        operators = Operator(results[0])
        return operators

    @classmethod
    def rollfour(cls):
        query = "SELECT * FROM operators WHERE rarity = 4 ORDER BY RAND() LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        operators = Operator(results[0])
        return operators

    @classmethod
    def rollthree(cls):
        query = "SELECT * FROM operators WHERE rarity = 3 ORDER BY RAND() LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        operators = Operator(results[0])
        return operators

    @classmethod
    def roll(self):
        num = random.random()
        if num <= 0.10:
            query = "SELECT * FROM operators WHERE rarity = 6 ORDER BY RAND() LIMIT 1;"
        elif num <= 0.20:
            query = "SELECT * FROM operators WHERE rarity = 5 ORDER BY RAND() LIMIT 1;"
        elif num <= 0.30:
            query = "SELECT * FROM operators WHERE rarity = 4 ORDER BY RAND() LIMIT 1;"
        else:
            query = "SELECT * FROM operators WHERE rarity = 3 ORDER BY RAND() LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query)
        return results[0]

# Wanted to try something Like  

# @app.route('/headhunt1')
# def headhunt1():
#     Operator.roll()
#     operator = Operator.roll()

#     return render_template("headhunt1.html", operator = operator[0])

