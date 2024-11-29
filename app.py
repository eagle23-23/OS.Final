from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "postgres.clgaa2koavq7.us-east-1.rds.amazonaws.com",
    "port": 5432
}

def get_courses():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # Query to fetch courses
        cur.execute("SELECT course, year, start_date, title, location, credit, days, times, instructor, registered, wait_num, status FROM:")
        courses = cur.fetchall()

        cur.close()
        conn.close()

        return courses
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return []

@app.route('/')
def index():
    courses = get_courses()
    return render_template('index5.html', courses=courses)

if name == 'main':
    app.run(debug=True, host='0.0.0.0', port=5000)