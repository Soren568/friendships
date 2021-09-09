from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.friendships import Friendship
from flask_app.models.users import User

@app.route('/')
def index():
    return redirect('/friendships')

@app.route('/friendships')
def home():
    return render_template("index.html", friendships = Friendship.get_all(), users = User.get_all())

@app.route('/save_user', methods=["POST"])
def save_user():
    User.save(request.form)
    return redirect('/friendships')

@app.route('/save_friendship', methods=["POST"])
def save_friendship():
    Friendship.save_friendship(request.form)
    return redirect('/friendships')