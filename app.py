from flask import Flask, render_template, request, redirect, url_for
import sqlite3
<<<<<<< HEAD
from oop import Student 

=======
import sys
from oop import *
>>>>>>> 01c4a63eaf7276403aad85219d0b79ec52caa6c4
app = Flask(__name__)
app.secret_key=['password']
# Set up SQLite database
DATABASE = 'database.db'

def create_table():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            national_id TEXT NOT NULL,
            email TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT NOT NULL,
            class_level TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

create_table()

@app.route('/')
def index():
    return render_template('sign_up_for_students.html')

@app.route('/sign_up_for_students', methods=['POST'])
def sign_up_for_students():
    s=Student()
    if request.method == 'POST':
        s.data = request.form
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO students (
                first_name, middle_name, last_name,
                contact_number, national_id, email,
                date_of_birth, gender, class_level, password
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            s.data['first-name'],
            s.data['middle-name'],
            s.data['last-name'],
            s.data['contact-number'],
            s.data['national-id'],
            s.data['email'],
            s.data['date-of-birth'],
            s.data['gender'],
            s.data['class_level'],
            s.data['password']
        ))
        connection.commit()
        connection.close()
        return "<h1>Welcome <h1/>"


if __name__ == '__main__':
    app.run(debug=True)
