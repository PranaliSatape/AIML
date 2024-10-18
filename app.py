from flask import Flask, render_template, request
from expert_system import diagnose

app = Flask(__name__)

# List of questions
questions = [
    "Do you have a fever?",
    "Do you have a sore throat?",
    "Do you have a cough?",
    "Are you experiencing shortness of breath?",
    "Do you have body aches or muscle pain?",
    "Have you lost your sense of taste or smell?",
    "Are you experiencing chills or shivering?",
    "Do you have a headache?",
    "Have you been in close contact with someone diagnosed with COVID-19?",
    "Do you have a history of respiratory issues?"
]

# Initialize user answers
user_answers = []

@app.route('/')
def home():
    return render_template('index.html', question=questions[0], question_number=0)

@app.route('/answer', methods=['POST'])
def answer():
    question_number = int(request.form['question_number'])
    answer = request.form['answer']
    user_answers.append(answer)

    # Check if there are more questions
    if question_number < len(questions) - 1:
        next_question_number = question_number + 1
        return render_template('index.html', question=questions[next_question_number], question_number=next_question_number)
    else:
        diagnosis = diagnose(user_answers)
        return render_template('result.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
