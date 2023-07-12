from flask import Flask, render_template, request, flash
from flask import jsonify ##

app = Flask(__name__)
app.secret_key = "gkudfgdfhgowrign"

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST", "GET"])
def result():
    protein = float(request.form['protein_input'])
    fat = float(request.form['fat_input'])
    fiber = float(request.form['fiber_input'])
    moisture = float(request.form['moisture_input'])
    other = 100 - protein - fat - fiber - moisture

    if str(request.form['phospherous_input']) != '':
        phospherous = float(request.form['phospherous_input'])
        phospherous = ((phospherous * 100) / (100 - moisture))
        other = other - phospherous
    
    
    protein = ((protein * 100) / (100 - moisture))
    fat = ((fat * 100) / (100 - moisture))
    fiber = ((fiber * 100) / (100 - moisture))
    other = ((other * 100) / (100 - moisture))

    flash("Protein: " + str(round(protein, 2))+ "%")
    flash("Fat: " + str(round(fat, 2)) + "%")
    flash("Fiber: " + str(round(fiber, 2)) + "%")
    flash("Other: " + str(round(other, 2)) + "%")
    if str(request.form['phospherous_input']) != '':
        flash("Phospherous: " + str(round(phospherous, 2)) + "%")
    return render_template("index.html")