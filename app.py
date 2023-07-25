from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
app= Flask(__name__)



@app.route("/")
def home():
    JOBS= load_jobs_from_db()
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    JOBS= load_jobs_from_db()
    return jsonify(JOBS)

@app.route("/jobs/<id>")
def show_jobs(id):
    job= load_job_from_db(id)
    if not job:
        return 'Not found', 404
    return render_template('jobpage.html',job=job)

@app.route("/job/<id>/app", methods=['post'])
def apply_to_job(id):
    job= load_job_from_db(id)
    data= request.form

    add_application_to_db(id, data)
    return render_template('application_submitted.html', application=data, job=job)

if __name__ =="__main__":
    app.run(debug=True)