from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from models import db, User,  Event
from datetime import datetime, timedelta
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')  # Required for server-side plotting
import matplotlib.pyplot as plt
import io
import os
import base64
from matplotlib.patches import Circle



app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vivek.sqlite'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)  # Attach to the Flask app
login_manager.login_view = 'user_login'  # Redirect unauthenticated users to login page

# User loader function (required for Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Load user from database

@app.route("/")
def home():
    return redirect(url_for('first_page'))

@app.route('/first_page')
def first_page():
    return render_template('home_page.html')

 
 
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            if user.blocked:
                flash('Your account is blocked. Please contact admin.', 'danger')
                return redirect(url_for('login'))

            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash(f"Welcome back, {user.username}!", 'success')

            # Redirect based on role (optional)
            if user.role == 0:
                return redirect(url_for('admin_dashboard'))  # example route
            else:
                return redirect(url_for('user_dashboard'))  # example route
        else:
            flash('Invalid email or password', 'danger')
            return redirect(url_for('login'))

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Collect form data
        username = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = generate_password_hash(request.form["password"], method='pbkdf2:sha256')

        # Check if user already exists (optional but recommended)
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username or email already exists.", "warning")
            return redirect(url_for("register"))

        # Create and save new user
        new_user = User(username=username, email=email, phone=phone, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("user_login"))  # Make sure you have a login route

    return render_template("register.html")
@app.route("/user_login", methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password) and user.role == 1:
            if user.blocked:
                flash("Your account is blocked. Please contact the administrator.", "danger")
                return redirect(url_for('user_login'))
            
            login_user(user)  # Flask-Login: Log in the user
            flash('Login successful!')
            return redirect(url_for('user_home_page', name=username))
        else:
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('user_login'))

    return render_template("login.html", role='User')

@app.route("/admin_login", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password) and user.role == 0:
            login_user(user)  # Flask-Login: Log in admin
            flash('Login successful!')
            return redirect(url_for('admin_dashboard', name=username))
        else:
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('admin_login'))
    
    return render_template('admin_login.html')

@app.route("/logout")
def logout():
    session.clear()  # Clear all session data
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))  # This should match your route for home_page.html

# @app.route("/admin_dashboard/<string:username>")
# def admin_dashboard(username):
    
#     return render_template("admin_dashboard.html",username=username)


@app.route("/home_page/<string:name>")
def home_page(name):

#     # chapters = Subject.query.get_or_404(subject_id)
#     subjects=Subject.query.all()
#     chapters=Chapter.query.all()
#     quizzes=Quiz.query.all()
#     questions=Question.query.all()
    return render_template("home_page.html",name=name)
@app.route("/user_home_page/<string:name>")
def user_home_page(name):
      events = Event.query.all()
#     # chapters = Subject.query.get_or_404(subject_id)
#     subjects=Subject.query.all()
#     chapters=Chapter.query.all()
#     quizzes=Quiz.query.all()
#     questions=Question.query.all()
      return render_template("user_home_page.html",name=name)
 
@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']
        start_dt = request.form['startDate']
        end_dt = request.form['endDate']
        category = request.form['category']
        reg_start = request.form['regStart']
        reg_end = request.form['regEnd']
        organizer_id = 1  # Assuming the organizer is the logged-in user 
        # Handle file upload
        photo = request.files.get('photo')
        photo_filename = None
        if photo:
            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join('static/images', photo_filename))

        # Save event
        event = Event(
            name=name,
            location=location,
            description=description,
            start_datetime=datetime.strptime(start_dt, '%Y-%m-%dT%H:%M'),
            end_datetime=datetime.strptime(end_dt, '%Y-%m-%dT%H:%M'),
            category=category,
            registration_start=datetime.strptime(reg_start, '%Y-%m-%dT%H:%M'),
            registration_end=datetime.strptime(reg_end, '%Y-%m-%dT%H:%M'),
            photo_filename=photo_filename,
            organizer_id=organizer_id
        )
        db.session.add(event)
        db.session.commit()
        events = Event.query.all()
        flash('Event added successfully!', 'success')
        # print(events)
        return redirect(url_for('user_home_page', name="vivek"))

    return render_template('add_event.html')

# Dummy event data (you should use your database instead)
events = {
    1: {
        "title": "Live Music Festival",
        "date": "Aug 14",
        "desc": "Experience live music, local food and beverages.",
        "location": "Silver Auditorium, Ahmedabad, Gujarat",
        "image": "/static/images/tennis-match.jpg",
        "tag": "Music"
    },
    # Add other events similarly
}

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    event = events.get(event_id)
    if not event:
        return "Event not found", 404
    return render_template("event_detail.html", event=event)
