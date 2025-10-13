from flask import Flask, render_template, jsonify
app = Flask(__name__)
QUALIFICATIONS= [
  {
    'id': 1,
    'title': 'PSC',
    'location': 'Dhaka board, Bangladesh',
    'Year': '2014'
  },
  {
    'id': 2,
    'title': 'JSC',
    'location': 'Dhaka board, Bangladesh',
    'Year': '2016'
  },
  {
    'id': 3,
    'title': 'SSC',
    'location': 'Dhaka board, Bangladesh',
    'Year': '2018'
  },
  {
    'id': 4,
    'title': 'H.S.C',
    'location': 'Dhaka board, Bangladesh',
    'Year': '2020'
  },
  {
    'id': 5,
    'title': 'B.Sc in Computer Science',
    'location': 'Albukhary International University, Kedah, Malaysia',
    'Year': '2026'
  }
]

@app.route("/")
def hello():
  return render_template("home.html" ,education=QUALIFICATIONS)

@app.route("/api/degrees")
def list_degrees():
  return jsonify(QUALIFICATIONS)

if __name__ == "__main__":
  app.run('0.0.0.0',debug=True)