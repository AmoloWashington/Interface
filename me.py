import os
import flask
import webview

app = flask.Flask(__name__)

# Home page
@app.route('/')
def home():
    return '<h1>Welcome to the Home Page!</h1>'

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        # Perform authentication logic here
        if username == 'admin' and password == 'password':
            return '<h1>Login successful!</h1>'
        else:
            return '<h1>Invalid username or password</h1>'

    # Render the login form
    return '''
        <h1>Login</h1>
        <form method="post">
            <input type="text" name="username" placeholder="Username"><br>
            <input type="password" name="password" placeholder="Password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    # Run the Flask app in a separate thread
    flask_thread = webview.FlaskThread(app)
    flask_thread.run()

    # Create a WebView window
    webview.create_window("Login Page", "http://localhost:5000")
    webview.start()
