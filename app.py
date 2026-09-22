from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

students = []


# Serve index.html and students.xml
@app.route("/")
def home():
    return send_from_directory(".", "index1.html")


@app.route("/students.xml")
def xml_file():
    return send_from_directory(".", "students.xml")


# POST method
@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    students.append(data)

    return jsonify({
        "message": "Student added successfully",
        "student": data
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)