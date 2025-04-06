from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# PostgreSQL setup
conn = psycopg2.connect(
    dbname="mydatabase",
    user="postgres",
    password="1qaz1WSX@#",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Ensure the tables existssss
cursor.execute('''
    CREATE TABLE IF NOT EXISTS submissions (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
''')
conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    
    if name and email:
        cursor.execute(
            "INSERT INTO submissions (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        return "Form submitted successfully!"
    return "Please fill out all fields."

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    
    if name and email and password:
        cursor.execute(
            "INSERT INTO members (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )
        conn.commit()
        return "Registration successful!"
    return "Please fill out all fields."
