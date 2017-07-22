from flask import Flask, render_template, request, redirect, url_for
from app.users.users import User

app = Flask(__name__)


# Data structure
users = {'test@test.com': 'some thing here'} # we save the class here
bucketlists = []
activities = []


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['passwd']
        if email in users:#authenticate
            return redirect(url_for('create_bucketlist')) #that is a function name for the route yu wanna go
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        firstName = request.form['firstName']
        email = request.form['email']
        userName = request.form['userName']
        passwd = request.form['passwd']
        passwd2 = request.form['passwd2']
        new_user = User(firstName, email, userName, passwd)
        users[userName] = new_user
        return redirect(url_for('index'))
    return render_template('signup.html')


@app.route('/bucketlist', methods=['GET', 'POST'])
@login_required
def create_bucketlist():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session['id']
        add_bucket_list(bucketlist, user_id)
        flash(bucketlist + ' has been added successful.')
        return redirect(url_for('update_bucketlist'))
    return render_template('bucketlist.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('email', None)
    session.pop('id', None)
    flash('you are logged out.')
    return redirect(url_for('index'))

@app.route('/bucketlist', methods =['GET', 'POST'])
def update_bucketlist():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session['id']
        add_bucket_list(bucketlist, user_id)
        flash(bucketlist + ' has been updated successful.')

    return render_template('bucketlist.html')

@app.route('/viewbucketlist')
def view_bucketlist():
    return render_template('View.html')