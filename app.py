from flask import Flask, render_template, request
from database import get_job_skills
from skill_engine import analyze_gap

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    skills_input = request.form["skills"]
    job_id = int(request.form["job_id"])

    student_skills = [s.strip() for s in skills_input.split(",")]

    job_skills = get_job_skills(job_id)

    percent, missing = analyze_gap(student_skills, job_skills)

    return f"""
    <h2>Result</h2>
    <p>Readiness: {round(percent,2)}%</p>
    <p>Missing Skills: {missing}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)