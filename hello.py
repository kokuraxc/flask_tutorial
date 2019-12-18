from flask import Flask, escape, url_for, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    return 'the project page'


@app.route('/about')
def about():
    return 'the about page'


with app.test_request_context():
    print(url_for('about'))
    print(url_for('hello_world'))
    print(url_for('show_subpath', subpath='this/is/sub/path'))
    print(url_for('projects'))


def show_the_login_form():
    return 'Enter your login info'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


def do_the_login():
    return 'You are logged in'

