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

def insert_job_roles():
    conn=connect()
    cursor=conn.cursor()

    roles=["Data Analyst","Backend Develop","ML Engineer"]
    for role in roles:
        cursor.execute("INSERT INTO job_roles(role_name) VALUES(?)", (role,))
    
    conn.commit()
    conn.close()

def insert_job_skills():
    conn=connect()
    cursor=conn.cursor()
    
    #DataAnalystSkills(JobId=1)
    skills = [
        (1, "Python", 1),
        (1, "SQL", 1),
        (1, "Excel", 2),
        (1, "Pandas", 1),
        (1, "Data Visualization", 2)
    ]
    cursor.executemany("INSERT INTO job_required_skills(job_id,skill_name,priority) VALUES(?,?,?)",skills)
    conn.commit()
    conn.close()

def get_job_skills(job_id):
    conn=connect()
    cursor=conn.cursor()
    cursor.execute(
        "select distinct skill_name from job_required_skills where job_id = ?",
        (job_id,)
    )
    rows=cursor.fetchall()
    skills=[row[0] for row in rows]
    return skills 

if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully!")
    insert_job_roles()
    insert_job_skills()