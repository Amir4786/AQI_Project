from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import sklearn
import numpy as np

app= Flask(__name__)
model= pickle.load(open("AQI_Delhi_Model.pkl","rb"))
@app.route("/", methods=["POST","GET"])
def Home():
    return render_template("index.html")
@app.route("/predict", methods=["POST","GET"])
def predict():
    if request.method=="POST":
        PM25= int(request.form["PM2.5"])
        PM100= int(request.form["PM10"])
        NO2= int(request.form["NO2"])
        NH3= int(request.form["NH3"])
        SO2= int(request.form["SO2"])
        CO= int(request.form["CO"])
        Ozone= int(request.form["Ozone"])
        prediction= int(model.predict([[PM25,PM100,NO2,NH3,SO2,CO,Ozone]]))
        if prediction<=50:
            return render_template("index.html",prediction_text="AQI= {} Good".format(prediction))
        elif prediction>50 and prediction<=100:
            return render_template("index.html",prediction_text="AQI= {} Satisfactory".format(prediction))
        elif prediction>100 and prediction<=200:
            return render_template("index.html",prediction_text="AQI= {} Moderate".format(prediction))
        elif prediction>200 and prediction<=300:
            return render_template("index.html",prediction_text="AQI= {} Poor".format(prediction))
        elif prediction>300 and prediction<=400:
            return render_template("index.html",prediction_text="AQI= {} Very Poor".format(prediction))
        elif prediction>400:
            return render_template("index.html",prediction_text="AQI= {} Severe".format(prediction))
    else:
        return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)