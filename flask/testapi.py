from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def home():
    return "Hello World"

@app.route("/get-user/<userId>")
def getUser(userId):
    userData = {
        "user_id": userId,
        "name": "gary"
    }
    
    extra = request.args.get("extra")
    
    if extra:
        userData["extra"] = extra
    
    return jsonify(userData), 200


@app.route("/create-user", methods=["POST"])
def createUser(userId):
    if request.method == "POST":
        print("POST")
        
    data = request.get_json()
    return jsonify(data),201

    
if __name__ == "__main__":
    app.run(debug=True)
    
    fl