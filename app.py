from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Password",
    database="registration_db"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    student_name = request.form['student_name']
    father_name = request.form['father_name']
    mother_name = request.form['mother_name']
    phone_number = request.form['phone_number']
    email = request.form['email']
    date_of_birth = request.form['date_of_birth']
    address = request.form['address']
    blood_group = request.form['blood_group']
    department = request.form['department']
    course = request.form['course']
    password = request.form['password']

    # Inserting data into MySQL
    insert_query = "INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    user_data = (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password)
    cursor.execute(insert_query, user_data)
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
