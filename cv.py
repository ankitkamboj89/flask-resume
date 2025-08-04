from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def executive_summary():
    return render_template('executive_summary.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/technical-knowledge')
def technical_knowledge():
    return render_template('technical_knowledge.html')

@app.route("/AI_ML_Projects")
def projects():
    return render_template("AI_ML_Projects.html")

if __name__ == '__main__':
    app.run(debug=True)
