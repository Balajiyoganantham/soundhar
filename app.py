from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')

# Database configuration for both development and production
database_url = os.getenv('DATABASE_URL')
if database_url:
    # Production (Render) - PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
elif os.path.exists(r'C:/Users/balaj/db/mydb.db'):
    # Development (local) - SQLite file
    app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:/Users/balaj/db/mydb.db'
else:
    # Fallback - In-memory SQLite for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

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

def get_data_or_empty(model, **filters):
    """Safely get data from database or return empty list if database error"""
    try:
        if filters:
            return model.query.filter_by(**filters).all()
        return model.query.all()
    except Exception as e:
        print(f"Database error for {model.__name__}: {e}")
        return []

@app.route('/')
def home():
    courses = get_data_or_empty(Course)
    mentors = get_data_or_empty(Mentor)
    testimonials = get_data_or_empty(Testimonial)
    programs = get_data_or_empty(Program, is_active=True)
    services = get_data_or_empty(Service, is_active=True)
    team_members = get_data_or_empty(TeamMember, is_active=True)
    statistics = get_data_or_empty(Statistics, is_active=True)
    
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
    try:
        course = Course.query.get_or_404(course_id)
        faqs = FAQ.query.filter_by(course_id=course_id).all()
        articles = Article.query.filter_by(course_id=course_id).all()
    except Exception as e:
        flash('Course not found or database error', 'error')
        return redirect(url_for('home'))
    
    return render_template('course_detail.html', 
                         course=course,
                         faqs=faqs,
                         articles=articles,
                         razorpay_key=os.getenv('RAZORPAY_KEY_ID'))

@app.route('/enroll/<int:course_id>')
def enroll(course_id):
    try:
        course = Course.query.get_or_404(course_id)
    except Exception as e:
        flash('Course not found', 'error')
        return redirect(url_for('home'))
    return render_template('enrollment.html', course=course)

@app.route('/submit-enrollment', methods=['POST'])
def submit_enrollment():
    if request.method == 'POST':
        # Process the form data and store in database
        flash('Enrollment successful! Please join the WhatsApp group.', 'success')
        return redirect(url_for('home'))

@app.route('/programs')
def programs():
    skill_up = get_data_or_empty(Program, category='Skill Up', is_active=True)
    level_up = get_data_or_empty(Program, category='Level Up', is_active=True)
    update_yourself = get_data_or_empty(Program, category='Update Yourself', is_active=True)
    
    return render_template('programs.html',
                         skill_up=skill_up,
                         level_up=level_up,
                         update_yourself=update_yourself)

@app.route('/about')
def about():
    team_members = get_data_or_empty(TeamMember, is_active=True)
    statistics = get_data_or_empty(Statistics, is_active=True)
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

@app.route('/seed')
def seed_database():
    """Seed the database with sample data"""
    try:
        with app.app_context():
            db.create_all()
            from seed_data import seed_database as seed
            seed()
        flash('Database seeded successfully!', 'success')
    except Exception as e:
        flash(f'Error seeding database: {str(e)}', 'error')
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"Database creation error: {e}")
    app.run(debug=True) 