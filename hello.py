from flask import Flask, escape, url_for, request, render_template
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


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


""" with app.test_request_context():
    print(url_for('about'))
    print(url_for('hello_world'))
    print(url_for('show_subpath', subpath='this/is/sub/path'))
    print(url_for('projects'))
    print(url_for('static', filename='style.css')) """


def show_the_login_form():
    return 'Enter your login info'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


def do_the_login():
    return 'You are logged in'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertion.
    assert request.path == '/hello'
    assert request.method == 'POST'
    print(request.path, request.method)

from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

""" @app.route('/login')
def login():
    abort(401)
    this_is_never_executed() """