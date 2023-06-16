import webview
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'secret_key'

# Mock user data for login
users = {'admin': 'password'}

# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            flash('Login successful!', 'success')
            webview.evaluate_js("window.location.href = '/home';")
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=False, port=5000)

# Start the webview
webview.create_window("Login Page", "http://localhost:5000")
webview.start()
