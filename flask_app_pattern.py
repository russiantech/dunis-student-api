from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = [
    {
        "id": 1,
        "title": "Fullstack Web Development",
        "description": "Learn HTML, CSS, JavaScript, React, Python, and Django.",
        "duration": "12 weeks",
        "level": "Beginner to Intermediate"
    },
    {
        "id": 2,
        "title": "Data Science & AI",
        "description": "Learn Python, data analysis, machine learning, and AI deployment.",
        "duration": "16 weeks",
        "level": "Intermediate"
    },
    {
        "id": 3,
        "title": "Mobile App Development",
        "description": "Build Android and iOS apps with Flutter and Dart.",
        "duration": "10 weeks",
        "level": "Beginner"
    }
]

@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

if __name__ == '__main__':
    app.run(debug=True)
