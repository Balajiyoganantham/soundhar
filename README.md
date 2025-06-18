# Full Stack Development Academy Website

A modern, responsive website for a Full Stack Development Academy built with Flask and Bootstrap 5. The website features course listings, mentor profiles, student testimonials, and a secure payment integration with Razorpay.

## Features

- Responsive design that works on all devices
- Modern UI with smooth animations and transitions
- Course catalog with filtering options
- Detailed course pages with curriculum
- Mentor profiles showcase
- Student testimonials
- Secure payment integration with Razorpay
- Post-enrollment form with file upload
- WhatsApp group integration

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
  - Pillow (for image handling)

- **Payment Integration:**
  - Razorpay

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fullstack-academy.git
cd fullstack-academy
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
```bash
cp .env.example .env
# Edit .env with your configuration
```

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
fullstack-academy/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
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
RAZORPAY_KEY_ID=your-razorpay-key-id
RAZORPAY_KEY_SECRET=your-razorpay-key-secret
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

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Bootstrap team for the amazing framework
- Flask team for the excellent web framework
- Razorpay for the payment integration
- Font Awesome for the icons
- All contributors who have helped with the project 