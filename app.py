from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from oop import *
app = Flask(__name__)

# Configuration
DATABASE = 'students.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            middle_name TEXT,
            last_name TEXT,
            contact_number TEXT,
            national_id TEXT,
            email TEXT,
            date_of_birth TEXT,
            gender TEXT,
            class_level TEXT,
            profile_file TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    return render_template('sign_up_for_students.html')

@app.route('/sign_up_for_students', methods=['GET', 'POST'])
def sign_up_for_students():
    if request.method == 'POST':
        s = Student()  # Create a new instance of Student for each form submission
        s.set_first_name(request.form['first-name'])
        s.set_middle_name(request.form['middle-name'])
        s.set_last_name(request.form['last-name'])
        s.set_contact_num(request.form['contact-number'])
        s.set_personal_id(request.form['national-id'])
        s.set_email(request.form['email'])
        s.set_date_of_birth(request.form['date-of-birth'])
        s.set_gender(request.form['gender'])
        s.set_level(request.form['class_level'])
        s.set_profile_file(request.form['profile-file'])

        # Insert data into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (
                first_name, middle_name, last_name, contact_number, national_id,
                email, date_of_birth, gender, class_level, profile_file
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            s.get_first_name(), s.get_middle_name(), s.get_last_name(),
            s.get_contact_num(), s.get_personal_id(), s.get_email(),
            s.get_date_of_birth(), s.get_gender(), s.get_level(), s.get_profile_file()
        ))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('sign_up_for_students.html')

if __name__ == '__main__':
    app.run(debug=True)
