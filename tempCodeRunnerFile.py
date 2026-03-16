from skill_engine import analyze_gap
from database import get_job_skills

student_skills=["Python","SQL","HTML"]

job_id = 1   # Data Analyst

job_skills = get_job_skills(job_id)

percent,missing=analyze_gap(student_skills,job_skills)

print("Job Skills:", job_skills)
print("Readiness:", round(percent,2), "%")
print("Missing Skills:", missing)