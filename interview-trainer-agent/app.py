from flask import Flask, render_template, request, jsonify
from ai.interview_engine import generate_questions, evaluate_answer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_questions', methods=['POST'])
def generate():
    data = request.get_json()

    role = data.get('role')

    questions = generate_questions(role)

    return jsonify({
        'questions': questions
    })

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()

    question = data.get('question')
    answer = data.get('answer')
    feedback = evaluate_answer(question, answer)

    return jsonify({
        'feedback': feedback
    })

if __name__ == '__main__':
    app.run(debug=True)