# @app.route("/admin_dashboard/<string:name>")
# def admin_dashboard(name):
#     subjects=Subject.query.all()
#     chapters=Chapter.query.all()
#     users = User.query.all()
#     # chapters = Subject.query.get_or_404(subject_id)
#     return render_template("admin_dashboard.html",users=users,subjects=subjects,chapters=chapters,name=name)
 

 #         circle_chart=circle_chart
#     )

# @app.route("/search/<name>",methods=["GET","POST"])
# def search(name):
#     if request.method=="POST":
#        search_txt=request.form.get("search_txt")
#        by_subject=search_by_subject(search_txt)
#        b_chapter=search_by_chapter(search_txt)
#        print(b_chapter)
#        if by_subject:
#            return render_template("admin_dashboard.html",name=name,subjects=by_subject)
#        elif b_chapter:
#            return render_template("admin_dashboard.html",name=name,subjects=b_chapter)

#     return redirect(url_for("admin_dashboard",name=name))

# @app.route("/scores_dashboard/<string:username>")
# @login_required
# def scores_dashboard(username):
#     # Get the current user's scores
#     user_scores = db.session.query(
#         Scores.id,
#         Quiz.quiz_name,
#         Quiz.no_of_question,
#         Scores.total_scored
#     ).join(
#         Quiz, Scores.quiz_id == Quiz.id
#     ).filter(
#         Scores.user_id == current_user.id
#     ).all()
    
#     return render_template("scores_dashboard.html", scores=user_scores, username=username)

# @app.route("/search_scores", methods=["POST"])
# @login_required
# def search_scores():
#     search_query = request.form.get("search_query", "")
    
#     # Search in quiz names and scores
#     user_scores = db.session.query(
#         Scores.id,
#         Quiz.quiz_name,
#         Quiz.no_of_question,
#         Scores.total_scored
#     ).join(
#         Quiz, Scores.quiz_id == Quiz.id
#     ).filter(
#         Scores.user_id == current_user.id,
#         Quiz.quiz_name.ilike(f"%{search_query}%")
#     ).all()
    
#     return render_template("scores_dashboard.html", scores=user_scores, username=current_user.username)

# def get_user_quiz_scores(user_id):
#     """Get all quiz scores for a specific user"""
#     return Scores.query.filter_by(user_id=user_id).all()

# def get_quiz_summary(quiz_id, user_id):
#     """Get summary of a specific quiz for a user"""
#     return Scores.query.filter_by(quiz_id=quiz_id, user_id=user_id).first()

def func():
    admin = User.query.filter_by(username="admin").first()
    if not admin:
        admin = User(
            username='admin',
            email='admin@gmail.com',
            phone='1234567890',        
            password=generate_password_hash('admin123', method='pbkdf2:sha256'), 
            role=0
        )
        db.session.add(admin)
        db.session.commit()
        return  'success'
    pass

# def search_by_subject(search_txt):
#     subjects=Subject.query.filter(Subject.name.ilike(f"%{search_txt}%")).all()
#     return subjects

# def search_by_chapter(search_txt):
#     # chapters=Chapter.query.filter(Chapter.name.ilike(f"%{search_txt}%"))
#     chapters=Chapter.query.filter(Chapter.name.ilike(f"%{search_txt}%")).all()
#     return chapters

# def get_subject(id):
#     subject=Subject.query.filter_by(id=id).first()
#     return subject

# def get_chapter(id):
#     chapter=Chapter.query.filter_by(id=id).first()
#     return chapter
# def get_question(id):
#     question=Question.query.filter_by(id=id).first()
#     return question

# def get_quiz(id):
#     quiz=Quiz.query.filter_by(id=id).first()
#     return quiz

# def get_quiz_id(id):
#     quiz_id=Quiz.query.filter_by(id=id).first()
#     return quiz_id
    
# def get_subject_name(name):
#     subject_name=Subject.query.filter_by(name=name).first()
#     return subject_name

# def get_chapter_name(name):
#     chapter_name=Chapter.query.filter_by(name=name).first()
#     return chapter_name

# def convert_duration_to_seconds(duration):
#     # Convert HH:MM to total seconds
#     time_obj = datetime.strptime(duration, "%H:%M")
#     return time_obj.hour * 3600 + time_obj.minute * 60


# # Define the custom filter
# @app.template_filter('time_format')
# def format_time(seconds):
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     return f"{hours:02}:{minutes:02}"
 
#Initialize the database
with app.app_context():
    db.create_all()
    func()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure the tables are created
    app.run(debug=True)  # Start the server