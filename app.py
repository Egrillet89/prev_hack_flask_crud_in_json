from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)



@app.route("/add", methods=["POST"])
def fn_add():

    email = request.form["email"]
    name = request.form["name"]
    age = request.form["age"]

    profile = {
        "email":email,
        "name":name,
        "age":age
    }

    with open("data.json", "r") as f:
        data = json.load(f)

    data.append(profile)

    with open("data.json", "w") as f:
        json.dump(data,f)

    return jsonify({
        "payload":"save"
    })



@app.route("/find", methods=["POST"])
def fn_find():
    email = request.form["email"]   
    res = "no exists"

    with open("data.json", "r") as f:
        data = json.load(f)

    for item in data:
        if item["email"] == email:
            res = "exists"


    return jsonify({
        "payload":res
    })


@app.route("/delete", methods=["POST"])
def fn_delete():
    email = request.form["email"]
    with open("data.json", "r") as f:
        data = json.load(f)
    for i in range(len(data)):
        if data[i]["email"] == email:
            del data[i]
            break
    with open("data.json", "w") as f:
        json.dump(data, f)
    return jsonify({
        "payload":"deleted"
    })

@app.route("/update", methods=["POST"])
def fn_update():
    email = request.form["email"]
    name = request.form["name"]
    age = request.form["age"]
    with open("data.json", "r") as f:
        data = json.load(f)
    for i in range(len(data)):
        if data[i]["email"] == email:
            data[i]["name"] = name
            data[i]["age"] = age
            break
    with open("data.json", "w") as f:
        json.dump(data, f)
    return jsonify({
        "payload":"update"
    })

if __name__ == "__main__":
    app.run(debug=True)