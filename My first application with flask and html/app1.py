from flask import Flask

app = Flask(__name__)
users = ['dhruv-dixit', 'azhaku', 'soham-jandhale', 'sou']

@app.route('/')
def index():
    return "<h1>Welcome to Flask!</h1>"

@app.route('/about')
def about_us():
    return '<h1>This is About us page</h1>'

@app.route('/user/<user_name>')
def user_profile(user_name):
    if user_name in users:
        return "Welcome {}!". format(user_name)
    return "Please Register."

if __name__ == '__main__':
    return 'This is About us page'
    app.run(debug = True)