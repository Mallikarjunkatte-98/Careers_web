from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title" : "Data Analyst",
    "location" : "Bengluru,India",
    "Salary" : "Rs. 1000000"
    },
    {
    "id": 2,
    "title" : "Data Scientist",
    "location" : "Delhi,India",
    "Salary" : "Rs. 1500000"
    },
    {
    "id": 3,
    "title" : "Front End Engineer",
    "location" : "remote"
    },
    {
    "id": 4,
    "title" : "Backend Developer",
    "location" : "San Francisco,USA",
    "Salary" : "$. 120,000"
    }
]

@app.route("/")
def hello_():
    return render_template("home.html",jobs = JOBS,company="Yugant")

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)



if __name__ == "__main__":
    app.run(debug=True)
