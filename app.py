# app.py
from flask import Flask, render_template, request
import sqlite3
from oop import Student, Professor,Professor_asst  # Assuming you have a class Professor in oop module

app = Flask(__name__)
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


def create_table2():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            national_id TEXT NOT NULL,
            email TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()
def create_table3():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assistant (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            national_id TEXT NOT NULL,
            email TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def create_table_courses():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Example table creation
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            course_name TEXT,
            instructor TEXT,
            start_date DATE,
            end_date DATE
        )
    ''')

    connection.commit()
    connection.close()

create_table()
create_table2()
create_table3()
create_table_courses()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/log_in")
def log_in():
    return render_template("log_in.html")


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/sign_up_for_students", methods=['GET', 'POST'])
def sign_up_for_students():
    s = Student()
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
    return render_template("sign_up_for_students.html")


@app.route("/sign_up_for_ass_prof",methods=['GET', 'POST'])
def sign_up_for_ass_prof():
    a=Professor_asst()
    if request.method == 'POST':
        a.data = request.form
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO assistant (
                first_name, middle_name, last_name,
                contact_number, national_id, email,
                date_of_birth, gender, password
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            a.data['first-name'],
            a.data['middle-name'],
            a.data['last-name'],
            a.data['contact-number'],
            a.data['national-id'],
            a.data['email'],
            a.data['date-of-birth'],
            a.data['gender'],
            a.data['password']
        ))
        connection.commit()
        connection.close()
    return render_template("sign_up_for_ass_prof.html")


@app.route("/sign_up_for_prof", methods=['GET', 'POST'])
def sign_up_for_prof():
    p = Professor()
    if request.method == 'POST':
        p.data = request.form
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO profs (
                first_name, middle_name, last_name,
                contact_number, national_id, email,
                date_of_birth, gender, password
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            p.data['first-name'],
            p.data['middle-name'],
            p.data['last-name'],
            p.data['contact-number'],
            p.data['national-id'],
            p.data['email'],
            p.data['date-of-birth'],
            p.data['gender'],
            p.data['password']
        ))
        connection.commit()
        connection.close()
    return render_template("sign_up_for_prof.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
