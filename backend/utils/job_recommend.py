import requests

def predict_job_title(resume_text):
    # Basic example - replace with ML model later
    if "python" in resume_text.lower():
        return "Python Developer"
    elif "react" in resume_text.lower():
        return "Frontend Developer"
    else:
        return "Software Engineer"

def get_job_recommendations(job_title, skills):
    # Using Remotive public API (for now)
    url = f"https://remotive.io/api/remote-jobs?search={job_title}"
    response = requests.get(url)
    if response.status_code != 200:
        return []

    jobs = response.json().get('jobs', [])
    top_jobs = []

    for job in jobs[:5]:  # Limit to top 5 jobs
        top_jobs.append({
            "title": job['title'],
            "company": job['company_name'],
            "location": job['candidate_required_location'],
            "link": job['url']
        })

    return top_jobs
