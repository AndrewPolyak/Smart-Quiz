from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('create_acct.html')

@app.route('/handle_acct_create', methods=['POST'])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username and password:
        None # do something


if __name__=="__main__":
    app.run(debug=True)