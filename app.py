from flask import Flask, render_template, request, redirect, url_for
import sqlite3

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
    return render_template('sign_up.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form['first-name']
        middle_name = request.form['middle-name']
        last_name = request.form['last-name']
        contact_number = request.form['contact-number']
        national_id = request.form['national-id']
        email = request.form['email']
        date_of_birth = request.form['date-of-birth']
        gender = request.form['gender']
        class_level = request.form['class_level']
        profile_file = request.form['profile-file']

        # Insert data into the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (
                first_name, middle_name, last_name, contact_number, national_id,
                email, date_of_birth, gender, class_level, profile_file
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            first_name, middle_name, last_name, contact_number, national_id,
            email, date_of_birth, gender, class_level, profile_file
        ))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('sign_up.html')

@app.route('/sign_up_for_students', methods=['GET', 'POST'])
def sign_up_for_students():
    if request.method == 'POST':
        # Retrieve and process form data (similar to the sign_up route)
        # ...

        return redirect(url_for('index'))

    return render_template('sign_up_for_students.html')

if __name__ == '__main__':
    app.run(debug=True)
