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
    instance.previous_uploaded_file = file_contents  # Store the contents for later use

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

    # Pass the paired questions and answers to the template
    return render_template("quiz.html", question_answer_pairs=question_answer_pairs, username=instance.username, xp=instance.xp)

@app.route('/handle_quiz_submission', methods=["POST"])
def handle_quiz_submission():
    user_answers = request.form.getlist('user_answers[]')  # Ensure this matches your form input name

    # Use the previously uploaded file contents
    processor = LLM()
    AI_Output = processor.generate_questions(instance.previous_uploaded_file)  # Use stored file contents

    # Call the grader function with user_answers and AI_Output
    results = grader(user_answers, AI_Output)

    # Prepare the results for rendering
    correct_answers = sum(1 for r in results if r != 0)  # Assuming non-zero means correct
    total_questions = len(results)

    return render_template("results.html", results=results, correct_answers=correct_answers, total_questions=total_questions, username=instance.username, xp=instance.xp)



if __name__=="__main__":
    app.run(debug=True)