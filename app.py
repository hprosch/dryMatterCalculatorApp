from flask import Flask, render_template, request, flash
from flask import jsonify ##

app = Flask(__name__)
app.secret_key = "gkudfgdfhgowrign"

@app.route("/home")
def index():
    return render_template("boiler.html")

@app.route("/result", methods=["POST", "GET"])
def resultInfo():

    proteinAsFed = float(request.form['protein_input'])
    fatAsFed = float(request.form['fat_input'])
    fiberAsFed = float(request.form['fiber_input'])
    moisture = float(request.form['moisture_input'])
    otherAsFed = 100 - proteinAsFed - fatAsFed - fiberAsFed - moisture

    if str(request.form['phospherous_input']) != '':
        phospherousAsFed = float(request.form['phospherous_input'])
        phospherousDryMatter = round(((phospherousAsFed * 100) / (100 - moisture)), 2)
        otherAsFed = otherAsFed - phospherousAsFed
    
    proteinDryMatter = round(((proteinAsFed * 100) / (100 - moisture)), 2) 
    fatDryMatter = round(((fatAsFed * 100) / (100 - moisture)), 2)
    fiberDryMatter = round(((fiberAsFed * 100) / (100 - moisture)), 2)
    otherDryMatter = round(((otherAsFed * 100) / (100 - moisture)), 2)

    if str(request.form['phospherous_input']) != '':
        return render_template("results.html", proteinAsFed=proteinAsFed, fatAsFed=fatAsFed, fiberAsFed=fiberAsFed, otherAsFed=otherAsFed, phospherousAsFed=phospherousAsFed, phospherousDryMatter=phospherousDryMatter, proteinDryMatter=proteinDryMatter, fatDryMatter=fatDryMatter, fiberDryMatter=fiberDryMatter, otherDryMatter=otherDryMatter)
    return render_template("results.html", proteinAsFed=proteinAsFed, fatAsFed=fatAsFed, fiberAsFed=fiberAsFed, otherAsFed=otherAsFed, proteinDryMatter=proteinDryMatter, fatDryMatter=fatDryMatter, fiberDryMatter=fiberDryMatter, otherDryMatter=otherDryMatter)