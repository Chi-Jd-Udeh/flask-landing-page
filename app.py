from flask import Flask, render_template, jsonify
from database import load_jobs_from_db
app= Flask(__name__)


def load_jobs_from_db():
    with engine.connect() as conn:
        result= conn.execute(text("select * from jobs"))
        results_as_dict = result.mappings().all()

        jobs=[]
        for row in results_as_dict:
            jobs.append(dict(row))
        return jobs

@app.route("/")
def home():
    JOBS= load_jobs_from_db()
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    JOBS= load_jobs_from_db()
    return jsonify(JOBS)

if __name__ =="__main__":
    app.run(debug=True)