from flask import Flask, render_template, jsonify

app= Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'Calgary, Canada',
        'salary': '$100,000'
    },
    {
        'id':2,
        'title':'Micro Circuit Engineer',
        'location': 'Edmonton, Canada',
        'salary': '$120,000'
    },
    {
        'id':3,
        'title':'Chip Specialist',
        'location': 'Vancover, Canada',
        'salary': '$80,000'
    },
    {
        'id':4,
        'title':'Data Programmer',
        'location': 'Toronto, Canada'
    }
]

@app.route("/")
def home():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ =="__main__":
    app.run(debug=True)