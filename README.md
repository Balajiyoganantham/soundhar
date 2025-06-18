# One Percentage Academy Website

A modern, responsive website for One Percentage built with Flask and Bootstrap 5. The website features course listings, mentor profiles, student testimonials, and contact form with email functionality.

## Features

- Responsive design that works on all devices
- Modern UI with smooth animations and transitions
- Course catalog with filtering options
- Detailed course pages with curriculum
- Mentor profiles showcase
- Student testimonials
- **Enhanced contact form with real-time feedback and email functionality**
- WhatsApp group integration
- **Success/error message display on contact form submission**
- **Loading states and form validation**

## Tech Stack

- **Frontend:**
  - HTML5
  - CSS3 (with custom variables and animations)
  - Bootstrap 5
  - JavaScript (ES6+)
  - Font Awesome icons
  - Owl Carousel

- **Backend:**
  - Python 3.8+
  - Flask
  - SQLAlchemy
  - Flask-WTF
  - Flask-Mail
  - Pillow (for image handling)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/onepercentage-academy.git
cd onepercentage-academy
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:

```env
# Flask Configuration
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# Database Configuration
DATABASE_URL=sqlite:///C:/Users/balaj/db/mydb.db

# Email Configuration
MAIL_USERNAME=onepercentage51@gmail.com
MAIL_PASSWORD=your-app-password-here
```

**Important Email Setup:**
- The contact form sends emails from `onepercentage51@gmail.com` to `onepercentageedu@gmail.com`
- You need to generate an App Password for Gmail:
  1. Go to your Google Account settings
  2. Enable 2-Step Verification if not already enabled
  3. Go to Security → App passwords
  4. Generate a new app password for "Mail"
  5. Use this app password in the `MAIL_PASSWORD` environment variable

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the development server:
```bash
flask run
```

## Project Structure

```
onepercentage-academy/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this file)
├── static/
│   ├── css/
│   │   └── style.css  # Custom styles
│   ├── js/
│   │   └── main.js    # Custom JavaScript
│   └── images/        # Image assets
├── templates/
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   └── course_detail.html  # Course detail page
└── README.md          # Project documentation
```

## Configuration

Create a `.env` file in the root directory with the following variables:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
MAIL_USERNAME=onepercentage51@gmail.com
MAIL_PASSWORD=your-app-password
```

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## Deployment

The application can be deployed to any platform that supports Python/Flask applications. Here are some recommended platforms:

- Heroku
- DigitalOcean
- AWS Elastic Beanstalk
- Google Cloud Platform

**For Render deployment:**
- Add the environment variables in the Render dashboard
- Set `MAIL_USERNAME` and `MAIL_PASSWORD` in the environment variables section

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Bootstrap team for the amazing framework
- Flask team for the excellent web framework
- Font Awesome for the icons
- All contributors who have helped with the project 