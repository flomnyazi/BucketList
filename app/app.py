from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from app.users.users import User
from app.bucketlists.bucketlists import BucketList


app = Flask(__name__)
app.secret_key = 'topsecret'


# Data structure
users = {} # we save the class here
bucketlists = {}
activities = []

def get_id_for_userName(userName):
    for user in users:
        print(user)
        if users[user].userName == userName:
            return users[user].id

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
        if get_id_for_userName(userName):
            if passwd == users[get_id_for_userName(userName)].password:
                session['logged_in'] = True
                session['id']= get_id_for_userName(userName)
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
            users[new_user.id] = new_user
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('email', None)
    session.pop('id', None)
    flash('you are logged out.')
    return redirect(url_for('index'))

@app.route('/mybucketlist',methods =['GET','POST'])
@login_required
def create_bucketlist():
    if request.method == 'POST':
        bucketlist = request.form['BucketListName']
        user_id = session['id']
        new_bucketlist = BucketList(bucketlist,user_id)
        if user_id in bucketlists:
            bucketlists[user_id][new_bucketlist.bucketlist_id] = new_bucketlist   
        else:
            bucketlists[user_id] = {new_bucketlist.bucketlist_id: new_bucketlist}


        return redirect(url_for('view_bucketlist'))
    return render_template('mybucketlist.html')

@app.route('/edit_bucketlist/<bucket_id>', methods =['GET', 'POST'])
def update_bucketlist(bucket_id):
    bucketlist = bucketlists[session['id']][bucket_id]
    if request.method == 'POST':
        bucketlist = request.form['/bucketlist']
        user_id = session['id']
        return redirect(url_for('view_bucketlist'))
    return render_template('bucketlist.html', bucketlist = bucketlists)

@app.route('/del_bucketlist', methods =['GET', 'POST'])
def delete_bucketlist():
    if request.method == 'POST':
        bucketlist = request.form['BucketListName']
        user_id = session['id']
        return redirect (url_for('view_bucketlist'))
    return render_template('mybucketlist.html')

@app.route('/bucketlist', methods = ['GET','POST'])
def add_bucketlist_item():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session['id']
        flash(bucketlist + 'item has been added succesfully.')


def edit_bucketlist_item():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session ['id']
        flash(bucketlist + 'item has been updated successfully.')

def delete_bucketlist_item():
    if request.method == 'POST':
        bucketlist = request.form['bucketlist']
        user_id = session['id']



@app.route('/view')
def view_bucketlist():
    return render_template('View.html', bucketlists=bucketlists[session ['id']])

