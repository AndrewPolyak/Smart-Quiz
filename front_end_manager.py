from flask import Flask, render_template, request, redirect, url_for
from backend.userdata import add_user, login_to_acct
from backend.file_to_text import process_file
from backend.Langchain.llm import LLM

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create_acct')
def create_acct():
    return render_template('create_acct.html')

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

@app.route('/handle_login', methods=['POST'])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username and password:
        if login_to_acct(username=username, password=password):
            return redirect(url_for('quiz'))

@app.route('/handle_acct_create', methods=['POST'])
def handle_acct_create():
    username = request.form.get("username")
    password = request.form.get("password")
    if username and password:
        add_user(username=username, password=password)
        return redirect(url_for('quiz'))
    
@app.route('/upload', methods=["POST"])
def file_upload_handler():
    file = request.files["uploaded_file"]

    if file == "":
        return redirect(url_for('quiz'))
    
    file_contents = process_file(file)

    processor = LLM()
    questions = processor.generate_questions(file_contents)


if __name__=="__main__":
    app.run(debug=True)