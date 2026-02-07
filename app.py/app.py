import time
import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    for i in range(10):
        try:
            return mysql.connector.connect(
                host="db",
                user="root",
                password="Samyak@7888",
                database="aproposdb"
            )
        except mysql.connector.Error:
            print(f"DB not ready, retrying... ({i+1}/10)")
            time.sleep(3)
    raise Exception("Database connection failed")

db = get_db_connection()
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")
db.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]

    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )
    db.commit()

    return render_template("success.html", name=name, email=email)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)