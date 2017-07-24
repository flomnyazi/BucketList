from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from app.users.users import User

app = Flask(__name__)
app.secret_key = 'topsecret'

i=0
# Data structure
users = {'test@test.com': 'some thing here'} # we save the class here
bucketlists = {}
activities = []

def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@app.route('/index')
def index():
    """ opens index page"""
    return render_template('index.html') #returns the home page


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ returns the login page """
    if request.method == 'POST':
        userName = request.form['userName']
        passwd = request.form['passwd']
        if userName in users:
            if passwd == users[userName].password:
                session['logged_in'] = True
            return redirect(url_for('create_bucketlist'))
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST': 
        firstName = request.form['firstName']
        email = request.form['email']
        userName = request.form['userName']
        passwd = request.form['passwd']
        passwd2 = request.form['passwd2']
        if passwd == passwd2:
            new_user = User(firstName, email, userName, passwd)
            users[userName] = new_user
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('email', None)
    session.pop('id', None)
    flash('you are logged out.')
    return redirect(url_for('index'))


@app.route('/mybucketlist', methods=['GET', 'POST'])
@login_required
def create_bucketlist():
    if request.method == 'POST':
        bucketlist = request.form['mybucketlist']
        user_id = session['id']
        flash(bucketlist + ' has been added successful.')
    return render_template('mybucketlist.html')

@app.route('/mybucketlist', methods =['GET', 'POST'])
def update_bucketlist():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session['id']
        add_bucket_list(bucketlist, user_id)
        flash(bucketlist + ' has been updated successful.')
    return render_template('mybucketlist.html')

@app.route('/mybucketlist', methods =['GET', 'POST'])
def delete_bucketlist():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session['id']
        add_bucket_list(bucketlist, user_id)
        flash(bucketlist + ' has been deleted successful.')
      
    return render_template('mybucketlist.html')

@app.route('/bucketlist', methods = ['GET','POST'])
def add_bucketlist_item():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session['id']
        add_bucket_list( bucketlist, user_id)
        flash(bucketlist + 'item has been added succesfully.')

def edit_bucketlist_item():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session ['id']
        edit_bucket_list(bucketlist, user_id)
        flash(bucketlist + 'item has been updated successfully.')
def delete_bucketlist_item():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session['id']



@app.route('/viewbucketlist')
def view_bucketlist():
    return render_template('View.html')
