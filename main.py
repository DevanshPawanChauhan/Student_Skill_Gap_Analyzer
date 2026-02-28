from skill_engine import analyze_gap

student_skills=["Python","SQL","HTML"]
job_skills = ["Python", "SQL", "Pandas", "Excel"]

percent,missing=analyze_gap(student_skills,job_skills)

print("Readiness:", round(percent,2), "%")
print("Missing Skills:", missing)