from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_migrate import Migrate
from datetime import datetime
import os
from dotenv import load_dotenv
import json

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'onepercentage51@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', '')  # App password will be set in .env
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME', 'onepercentage51@gmail.com')

mail = Mail(app)

# Database Configuration
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'courses.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
# For Render deployment with persistent disk
if 'RENDER' in os.environ:
    # The disk is mounted at '/var/data'
    data_dir = '/var/data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(data_dir, 'courses.db')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
    what_youll_learn = db.Column(db.Text, nullable=True)
    course_content = db.Column(db.Text, nullable=True)
    requirements = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

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
    rating = db.Column(db.Float, nullable=False)
    feedback = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    position = db.Column(db.String(100))
    company = db.Column(db.String(100))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=True)

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

# Custom CLI command to reset and seed database
@app.cli.command("seed-db")
def seed_db():
    """Resets the database and seeds it with initial data."""
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()
    
    # Import and run the seeder function
    from seed_data import seed_data
    seed_data()
    
    print("Database has been reset and seeded successfully.")

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
        
        # Parse curriculum JSON for course ID 8-12 (Programming courses), 13 (UI/UX College), 14 (AI/ML), 15 (Cybersecurity), 16 (Data Analyst), 17 (Advanced Web Development), 18 (Data Science), 19 (Advanced UI/UX), 20 (Full Stack Development), 21 (Trading), 22 (E-Commerce), and 23 (Drop-shipping)
        curriculum_modules = None
        if course_id in [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] and course.course_content:
            try:
                curriculum_modules = json.loads(course.course_content)
            except (json.JSONDecodeError, TypeError):
                curriculum_modules = None
                
    except Exception as e:
        flash('Course not found or database error', 'error')
        return redirect(url_for('home'))
    
    return render_template('course_detail.html', 
                         course=course,
                         faqs=faqs,
                         articles=articles,
                         curriculum_modules=curriculum_modules)

@app.route('/enroll/<int:course_id>', methods=['GET', 'POST'])
def enroll(course_id):
    try:
        course = Course.query.get_or_404(course_id)
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            education = request.form.get('education')
            profile = request.form.get('profile')
            
            # Validate required fields
            if not all([name, email, phone, education, profile]):
                flash('Please fill in all required fields', 'error')
                return redirect(url_for('course_detail', course_id=course_id))
            
            # Send confirmation email to admin and user
            try:
                msg = Message(
                    subject=f"New Enrollment: {course.title}",
                    recipients=[app.config['MAIL_USERNAME']],
                    body=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nEducation: {education}\nProfile: {profile}\nCourse: {course.title}"
                )
                mail.send(msg)
                # Confirmation to user
                user_msg = Message(
                    subject=f"Enrollment Confirmation: {course.title}",
                    recipients=[email],
                    body=f"Thank you for enrolling in {course.title}! We have received your details and will contact you soon."
                )
                mail.send(user_msg)
            except Exception as e:
                print(f"Mail error: {e}")
            
            flash('Thank you for enrolling! We have received your details and will contact you soon.', 'success')
            return redirect(url_for('course_detail', course_id=course_id))
        
        # GET request: redirect to course detail page
        return redirect(url_for('course_detail', course_id=course_id))
        
    except Exception as e:
        flash('Course not found', 'error')
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

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Send email
        msg = Message(f'New Contact Form: {subject}',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[os.environ.get('MAIL_RECIPIENT')])
        msg.body = f"""
        You have a new contact form submission from your website.

        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """
        try:
            mail.send(msg)
            flash('Your message has been sent successfully! We will get back to you shortly.', 'success')
        except Exception as e:
            current_app.logger.error(f"Failed to send email: {e}")
            flash('Sorry, there was an error sending your message. Please try again later.', 'danger')
        
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone', '')
            subject = request.form.get('subject')
            message = request.form.get('message')
            
            # Validate required fields
            if not all([name, email, subject, message]):
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return {'error': 'Please fill in all required fields'}, 400
                flash('Please fill in all required fields', 'error')
                return redirect(url_for('contact'))
            
            # Create email subject
            email_subject = f"Contact Form: {subject} - {name}"
            
            # Create email body
            email_body = f"""
New contact form submission from One Percentage website:

Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject}

Message:
{message}

---
This email was sent from the contact form on the One Percentage website.
            """
            
            # Create and send email
            msg = Message(
                subject=email_subject,
                recipients=['onepercentageedu@gmail.com'],
                body=email_body
            )
            
            mail.send(msg)
            
            # Check if it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return {'success': 'Message sent successfully!'}, 200
            
            flash('Thank you for your message! We will get back to you soon.', 'success')
            
        except Exception as e:
            print(f"Email error: {e}")
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return {'error': 'Sorry, there was an error sending your message. Please try again or contact us directly.'}, 500
            
            flash('Sorry, there was an error sending your message. Please try again or contact us directly.', 'error')
        
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