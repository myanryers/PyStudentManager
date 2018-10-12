import flask
import student

students = []

app = flask.Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def students_page():
    if flask.request.method == "POST":
        new_student_id = flask.request.form.get("student-id", "")
        new_student_first_name = flask.request.form.get("name", "")
        new_student_last_name = flask.request.form.get("last-name", "")

        new_student = student.Student(first_name=new_student_first_name, last_name=new_student_last_name, student_id=new_student_id)
        students.append(new_student)

        return flask.redirect(flask.url_for("students_page"))

    return flask.render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
