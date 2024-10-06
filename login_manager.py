from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/handle_login', methods=['POST'])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username and password:
        return f"Thank you {username}. You submitted password: {password}"


if __name__=="__main__":
    app.run(debug=True)