from flask import Flask, render_template, request, jsonify
from utilities import predict_species

app = Flask(__name__)

@app.route("/")
def app_home():
    return render_template("index.html")

@app.route("/prediction", methods = ["post"])
def get_species_name():
    data = request.form
    species = predict_species(data)
    return jsonify({"result": species})
    # return render_template("index.html", result = species)

if __name__ == "__main__":
    app.run(debug = True, port = 8080, host = "0.0.0.0")