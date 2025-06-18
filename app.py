from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')

# Database configuration for both development and production
if os.getenv('DATABASE_URL'):
    # Production (Render)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    # Development (local)
    app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:/Users/balaj/db/mydb.db'

db = SQLAlchemy(app)

# Models
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(500))
    description = db.Column(db.Text, nullable=False)
    stream = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.String(50))
    level = db.Column(db.String(50))
    total_lectures = db.Column(db.Integer)
    rating = db.Column(db.Float)
    total_reviews = db.Column(db.Integer)
    last_updated = db.Column(db.Date)
    instructor_name = db.Column(db.String(100))
    instructor_title = db.Column(db.String(200))
    instructor_bio = db.Column(db.Text)
    what_youll_learn = db.Column(db.Text)
    course_content = db.Column(db.Text)
    requirements = db.Column(db.Text)
    image = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Mentor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(200))
    company = db.Column(db.String(200))
    experience = db.Column(db.Integer)
    expertise = db.Column(db.Text)
    bio = db.Column(db.Text)
    image_url = db.Column(db.String(500))

class Testimonial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer)
    feedback = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    position = db.Column(db.String(200))
    company = db.Column(db.String(200))

class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(100))
    read_time = db.Column(db.String(50))
    url = db.Column(db.String(500))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Skill Up, Level Up, Update Yourself
    description = db.Column(db.Text)
    duration = db.Column(db.String(50))
    price = db.Column(db.Float)
    image_url = db.Column(db.String(500))
    is_active = db.Column(db.Boolean, default=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True)

class TeamMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(200))
    bio = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    linkedin_url = db.Column(db.String(500))
    twitter_url = db.Column(db.String(500))
    is_active = db.Column(db.Boolean, default=True)

class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    icon = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True)

@app.route('/')
def home():
    courses = Course.query.all()
    mentors = Mentor.query.all()
    testimonials = Testimonial.query.all()
    programs = Program.query.filter_by(is_active=True).all()
    services = Service.query.filter_by(is_active=True).all()
    team_members = TeamMember.query.filter_by(is_active=True).all()
    statistics = Statistics.query.filter_by(is_active=True).all()
    
    return render_template('index.html', 
                         courses=courses, 
                         mentors=mentors, 
                         testimonials=testimonials,
                         programs=programs,
                         services=services,
                         team_members=team_members,
                         statistics=statistics)

@app.route('/course/<int:course_id>')
def course_detail(course_id):
    course = Course.query.get_or_404(course_id)
    faqs = FAQ.query.filter_by(course_id=course_id).all()
    articles = Article.query.filter_by(course_id=course_id).all()
    return render_template('course_detail.html', 
                         course=course,
                         faqs=faqs,
                         articles=articles,
                         razorpay_key=os.getenv('RAZORPAY_KEY_ID'))

@app.route('/enroll/<int:course_id>')
def enroll(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('enrollment.html', course=course)

@app.route('/submit-enrollment', methods=['POST'])
def submit_enrollment():
    if request.method == 'POST':
        # Process the form data and store in database
        flash('Enrollment successful! Please join the WhatsApp group.', 'success')
        return redirect(url_for('home'))

@app.route('/programs')
def programs():
    skill_up = Program.query.filter_by(category='Skill Up', is_active=True).all()
    level_up = Program.query.filter_by(category='Level Up', is_active=True).all()
    update_yourself = Program.query.filter_by(category='Update Yourself', is_active=True).all()
    
    return render_template('programs.html',
                         skill_up=skill_up,
                         level_up=level_up,
                         update_yourself=update_yourself)

@app.route('/about')
def about():
    team_members = TeamMember.query.filter_by(is_active=True).all()
    statistics = Statistics.query.filter_by(is_active=True).all()
    return render_template('about.html',
                         team_members=team_members,
                         statistics=statistics)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        # Process contact form
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 