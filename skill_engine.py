def analyze_gap(student_skills,job_skills):
    student_set=set(student_skills)
    job_set=set(job_skills)

    matched=student_set&job_set
    missing=job_set-student_set

    percent=(len(matched)/len(job_set))*100

    return percent,list(missing)