import sqlite3

def connect():
    return sqlite3.connect("data/data.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_skills(
        student_id INTEGER,
        skill_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_roles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_required_skills(
        job_id INTEGER,
        skill_name TEXT,
        priority INTEGER
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully!")