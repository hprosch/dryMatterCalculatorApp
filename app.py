from flask import Flask, render_template, request, flash
from flask import jsonify ##

app = Flask(__name__)
app.secret_key = "gkudfgdfhgowrign"

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST", "GET"])
def resultInfo():

    proteinAsFed = float(request.form['protein_input'])
    fatAsFed = float(request.form['fat_input'])
    fiberAsFed = float(request.form['fiber_input'])
    moisture = float(request.form['moisture_input'])
    otherAsFed = 100 - proteinAsFed - fatAsFed - fiberAsFed - moisture

    if str(request.form['phospherous_input']) != '':
        phospherousAsFed = float(request.form['phospherous_input'])
        phospherousDryMatter = ((phospherousAsFed * 100) / (100 - moisture))
        otherAsFed = otherAsFed - phospherousAsFed
    
    proteinDryMatter = ((proteinAsFed * 100) / (100 - moisture)) 
    fatDryMatter = ((fatAsFed * 100) / (100 - moisture))
    fiberDryMatter = ((fiberAsFed * 100) / (100 - moisture))
    otherDryMatter = ((otherAsFed * 100) / (100 - moisture))

    if str(request.form['phospherous_input']) != '':
        return render_template("results.html", moisture=moisture, proteinAsFed=proteinAsFed, fatAsFed=fatAsFed, fiberAsFed=fiberAsFed, otherAsFed=otherAsFed, phospherousAsFed=phospherousAsFed, phospherousDryMatter=phospherousDryMatter, proteinDryMatter=proteinDryMatter, fatDryMatter=fatDryMatter, fiberDryMatter=fiberDryMatter, otherDryMatter=otherDryMatter)
    return render_template("results.html", moisture=moisture, proteinAsFed=proteinAsFed, fatAsFed=fatAsFed, fiberAsFed=fiberAsFed, otherAsFed=otherAsFed, proteinDryMatter=proteinDryMatter, fatDryMatter=fatDryMatter, fiberDryMatter=fiberDryMatter, otherDryMatter=otherDryMatter)


#Preserving the original route:
#@app.route("/result", methods=["POST", "GET"])
#def result():
#    protein = float(request.form['protein_input'])
#    fat = float(request.form['fat_input'])
#    fiber = float(request.form['fiber_input'])
#    moisture = float(request.form['moisture_input'])
#    other = 100 - protein - fat - fiber - moisture

#    if str(request.form['phospherous_input']) != '':
#        phospherous = float(request.form['phospherous_input'])
#        phospherous = ((phospherous * 100) / (100 - moisture))
#        other = other - phospherous
    
    
#    protein = ((protein * 100) / (100 - moisture))
#    fat = ((fat * 100) / (100 - moisture))
#    fiber = ((fiber * 100) / (100 - moisture))
#    other = ((other * 100) / (100 - moisture))

#    flash("Protein: " + str(round(protein, 2))+ "%")
#    flash("Fat: " + str(round(fat, 2)) + "%")
#    flash("Fiber: " + str(round(fiber, 2)) + "%")
#    flash("Other: " + str(round(other, 2)) + "%")
#    if str(request.form['phospherous_input']) != '':
#        flash("Phospherous: " + str(round(phospherous, 2)) + "%")
#    return render_template("index.html")