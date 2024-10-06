from flask import Flask, render_template, request, redirect, url_for
from backend.userdata import add_user, login_to_acct
from backend.file_to_text import process_file
from backend.Langchain.llm import LLM
from backend.quiz_evaluator import grader

app = Flask(__name__)

class Instance():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.xp = 0
        self.quiz = ""
        self.correct_answers = ""

instance = Instance()


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create_acct')
def create_acct():
    return render_template('create_acct.html', title=instance.username, xp=instance.xp)

@app.route('/quiz')
def quiz():
    return render_template("quiz.html", username=instance.username, xp=instance.xp)

@app.route('/handle_login', methods=['POST'])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username and password:
        if login_to_acct(username=username, password=password):
            instance.username = username
            return redirect(url_for('quiz'))

@app.route('/handle_acct_create', methods=['POST'])
def handle_acct_create():
    username = request.form.get("username")
    password = request.form.get("password")
    if username and password:
        add_user(username=username, password=password)
        instance.username = username
        return redirect(url_for('quiz'))


@app.route('/upload', methods=["POST"])
def file_upload_handler():
    file = request.files.get("uploaded_file")  # Using .get() for safer access

    if not file:  # Check if a file was uploaded
        return redirect(url_for('quiz'))

    file_contents = process_file(file)

    processor = LLM()
    questions = processor.generate_questions(file_contents)

    # Initialize an empty list for question-answer pairs
    question_answer_pairs = []

    # Ensure questions is a list
    if isinstance(questions, list):  
        for q in questions:
            # Ensure q is a dictionary and has the required keys
            if isinstance(q, dict) and 'question' in q and 'answers' in q:
                question_text = q['question']  # Extract the question text
                answers = [ans['answer'] for ans in q.get('answers', [])]  # Extract answers safely
                question_answer_pairs.append((question_text, answers))  # Append as a tuple
            else:
                # Handle cases where q is not formatted correctly
                return "Invalid question format", 400
    else:
        return "Questions must be a list", 400
    
    answerstr = []
    # gets the answer in a string
    for j in questions:
        for l in j['answers']:
            if l['is_correct'] == 1:
                answerstr.append(l['answer'])


    instance.correct_answers = "Answers: " + str(answerstr)
    instance.quiz = question_answer_pairs

    # Pass the paired questions and answers to the template
    return render_template("quiz.html", question_answer_pairs=question_answer_pairs, username=instance.username, xp=instance.xp)


@app.route('/handle_quiz_submission', methods=["POST"])
def handle_quiz_submission():
    user_answers = []

    # Collecting user answers from checkboxes
    for i in range(len(instance.quiz)):
        user_answers.append(request.form.getlist(f'question_{i + 1}'))  # Adjust based on your input names

    # Assuming you have a way to retrieve the correct answers
    correct_answers = instance.correct_answers

    # Initialize the score
    score = 0

    # Calculate the score
    for i, user_answer in enumerate(user_answers):
        if user_answer:  # Ensure the user provided an answer
            # Check if the user's answer matches the correct answer
            if set(user_answer) == set(correct_answers[i]):
                score += 1  # Increment score for each correct answer

    # Update the user's score in the instance
    instance.xp += score

    # Render the quiz page with results
    return render_template("quiz.html", question_answer_pairs=instance.quiz, answer=instance.correct_answers, xp=instance.xp)


if __name__=="__main__":
    app.run(debug=True)