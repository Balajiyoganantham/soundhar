from app import app, db, Course, FAQ, Article, Program, Service, TeamMember, Statistics, Mentor, Testimonial
from datetime import datetime, date

def seed_database():
    with app.app_context():
        # Clear existing data
        db.session.query(Course).delete()
        db.session.query(FAQ).delete()
        db.session.query(Article).delete()
        db.session.query(Program).delete()
        db.session.query(Service).delete()
        db.session.query(TeamMember).delete()
        db.session.query(Statistics).delete()
        db.session.query(Mentor).delete()
        db.session.query(Testimonial).delete()

        # Create the course
        course = Course(
            title="JavaScript, React, & Node.js – The Complete Full-Stack Web Development Bootcamp",
            subtitle="Become a Full-Stack Web Developer with just ONE course. HTML, CSS, JavaScript, Node, React, PostgreSQL, Web3, and DApps.",
            description="""A comprehensive bootcamp that takes you from beginner to professional full-stack web developer. 
            You'll learn everything you need to know to build complete web applications from scratch.""",
            stream="Web Development",
            price=119.99,
            duration="61.5 hours",
            level="All Levels",
            total_lectures=374,
            rating=4.7,
            total_reviews=439709,
            last_updated=date(2025, 2, 1),
            instructor_name="Dr. Angela Yu",
            instructor_title="Developer and Lead Instructor",
            instructor_bio="""Angela is a developer with a passion for teaching. She is the lead instructor at the London App Brewery, 
            London's leading Programming Bootcamp. She has helped hundreds of thousands of students learn to code and change their lives 
            by becoming developers.""",
            what_youll_learn="""• Build 16 web development projects for your portfolio.
• Master frontend technologies: HTML5, CSS3, Flexbox, Grid, Bootstrap 5.
• Dive into JavaScript ES6, DOM Manipulation, and jQuery.
• Develop server-side applications using Node.js, Express.js, and EJS.
• Understand REST, APIs, and database handling with SQL.
• Implement authentication using OAuth.
• Build dynamic UIs with React.js and React Hooks.
• Deploy decentralized applications on the ICP Live Blockchain.""",
            course_content="""The course is divided into 44 sections with a total of 374 lectures, covering:

Frontend Development:
• HTML5, CSS3, Flexbox, Grid, Bootstrap 5
• JavaScript ES6, DOM Manipulation, jQuery
• React.js, React Hooks, State Management

Backend Development:
• Node.js, Express.js, EJS
• REST, APIs, SQL

Version Control:
• Git, Command Line, GitHub, Remote Repositories

Authentication & Security:
• Handling credentials, Designing secure login, Implementing OAuth for user login

Web3 Development:
• Build a Decentralized App, Deploy to the ICP Live Blockchain""",
            requirements="No programming experience needed - I'll teach you everything you need to know",
            image="web-dev-bootcamp.jpg"
        )

        # Create Programs based on Cybernaut website
        programs = [
            Program(name="Tech Trio", category="Skill Up", description="Comprehensive tech training covering multiple technologies", duration="12 weeks", price=999.99),
            Program(name="UI/UX Design", category="Skill Up", description="Master the art of user interface and experience design", duration="8 weeks", price=799.99),
            Program(name="Full Stack Development", category="Skill Up", description="Complete full-stack web development bootcamp", duration="16 weeks", price=1299.99),
            Program(name="Data Analysis", category="Skill Up", description="Learn data analysis and visualization techniques", duration="10 weeks", price=899.99),
            Program(name="MetaZen", category="Skill Up", description="Advanced AI and machine learning program", duration="14 weeks", price=1199.99),
            Program(name="Hackathon 2024", category="Level Up", description="24-hour coding competition for students", duration="24 hours", price=0),
            Program(name="Coding Competition", category="Level Up", description="Monthly coding challenges and competitions", duration="1 month", price=0),
            Program(name="Tech Interview Series", category="Update Yourself", description="Weekly sessions on technical interview preparation", duration="8 weeks", price=299.99),
            Program(name="Tech IR 5.0", category="Update Yourself", description="Industry roundtable and networking event", duration="1 day", price=199.99),
            Program(name="Tech Summit 2024", category="Update Yourself", description="Annual technology conference and networking event", duration="2 days", price=399.99)
        ]

        # Create Services based on Cybernaut website
        services = [
            Service(name="Premier Educational Solutions", description="Comprehensive training programs for institutions and individuals, designed to meet industry standards and prepare students for real-world challenges.", icon="🎓"),
            Service(name="Institution Partnerships", description="Partnered with 50+ institutions for enhanced learning experiences, providing cutting-edge curriculum and industry connections.", icon="🤝"),
            Service(name="Hands-on Training", description="Practical, project-based learning with real-world applications, ensuring students gain practical experience alongside theoretical knowledge.", icon="🔧"),
            Service(name="AI-driven Tools", description="Advanced educational technology for modern learning, incorporating the latest AI tools and platforms to enhance the learning experience.", icon="🤖")
        ]

        # Create Team Members based on Cybernaut website
        team_members = [
            TeamMember(
                name="Jayasurya Gnanavel",
                position="Founder & Visionary",
                bio="Leading the charge in transforming tech education and creating opportunities for aspiring developers.",
                image_url="jayasurya.jpg",
                linkedin_url="https://linkedin.com/in/jayasurya",
                twitter_url="https://twitter.com/jayasurya"
            ),
            TeamMember(
                name="B. Manish Kumar",
                position="President & UI/UX Designer",
                bio="Expert in user experience design and strategic planning for educational technology solutions.",
                image_url="manish.jpg",
                linkedin_url="https://linkedin.com/in/manish",
                twitter_url="https://twitter.com/manish"
            )
        ]

        # Create Statistics based on Cybernaut website
        statistics = [
            Statistics(name="Students Trained", value=100000, icon="👥"),  # 1L+ students
            Statistics(name="Events Conducted", value=75000, icon="🎪"),  # 75K+ events
            Statistics(name="Google Rating", value=48, icon="⭐"),  # 4.8 rating
            Statistics(name="MOU Signed", value=15, icon="🤝"),  # 15+ MOUs
            Statistics(name="Outreach Programs", value=100, icon="🌍"),  # 100+ programs
            Statistics(name="Years of Impact", value=5, icon="⭐")  # 5 years
        ]

        # Create Mentors
        mentors = [
            Mentor(
                name="Dr. Sarah Johnson",
                position="Senior Software Engineer",
                company="Google",
                experience=8,
                expertise="Full-stack development, Cloud computing, System design",
                bio="Experienced software engineer with expertise in building scalable applications.",
                image_url="sarah.jpg"
            ),
            Mentor(
                name="Michael Chen",
                position="Data Scientist",
                company="Microsoft",
                experience=6,
                expertise="Machine Learning, Data Analysis, Python",
                bio="Passionate about teaching data science and helping students understand complex concepts.",
                image_url="michael.jpg"
            )
        ]

        # Create Testimonials based on Cybernaut website
        testimonials = [
            Testimonial(
                student_name="Anitha",
                feedback="Cybernaut transformed my career completely. The hands-on training and real-world projects helped me land my dream job at a top tech company.",
                rating=5,
                image_url="anitha.jpg"
            ),
            Testimonial(
                student_name="Rajkumar",
                feedback="The Tech Trio program was exactly what I needed. I went from knowing nothing about coding to building full-stack applications.",
                rating=5,
                image_url="rajkumar.jpg"
            ),
            Testimonial(
                student_name="Kavitha",
                feedback="The UI/UX Design course opened up new opportunities for me. The instructors are industry experts and the curriculum is cutting-edge.",
                rating=5,
                image_url="kavitha.jpg"
            ),
            Testimonial(
                student_name="MohanKumar",
                feedback="Cybernaut's approach to learning is unique. They focus on creating leaders, not just employees. This mindset has helped me excel in my career.",
                rating=5,
                image_url="mohankumar.jpg"
            )
        ]

        # Create FAQs
        faqs = [
            FAQ(
                question="What is the duration of the course?",
                answer="The course consists of 61.5 hours of video content, but students typically take 3-4 months to complete it while working on the projects.",
                course_id=1
            ),
            FAQ(
                question="Do I need prior programming experience?",
                answer="No prior programming experience is needed. The course starts from the basics and gradually progresses to advanced topics.",
                course_id=1
            ),
            FAQ(
                question="Will I receive a certificate upon completion?",
                answer="Yes, you will receive a certificate of completion once you finish all the course lectures and projects.",
                course_id=1
            ),
            FAQ(
                question="How can I access the course materials?",
                answer="All course materials, including video lectures, code samples, and project files, are available online through our learning platform.",
                course_id=1
            )
        ]

        # Create Articles
        articles = [
            Article(
                title="What Does a Web Developer Do?",
                author="Kevin Kurtz",
                read_time="15 min read",
                url="#",
                course_id=1
            ),
            Article(
                title="Understanding Kubernetes Architecture",
                author="Jilles Soeters",
                read_time="15 min read",
                url="#",
                course_id=1
            ),
            Article(
                title="UX Design Process: A Step-by-Step Guide to Building Better User Experiences",
                author="Megan Russell",
                read_time="12 min read",
                url="#",
                course_id=1
            )
        ]

        # Add all data to session
        db.session.add(course)
        
        for program in programs:
            db.session.add(program)
            
        for service in services:
            db.session.add(service)
            
        for team_member in team_members:
            db.session.add(team_member)
            
        for stat in statistics:
            db.session.add(stat)
            
        for mentor in mentors:
            db.session.add(mentor)
            
        for testimonial in testimonials:
            db.session.add(testimonial)

        for faq in faqs:
            db.session.add(faq)

        for article in articles:
            db.session.add(article)

        db.session.commit()
        print("Database seeded successfully with exact Cybernaut content!")

if __name__ == "__main__":
    seed_database() 