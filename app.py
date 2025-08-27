
from flask import Flask, jsonify, request
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os

load_dotenv()

# create app
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT")
    )
    return conn

# Create table if it doesn't exist
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def home():
    return jsonify({"message":"Welcome to our homepage"})

@app.route("/students", methods=["GET"])
def get_students():
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM  students ")
            students = cur.fetchall()   
            return jsonify([dict(s) for s in students])

@app.route("/students", methods = ["POST"])
def add_student():
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    email = data.get("email")
    grade = data.get("grade")

    if not name or not age or not email or not grade:
        return jsonify({"error": "missing fields: name, age, email required"}),400

    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("INSERT INTO students (name, age, email, grade) VALUES (%s, %s, %s, %s) RETURNING *;", 
                        (name,age,email,grade))

            new_student = cur.fetchone()
            conn.commit()
            return jsonify(dict(new_student)),201





if __name__ == "__main__":
    app.run(debug=True)