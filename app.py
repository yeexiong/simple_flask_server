# We import the `Flask` and `jsonify` classes from the Flask library.
from flask import Flask, jsonify

# We create a Flask application by initializing the `app` object.
app = Flask(__name__)

# Sample student data
students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

# We define a route `/students` that responds to GET requests.
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    old_student = []
    for student in students:
        if student['age'] > 20:
            old_student.append(student)
    return old_student

@app.route('/young_students', methods=['GET'])
def get_young_students():
    young_student = []
    for student in students:
        if student['age'] < 21:
            young_student.append(student)
    return young_student

@app.route('/advance_students', methods=['GET'])
def get_advance_students():
    advance_student = []
    for student in students:
        if student['age'] < 21 and student['grade'] == 'A':
            advance_student.append(student)
    return advance_student

@app.route('/student_names', methods=['GET'])
def get_student_names():
    name_student = []
    for student in students:
        name_student.append({"first_name": student['first_name'],
                             "last_name": student['last_name']})
    return name_student

@app.route('/student_ages', methods=['GET'])
def get_student_ages():
    student_ages = []
    for student in students:
        student_ages.append({"first_name": student['first_name'],
                             "last_name": student['last_name'],
                            "age": student['age'] })
    return student_ages

if __name__ == '__main__':
    app.run(debug=True, port=8000) # Flask tries to run on port 5000 by default but it's sometimes occupied by a different function. Let's tell flask to utilize port 8000 instead