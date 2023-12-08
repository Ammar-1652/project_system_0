# app.py
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    return render_template("log_in.html")


# ... (remaining code)


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/sign_up_for_students", methods=["GET", "POST"])
def sign_up_for_students():
    return render_template("sign_up_for_students.html")


@app.route("/sign_up_for_ass_prof", methods=["GET", "POST"])
def sign_up_for_ass_prof():
    return render_template("sign_up_for_ass_prof.html")


@app.route("/sign_up_for_prof", methods=["GET", "POST"])
def sign_up_for_prof():
    return render_template("sign_up_for_prof.html")


@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
    )


@app.route("/student_dashboard")
def student_dashboard():
    return render_template("student_dashboard.html")


@app.route("/student_dashboard/assignment_for_student")
def assignment_for_student():
    return render_template("assignment_for_student.html")


@app.route("/student_dashboard/courses_for_student")
def courses_for_student():
    return render_template("courses_for_student.html")


@app.route("/student_dashboard/timetable_for_student")
def timetable_for_student():
    return render_template("timetable_for_student.html")


if __name__ == "__main__":
    app.run(debug=True)
