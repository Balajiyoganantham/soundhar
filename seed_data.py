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
• Master frontend technologies: HTML5, CSS3, JavaScript, Node, React, PostgreSQL, Web3, and DApps.
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
        db.session.add(course)

        # UI/UX Design Course
        uiux_course = Course(
            id=2,
            title="Advanced UI/UX Design Course",
            subtitle="Master advanced design thinking, user research, prototyping, and more.",
            description="The Advanced UI/UX Design Course is crafted for those who have a basic understanding of design and want to build expertise in creating seamless, user‑centric digital experiences. You'll learn advanced design methodologies, work on complex projects, and gain hands‑on experience with industry‑leading tools and practices — making you job‑ready as a UI/UX Designer or Product Designer.",
            stream="UI/UX Design",
            price=3000,
            duration="60+ Hours",
            level="Intermediate-Advanced",
            total_lectures=50,
            rating=4.7,
            total_reviews=9000,
            last_updated=datetime.now().date(),
            instructor_name="Expert UI/UX Mentor",
            instructor_title="Senior Product Designer",
            instructor_bio="Industry expert in UI/UX with 10+ years of experience.",
            what_youll_learn="Advanced design thinking, user research, prototyping, Figma, Adobe XD, usability testing, and more.",
            course_content="See course detail page for full module breakdown.",
            requirements="Basic understanding of design principles.",
            image="ui-ux-design.jpg"
        )
        db.session.add(uiux_course)

        # Full Stack Development Course
        fullstack_course = Course(
            id=3,
            title="Full Stack Development",
            subtitle="Complete full-stack web development bootcamp",
            description="Master both frontend and backend development with our comprehensive full-stack course.",
            stream="Web Development",
            price=3500,
            duration="60+ Hours",
            level="Intermediate",
            total_lectures=60,
            rating=4.8,
            total_reviews=10000,
            last_updated=datetime.now().date(),
            instructor_name="Full Stack Expert",
            instructor_title="Senior Full Stack Developer",
            instructor_bio="Expert in full-stack development with 8+ years of experience.",
            what_youll_learn="Frontend and backend development, database management, deployment, and more.",
            course_content="See course detail page for full module breakdown.",
            requirements="Basic programming knowledge.",
            image="full-stack.jpg"
        )
        db.session.add(fullstack_course)

        # Data Analytics Course
        data_analytics_course = Course(
            id=4,
            title="Data Analyst – PRO Combo Pack",
            subtitle="Ready for Analyst Internships / Entry Jobs",
            description="Comprehensive data analysis course preparing you for analyst roles.",
            stream="Data Analytics",
            price=1499,
            duration="8 Weeks",
            level="Beginner-Intermediate",
            total_lectures=40,
            rating=4.8,
            total_reviews=15000,
            last_updated=datetime.now().date(),
            instructor_name="Data Analytics Expert",
            instructor_title="Senior Data Analyst",
            instructor_bio="Expert in data analysis with 6+ years of experience.",
            what_youll_learn="Data analysis, visualization, statistical analysis, and more.",
            course_content="See course detail page for full module breakdown.",
            requirements="Basic mathematics and computer skills.",
            image="data-analytics.jpg"
        )
        db.session.add(data_analytics_course)

        # Data Science Course
        data_science_course = Course(
            id=5,
            title="Data Science – PRO Combo Pack",
            subtitle="Portfolio-ready + Interview Prep",
            description="Advanced data science course with portfolio building and interview preparation.",
            stream="Data Science",
            price=1999,
            duration="10–12 Weeks",
            level="Intermediate-Advanced",
            total_lectures=50,
            rating=4.8,
            total_reviews=15000,
            last_updated=datetime.now().date(),
            instructor_name="Data Science Expert",
            instructor_title="Senior Data Scientist",
            instructor_bio="Expert in data science with 7+ years of experience.",
            what_youll_learn="Machine learning, statistical analysis, data visualization, and more.",
            course_content="See course detail page for full module breakdown.",
            requirements="Basic programming and statistics knowledge.",
            image="data-science.png"
        )
        db.session.add(data_science_course)

        # Cyber Security Course
        cyber_security_course = Course(
            id=6,
            title="Cyber Security – PRO Combo Pack",
            subtitle="CEH-Ready Beginner + Internship Opportunity",
            description="Comprehensive cybersecurity course preparing you for CEH certification.",
            stream="Cyber Security",
            price=1499,
            duration="8–10 Weeks",
            level="Beginner-Intermediate",
            total_lectures=45,
            rating=4.8,
            total_reviews=15000,
            last_updated=datetime.now().date(),
            instructor_name="Cyber Security Expert",
            instructor_title="Senior Security Analyst",
            instructor_bio="Expert in cybersecurity with 8+ years of experience.",
            what_youll_learn="Network security, ethical hacking, incident response, and more.",
            course_content="See course detail page for full module breakdown.",
            requirements="Basic networking knowledge.",
            image="cyber-security.png"
        )
        db.session.add(cyber_security_course)

        # Certificate Course
        certificate_course = Course(
            id=7,
            title="Skills Certificate Program",
            subtitle="Get your quality Skills Certificate from One Percentage",
            description="Professional certification program to validate your skills.",
            stream="Certification",
            price=500,
            duration="4 Weeks",
            level="All Levels",
            total_lectures=20,
            rating=4.9,
            total_reviews=5000,
            last_updated=datetime.now().date(),
            instructor_name="Certification Expert",
            instructor_title="Certification Specialist",
            instructor_bio="Expert in professional certifications with 5+ years of experience.",
            what_youll_learn="Professional certification preparation and skill validation.",
            course_content="See course detail page for full module breakdown.",
            requirements="Basic knowledge in chosen field.",
            image="certificate.png"
        )
        db.session.add(certificate_course)

        # Python Programming Course
        python_course = Course(
            id=8,
            title="Python Programming Masterclass",
            subtitle="Learn Python from scratch to advanced level with hands-on projects and real-world applications",
            description="The Python Programming Masterclass is designed for students who want to master Python programming from fundamentals to advanced concepts. This comprehensive course covers everything from basic syntax to advanced topics like web development, data analysis, automation, and machine learning. You'll build real-world projects, work with popular libraries, and gain the skills needed for a successful career in Python development.",
            stream="Programming",
            price=2000,
            duration="40+ Hours",
            level="Beginner to Intermediate",
            total_lectures=45,
            rating=4.8,
            total_reviews=12000,
            last_updated=datetime.now().date(),
            instructor_name="Rajesh Kumar",
            instructor_title="Senior Python Developer & Tech Lead",
            instructor_bio="Rajesh Kumar is a senior Python developer with 8+ years of experience in software development and teaching. He has worked with top tech companies and startups, specializing in web development, data science, and automation. Rajesh has trained 5000+ students and is passionate about making programming accessible to everyone.",
            what_youll_learn="""• Master Python fundamentals: variables, data types, control structures, and functions
• Object-Oriented Programming: classes, inheritance, polymorphism, and encapsulation
• Web Development: Build web applications using Flask and Django frameworks
• Data Analysis: Work with pandas, NumPy, and matplotlib for data manipulation
• Database Integration: Connect Python applications with SQLite, MySQL, and MongoDB
• API Development: Create RESTful APIs and work with external APIs
• Automation & Scripting: Automate tasks and build useful scripts
• Best Practices: Code organization, testing, debugging, and version control with Git""",
            course_content='[{"title": "Module 1: Python Fundamentals", "duration": "8 hours", "description": "Introduction to Python, variables, data types, operators, control structures (if-else, loops), functions, and basic input/output operations. Hands-on exercises and mini-projects."}, {"title": "Module 2: Data Structures & Algorithms", "duration": "10 hours", "description": "Lists, tuples, dictionaries, sets, string manipulation, list comprehensions, and basic algorithms. Problem-solving techniques and coding challenges."}, {"title": "Module 3: Object-Oriented Programming", "duration": "8 hours", "description": "Classes, objects, inheritance, polymorphism, encapsulation, and abstraction. Building complex applications using OOP principles."}, {"title": "Module 4: File Handling & Exception Handling", "duration": "6 hours", "description": "Reading and writing files, working with different file formats (CSV, JSON, XML), exception handling, and error management."}, {"title": "Module 5: Web Development with Flask", "duration": "8 hours", "description": "Introduction to web development, Flask framework, routing, templates, forms, and building a complete web application."}, {"title": "Module 6: Data Analysis & Visualization", "duration": "6 hours", "description": "Working with pandas for data manipulation, NumPy for numerical computing, and matplotlib for data visualization."}, {"title": "Module 7: Database Integration", "duration": "4 hours", "description": "Connecting Python with databases, SQLite operations, and building applications with persistent data storage."}]',
            requirements="Basic computer knowledge and logical thinking. No prior programming experience required. A computer with Python installed (installation guidance provided). Enthusiasm to learn and practice coding regularly.",
            image="python.png"
        )
        db.session.add(python_course)

        # Java Programming Course
        java_course = Course(
            id=9,
            title="Java Programming Complete Course",
            subtitle="Master Java programming from basics to advanced concepts with enterprise-level applications",
            description="The Java Programming Complete Course is designed for students who want to master Java programming and prepare for a career in software development. This comprehensive course covers everything from basic syntax to advanced topics like Spring Framework, microservices, and enterprise application development. You'll learn object-oriented programming, build real-world applications, and gain the skills needed for Java development roles in top companies.",
            stream="Programming",
            price=2200,
            duration="45+ Hours",
            level="Beginner to Intermediate",
            total_lectures=50,
            rating=4.7,
            total_reviews=10000,
            last_updated=datetime.now().date(),
            instructor_name="Priya Sharma",
            instructor_title="Senior Java Developer & Software Architect",
            instructor_bio="Priya Sharma is a senior Java developer with 10+ years of experience in enterprise software development. She has worked with major tech companies and financial institutions, specializing in Java EE, Spring Framework, and microservices architecture. Priya has trained 3000+ students and is certified in Java technologies.",
            what_youll_learn="""• Master Java fundamentals: syntax, data types, control structures, and object-oriented programming
• Advanced Java concepts: collections, generics, exception handling, and multithreading
• Spring Framework: Dependency injection, Spring Boot, and building RESTful APIs
• Database connectivity: JDBC, JPA, and working with MySQL and PostgreSQL
• Web Development: Servlets, JSP, and building web applications
• Testing: Unit testing with JUnit and integration testing
• Build Tools: Maven and Gradle for project management
• Best Practices: Design patterns, clean code principles, and enterprise development""",
            course_content='[{"title": "Module 1: Java Fundamentals", "duration": "10 hours", "description": "Introduction to Java, variables, data types, operators, control structures, arrays, and basic input/output. Setting up development environment and writing first Java programs."}, {"title": "Module 2: Object-Oriented Programming", "duration": "12 hours", "description": "Classes, objects, inheritance, polymorphism, encapsulation, abstraction, interfaces, and abstract classes. Building complex applications using OOP principles."}, {"title": "Module 3: Advanced Java Concepts", "duration": "10 hours", "description": "Collections framework, generics, exception handling, file I/O, and string manipulation. Working with complex data structures and error handling."}, {"title": "Module 4: Multithreading & Concurrency", "duration": "6 hours", "description": "Thread creation, synchronization, thread pools, and concurrent programming. Building responsive and efficient applications."}, {"title": "Module 5: Database Connectivity", "duration": "8 hours", "description": "JDBC basics, connecting to databases, executing queries, and working with MySQL and PostgreSQL. Building data-driven applications."}, {"title": "Module 6: Web Development", "duration": "6 hours", "description": "Servlets, JSP, web application architecture, and building dynamic web applications. Understanding web technologies and deployment."}, {"title": "Module 7: Spring Framework", "duration": "8 hours", "description": "Spring Core, dependency injection, Spring Boot, and building RESTful APIs. Modern Java development practices and frameworks."}, {"title": "Module 8: Testing & Best Practices", "duration": "4 hours", "description": "Unit testing with JUnit, integration testing, design patterns, and clean code principles. Professional development practices."}]',
            requirements="Basic computer knowledge and logical thinking. No prior programming experience required. A computer with Java Development Kit (JDK) installed (installation guidance provided). Enthusiasm to learn and practice coding regularly.",
            image="java.png"
        )
        db.session.add(java_course)

        # C++ Programming Course
        cpp_course = Course(
            id=10,
            title="C++ Programming Comprehensive Course",
            subtitle="Master C++ programming from fundamentals to advanced concepts with system programming and game development",
            description="The C++ Programming Comprehensive Course is designed for students who want to master C++ programming and prepare for careers in system programming, game development, and high-performance computing. This course covers everything from basic syntax to advanced topics like memory management, templates, STL, and modern C++ features. You'll build real-world applications, work with complex algorithms, and gain the skills needed for C++ development roles.",
            stream="Programming",
            price=1800,
            duration="35+ Hours",
            level="Beginner to Intermediate",
            total_lectures=40,
            rating=4.6,
            total_reviews=8000,
            last_updated=datetime.now().date(),
            instructor_name="Amit Patel",
            instructor_title="Senior C++ Developer & System Architect",
            instructor_bio="Amit Patel is a senior C++ developer with 12+ years of experience in system programming, game development, and embedded systems. He has worked with major gaming companies and tech firms, specializing in performance optimization, memory management, and cross-platform development. Amit has trained 2000+ students and is passionate about teaching complex programming concepts.",
            what_youll_learn="""• Master C++ fundamentals: syntax, data types, control structures, and functions
• Object-Oriented Programming: classes, inheritance, polymorphism, and encapsulation
• Memory Management: pointers, references, dynamic memory allocation, and smart pointers
• Advanced C++ Features: templates, STL containers, algorithms, and lambda expressions
• Modern C++: C++11/14/17 features, auto keyword, range-based for loops, and move semantics
• File I/O and Exception Handling: working with files, error handling, and robust programming
• Algorithm Design: sorting, searching, and data structure implementation
• Best Practices: code organization, debugging, optimization, and professional development""",
            course_content='[{"title": "Module 1: C++ Fundamentals", "duration": "8 hours", "description": "Introduction to C++, variables, data types, operators, control structures, functions, and basic input/output. Setting up development environment and writing first C++ programs."}, {"title": "Module 2: Object-Oriented Programming", "duration": "10 hours", "description": "Classes, objects, constructors, destructors, inheritance, polymorphism, encapsulation, and abstraction. Building complex applications using OOP principles."}, {"title": "Module 3: Memory Management", "duration": "8 hours", "description": "Pointers, references, dynamic memory allocation, smart pointers (unique_ptr, shared_ptr), and memory leak prevention. Understanding memory layout and management."}, {"title": "Module 4: Advanced C++ Features", "duration": "10 hours", "description": "Templates, function templates, class templates, STL containers (vector, list, map, set), algorithms, and lambda expressions. Modern C++ programming techniques."}, {"title": "Module 5: File I/O and Exception Handling", "duration": "6 hours", "description": "File streams, reading and writing files, exception handling, try-catch blocks, and creating robust applications with proper error handling."}, {"title": "Module 6: Modern C++ Features", "duration": "6 hours", "description": "C++11/14/17 features, auto keyword, range-based for loops, move semantics, and other modern C++ improvements for efficient programming."}, {"title": "Module 7: Algorithm Design and Data Structures", "duration": "8 hours", "description": "Implementing common algorithms, sorting techniques, searching algorithms, and custom data structures. Problem-solving and optimization techniques."}, {"title": "Module 8: Best Practices and Project Work", "duration": "4 hours", "description": "Code organization, debugging techniques, performance optimization, and building a complete C++ project. Professional development practices."}]',
            requirements="Basic computer knowledge and logical thinking. No prior programming experience required. A computer with a C++ compiler installed (installation guidance provided). Enthusiasm to learn and practice coding regularly.",
            image="cpp.png"
        )
        db.session.add(cpp_course)

        # JavaScript Programming Course
        javascript_course = Course(
            id=11,
            title="JavaScript Programming Complete Course",
            subtitle="Master JavaScript from basics to advanced concepts with modern web development and Node.js",
            description="The JavaScript Programming Complete Course is designed for students who want to master JavaScript programming and prepare for careers in web development, full-stack development, and modern application development. This comprehensive course covers everything from basic syntax to advanced topics like ES6+ features, asynchronous programming, DOM manipulation, and Node.js backend development. You'll build real-world web applications and gain the skills needed for JavaScript development roles.",
            stream="Programming",
            price=1900,
            duration="30+ Hours",
            level="Beginner to Intermediate",
            total_lectures=35,
            rating=4.8,
            total_reviews=11000,
            last_updated=datetime.now().date(),
            instructor_name="Kavya Reddy",
            instructor_title="Senior JavaScript Developer & Full-Stack Engineer",
            instructor_bio="Kavya Reddy is a senior JavaScript developer with 9+ years of experience in web development and full-stack engineering. She has worked with major tech companies and startups, specializing in modern JavaScript frameworks, Node.js, and cloud technologies. Kavya has trained 4000+ students and is passionate about teaching modern web development practices.",
            what_youll_learn="""• Master JavaScript fundamentals: variables, data types, functions, and control structures
• Modern JavaScript: ES6+ features, arrow functions, destructuring, and template literals
• DOM Manipulation: selecting elements, event handling, and dynamic web page creation
• Asynchronous Programming: callbacks, promises, async/await, and AJAX
• Object-Oriented JavaScript: classes, inheritance, and modern OOP patterns
• Node.js Backend Development: server-side JavaScript, Express.js, and API development
• Modern Web APIs: Fetch API, Local Storage, and browser APIs
• Best Practices: code organization, debugging, testing, and professional development""",
            course_content='[{"title": "Module 1: JavaScript Fundamentals", "duration": "6 hours", "description": "Introduction to JavaScript, variables, data types, operators, control structures, functions, and basic programming concepts. Setting up development environment."}, {"title": "Module 2: Modern JavaScript (ES6+)", "duration": "8 hours", "description": "ES6+ features, arrow functions, destructuring, template literals, spread/rest operators, and modern JavaScript syntax. Writing clean and efficient code."}, {"title": "Module 3: DOM Manipulation", "duration": "8 hours", "description": "Document Object Model, selecting elements, event handling, creating dynamic content, and building interactive web pages. Real-world DOM projects."}, {"title": "Module 4: Asynchronous JavaScript", "duration": "6 hours", "description": "Callbacks, promises, async/await, AJAX, Fetch API, and handling asynchronous operations. Building responsive web applications."}, {"title": "Module 5: Object-Oriented JavaScript", "duration": "6 hours", "description": "Classes, inheritance, encapsulation, and modern OOP patterns in JavaScript. Building complex applications with proper structure."}, {"title": "Module 6: Node.js Backend Development", "duration": "8 hours", "description": "Introduction to Node.js, Express.js framework, building RESTful APIs, and server-side JavaScript development. Full-stack application development."}, {"title": "Module 7: Modern Web APIs", "duration": "4 hours", "description": "Local Storage, Session Storage, Geolocation API, and other browser APIs. Building feature-rich web applications."}, {"title": "Module 8: Best Practices and Project Work", "duration": "4 hours", "description": "Code organization, debugging techniques, testing, and building a complete JavaScript project. Professional development practices."}]',
            requirements="Basic computer knowledge and understanding of HTML/CSS (helpful but not required). No prior programming experience required. A modern web browser and code editor (installation guidance provided). Enthusiasm to learn and practice coding regularly.",
            image="javascript.png"
        )
        db.session.add(javascript_course)

        # HTML & CSS Course
        html_css_course = Course(
            id=12,
            title="HTML & CSS Complete Web Development Course",
            subtitle="Master HTML5 and CSS3 with modern web design principles and responsive layouts",
            description="The HTML & CSS Complete Web Development Course is designed for students who want to master web development fundamentals and create beautiful, responsive websites. This comprehensive course covers everything from basic HTML structure to advanced CSS techniques including Flexbox, Grid, animations, and modern web design principles. You'll build real-world projects, learn responsive design, and gain the skills needed for front-end development roles.",
            stream="Web Development",
            price=1500,
            duration="25+ Hours",
            level="Beginner to Intermediate",
            total_lectures=30,
            rating=4.9,
            total_reviews=14000,
            last_updated=datetime.now().date(),
            instructor_name="Meera Iyer",
            instructor_title="Senior Front-End Developer & UI Specialist",
            instructor_bio="Meera Iyer is a senior front-end developer with 8+ years of experience in web design and development. She has worked with major design agencies and tech companies, specializing in responsive design, user experience, and modern CSS techniques. Meera has trained 6000+ students and is passionate about creating beautiful, accessible web experiences.",
            what_youll_learn="""• Master HTML5: semantic markup, forms, multimedia, and accessibility best practices
• Advanced CSS3: selectors, box model, positioning, and modern layout techniques
• Responsive Design: mobile-first approach, media queries, and flexible layouts
• CSS Layout Systems: Flexbox and CSS Grid for modern web layouts
• CSS Animations: transitions, transforms, and keyframe animations
• Web Design Principles: typography, color theory, and visual hierarchy
• Performance Optimization: efficient CSS, image optimization, and best practices
• Modern Tools: CSS preprocessors, build tools, and version control with Git""",
            course_content='[{"title": "Module 1: HTML5 Fundamentals", "duration": "6 hours", "description": "Introduction to HTML5, document structure, semantic elements, text formatting, links, images, and basic forms. Building well-structured web pages."}, {"title": "Module 2: Advanced HTML5", "duration": "4 hours", "description": "HTML5 forms, multimedia elements (audio, video), canvas, and accessibility features. Creating rich, interactive content."}, {"title": "Module 3: CSS3 Fundamentals", "duration": "8 hours", "description": "CSS syntax, selectors, box model, colors, typography, and basic styling. Understanding CSS cascade and specificity."}, {"title": "Module 4: CSS Layout and Positioning", "duration": "6 hours", "description": "Display properties, positioning (static, relative, absolute, fixed), and float layouts. Creating complex page layouts."}, {"title": "Module 5: Flexbox Layout", "duration": "4 hours", "description": "CSS Flexbox properties, flex containers, flex items, and creating flexible, responsive layouts. Modern layout techniques."}, {"title": "Module 6: CSS Grid Layout", "duration": "4 hours", "description": "CSS Grid properties, grid containers, grid items, and creating complex grid-based layouts. Advanced layout systems."}, {"title": "Module 7: Responsive Design", "duration": "6 hours", "description": "Mobile-first design, media queries, responsive images, and creating websites that work on all devices. Modern web development practices."}, {"title": "Module 8: CSS Animations and Advanced Features", "duration": "4 hours", "description": "CSS transitions, transforms, keyframe animations, and advanced CSS features. Creating engaging user experiences."}, {"title": "Module 9: Web Design Principles and Best Practices", "duration": "3 hours", "description": "Typography, color theory, visual hierarchy, accessibility, and performance optimization. Professional web development practices."}]',
            requirements="Basic computer knowledge and familiarity with using a web browser. No prior programming or design experience required. A code editor (installation guidance provided). Enthusiasm to learn and create beautiful websites.",
            image="html-css.png"
        )
        db.session.add(html_css_course)

        # College UI/UX Design Course
        college_uiux_course = Course(
            id=13,
            title="UI/UX Design ",
            subtitle="Master the art of user interface and experience design with comprehensive training",
            description="This comprehensive UI/UX Design course is specifically designed for college students who want to master the art of creating beautiful, functional, and user-centered digital experiences. You'll learn design thinking, user research, prototyping, and visual design principles using industry-standard tools like Figma and Adobe XD. This course prepares you for a successful career in UI/UX design with hands-on projects and real-world applications.",
            stream="UI/UX Design",
            price=25000,
            duration="80+ Hours",
            level="Advanced",
            total_lectures=70,
            rating=4.9,
            total_reviews=500,
            last_updated=datetime.now().date(),
            instructor_name="Senior UI/UX Design Expert",
            instructor_title="Lead Product Designer & Design Systems Specialist",
            instructor_bio="Expert in UI/UX design with 10+ years of experience in creating user-centric digital experiences. Certified in Figma, Adobe XD, and design thinking methodologies. Has worked with top tech companies and startups, specializing in mobile and web application design.",
            what_youll_learn="""• Master Design Fundamentals: Learn color theory, typography, layout principles, and visual hierarchy
• User Research & Personas: Conduct user interviews, create personas, and understand user needs
• Wireframing & Prototyping: Build wireframes, interactive prototypes, and user flows using Figma
• Visual Design & Branding: Create beautiful interfaces with consistent design systems
• Usability Testing: Learn to test designs with real users and iterate based on feedback
• Portfolio Development: Build a professional portfolio showcasing your design projects
• Industry Tools: Master Figma, Adobe XD, and other essential design tools
• Design Thinking: Apply design thinking methodology to solve complex problems""",
            course_content='[{"title": "Module 1: Design Fundamentals & Principles", "duration": "12 hours", "description": "Introduction to UI/UX design, color theory, typography, layout principles, visual hierarchy, and design psychology."}, {"title": "Module 2: User Research & Design Thinking", "duration": "10 hours", "description": "User research methods, creating user personas, empathy mapping, user journey mapping, and design thinking process."}, {"title": "Module 3: Wireframing & Information Architecture", "duration": "15 hours", "description": "Creating wireframes, information architecture, sitemaps, user flows, and low-fidelity prototypes."}, {"title": "Module 4: Visual Design & UI Elements", "duration": "18 hours", "description": "Visual design principles, creating UI components, design systems, style guides, and high-fidelity mockups."}, {"title": "Module 5: Prototyping & Interaction Design", "duration": "12 hours", "description": "Interactive prototyping with Figma, micro-interactions, responsive design, and user testing."}, {"title": "Module 6: Portfolio & Career Preparation", "duration": "13 hours", "description": "Building a professional portfolio, presenting your work, career guidance, and industry best practices."}]',
            requirements="Basic computer skills and creativity. No prior design experience required. A passion for creating user-centered experiences and willingness to learn design tools is essential.",
            image="ui-ux-college.png"
        )
        db.session.add(college_uiux_course)

        # AI/ML Course
        ai_ml_course = Course(
            id=14,
            title="Advanced AI & Machine Learning Course",
            subtitle="Master artificial intelligence, machine learning, and deep learning for cutting-edge tech careers",
            description="The Advanced AI & Machine Learning Course is designed for college students who want to dive deep into the world of artificial intelligence and machine learning. This comprehensive program covers everything from fundamental ML algorithms to advanced deep learning techniques, preparing you for roles in AI engineering, ML research, and data science. You'll work with real-world datasets, build AI models, and gain hands-on experience with industry-standard tools and frameworks.",
            stream="Artificial Intelligence & Machine Learning",
            price=35000,
            duration="100+ Hours",
            level="Advanced",
            total_lectures=80,
            rating=4.8,
            total_reviews=300,
            last_updated=datetime.now().date(),
            instructor_name="Dr. Sarah Chen",
            instructor_title="Senior AI Research Scientist & ML Engineer",
            instructor_bio="Dr. Sarah Chen is a leading expert in artificial intelligence and machine learning with 12+ years of experience in research and industry applications. She holds a Ph.D. in Computer Science with specialization in AI/ML from Stanford University. Dr. Chen has worked with top tech companies including Google AI, Microsoft Research, and OpenAI, contributing to breakthrough projects in natural language processing, computer vision, and reinforcement learning. She has published 50+ research papers and holds 15 patents in AI technologies.",
            what_youll_learn="""• Master Core ML Concepts: Understand supervised, unsupervised, and reinforcement learning algorithms
• Deep Learning Expertise: Build and train neural networks using TensorFlow and PyTorch
• Computer Vision Skills: Implement image recognition, object detection, and computer vision applications
• Natural Language Processing: Develop chatbots, sentiment analysis, and language models
• Real-World Applications: Work on industry-relevant projects like recommendation systems and predictive analytics
• AI Ethics & Responsible AI: Learn about bias detection, fairness, and ethical AI development
• Model Deployment: Deploy ML models to production using cloud platforms and APIs
• Research & Innovation: Stay updated with latest AI trends and contribute to cutting-edge research""",
            course_content='[{"title": "Module 1: Foundations of Machine Learning", "duration": "20 hours", "description": "Introduction to ML concepts, types of learning (supervised, unsupervised, reinforcement), data preprocessing, feature engineering, and model evaluation metrics. Hands-on with scikit-learn and pandas."}, {"title": "Module 2: Supervised Learning Algorithms", "duration": "18 hours", "description": "Linear and logistic regression, decision trees, random forests, support vector machines, and ensemble methods. Practical implementation and hyperparameter tuning."}, {"title": "Module 3: Unsupervised Learning & Clustering", "duration": "12 hours", "description": "K-means clustering, hierarchical clustering, dimensionality reduction (PCA, t-SNE), and anomaly detection techniques."}, {"title": "Module 4: Deep Learning Fundamentals", "duration": "25 hours", "description": "Neural network architecture, backpropagation, activation functions, optimization algorithms, and building neural networks with TensorFlow/Keras."}, {"title": "Module 5: Advanced Deep Learning", "duration": "20 hours", "description": "Convolutional Neural Networks (CNNs) for computer vision, Recurrent Neural Networks (RNNs) and LSTM for sequence data, and transfer learning techniques."}, {"title": "Module 6: Natural Language Processing", "duration": "15 hours", "description": "Text preprocessing, word embeddings, sentiment analysis, named entity recognition, and building chatbots using transformers and BERT."}, {"title": "Module 7: AI Ethics & Model Deployment", "duration": "10 hours", "description": "AI bias detection and mitigation, model interpretability, responsible AI practices, and deploying models using cloud platforms (AWS, Azure, GCP)."}]',
            requirements="Strong foundation in Python programming, basic understanding of linear algebra and calculus, familiarity with statistics and probability. Prior experience with data analysis or programming is recommended. A passion for AI/ML and willingness to work with complex mathematical concepts is essential.",
            image="ai-ml.png"
        )
        db.session.add(ai_ml_course)

        # Cybersecurity College Course
        cybersecurity_college_course = Course(
            id=15,
            title="Cyber Security (Intermediate Level)",
            subtitle="Advanced cybersecurity for college students",
            description="Advanced cybersecurity course specifically designed for college students. This comprehensive program covers network security, ethical hacking, incident response, and prepares you for industry certifications like CEH (Certified Ethical Hacker).",
            stream="Cyber Security",
            price=30000,
            duration="90+ Hours",
            level="Advanced",
            total_lectures=75,
            rating=4.9,
            total_reviews=400,
            last_updated=datetime.now().date(),
            instructor_name="Cyber Security Expert",
            instructor_title="Senior Security Engineer",
            instructor_bio="Expert in cybersecurity with 10+ years of experience in network security, penetration testing, and incident response. Certified in CEH, CISSP, and CompTIA Security+.",
            what_youll_learn="""• Master network security fundamentals and protocols
• Learn ethical hacking techniques and methodologies
• Understand threat modeling and risk assessment
• Develop incident response and forensics skills
• Practice penetration testing on virtual environments
• Prepare for CEH (Certified Ethical Hacker) certification
• Build security tools and scripts using Python
• Implement security controls and monitoring systems""",
            course_content='[{"title": "Module 1: Network Security Fundamentals", "duration": "20 hours", "description": "TCP/IP protocols and security vulnerabilities, network architecture and security design, firewall configuration and management, VPN technologies and implementation."}, {"title": "Module 2: Ethical Hacking", "duration": "25 hours", "description": "Reconnaissance and information gathering, scanning and enumeration techniques, exploitation and post-exploitation, web application security testing."}, {"title": "Module 3: Incident Response & Forensics", "duration": "20 hours", "description": "Digital forensics methodology, evidence collection and preservation, malware analysis and reverse engineering, incident response procedures."}, {"title": "Module 4: Security Tools & Automation", "duration": "15 hours", "description": "Python scripting for security automation, security tool development, SIEM implementation and monitoring, threat hunting techniques."}, {"title": "Module 5: Certification Preparation", "duration": "10 hours", "description": "CEH exam preparation, practice tests and mock exams, interview preparation and career guidance, industry best practices and standards."}]',
            requirements="Basic networking knowledge, familiarity with Linux command line, and understanding of programming concepts. Prior experience with Python is helpful but not required.",
            image="cybersecurity-college.png"
        )
        db.session.add(cybersecurity_college_course)

        # Data Analyst College Course
        data_analyst_college_course = Course(
            id=16,
            title="Data Analyst",
            subtitle="Transform students into proficient data analysts with hands-on training",
            description="This hands-on program is designed to transform students into proficient data analysts. From mastering tools like Excel and Power BI to understanding data cleaning, statistical analysis, and visual storytelling, this course prepares you for a successful career in data analytics. Data analytics is one of the fastest-growing fields across industries. Learn how to transform raw data into actionable insights, make data-driven decisions, and build dashboards that drive business growth.",
            stream="Data Analytics",
            price=20000,
            duration="70+ Hours",
            level="Advanced",
            total_lectures=60,
            rating=4.7,
            total_reviews=600,
            last_updated=datetime.now().date(),
            instructor_name="Data Analytics Expert",
            instructor_title="Senior Data Analyst & Business Intelligence Specialist",
            instructor_bio="Expert in data analytics with 8+ years of experience in Excel, SQL, Power BI, and statistical analysis. Certified in Microsoft Power BI and Tableau, with expertise in transforming raw data into actionable business insights.",
            what_youll_learn="""• Industry-Relevant Skills – Learn Excel, SQL, Power BI, and statistical analysis used by top employers
• Hands-On Training – Practice with real-world data and build a strong project portfolio
• Better Job Opportunities – Get job-ready for roles like Data Analyst, Business Analyst, or MIS Analyst
• Certification Advantage – Earn a recognized certificate that adds value to your resume
• Analytical Mindset – Develop critical thinking and problem-solving abilities to make data-driven decisions
• Future-Focused Growth – Stay relevant in a data-driven world and build a long-term, rewarding career""",
            course_content='[{"title": "Module 1: Introduction to Data Analysis", "duration": "10 hours", "description": "What is data analytics and its role in business, understanding data types and sources, importance of data-driven decision making."}, {"title": "Module 2: Excel for Data Analysis", "duration": "15 hours", "description": "Advanced Excel formulas, charts, and pivot tables, data cleaning and preparation, creating dashboards in Excel."}, {"title": "Module 3: Introduction to SQL", "duration": "12 hours", "description": "Writing queries for extracting and manipulating data, understanding relational databases, joins, aggregations, and data filtering."}, {"title": "Module 4: Data Visualization Tools", "duration": "15 hours", "description": "Introduction to Power BI / Tableau, creating interactive dashboards and reports, best practices for effective data storytelling."}, {"title": "Module 5: Statistical Analysis & Insights", "duration": "10 hours", "description": "Introduction to statistics for data analytics, understanding trends, patterns, and anomalies, making data actionable for business decisions."}, {"title": "Module 6: Final Project & Presentation", "duration": "8 hours", "description": "Build a complete analytics project from scratch, presenting insights and recommendations, preparing a portfolio for interviews and career growth."}]',
            requirements="Basic computer skills and familiarity with Microsoft Office. No prior programming or statistics knowledge required. A passion for working with data and solving business problems is essential.",
            image="data-analyst-college.png"
        )
        db.session.add(data_analyst_college_course)

        # Advanced Web Development Course
        web_dev_college_course = Course(
            id=17,
            title="Advanced Web Development Course",
            subtitle="Master full-stack web development with advanced technologies and deployment strategies",
            description="The Advanced Web Development Course is designed for those who have a basic understanding of coding and want to build dynamic, responsive, and full-stack websites and applications. From advanced JavaScript to backend frameworks and deployment strategies, this program prepares you for roles like Full-Stack Developer, Front-End Specialist, and Software Engineer.",
            stream="Web Development",
            price=45000,
            duration="120+ Hours",
            level="Advanced",
            total_lectures=100,
            rating=4.8,
            total_reviews=250,
            last_updated=datetime.now().date(),
            instructor_name="Senior Full-Stack Development Expert",
            instructor_title="Lead Software Engineer & Full-Stack Specialist",
            instructor_bio="Expert in full-stack web development with 12+ years of experience in React, Node.js, and cloud deployment. Certified in AWS, Azure, and modern web technologies. Has worked with top tech companies and startups, specializing in scalable web applications.",
            what_youll_learn="""• Master In-Demand Skills: Learn advanced front-end and back-end technologies for full-stack roles
• Build Real Projects: Get hands-on experience by creating a fully functional website from scratch
• Better Job Opportunities: Be ready for roles like Full-Stack Developer, Software Developer, or Technical Lead
• Industry-Standard Tools: Get proficient with technologies like React, Node.js, Express, and Docker
• Future-Focused: Learn deployment and scaling methods for long-term growth
• Personalized Guidance: Receive mentorship and support throughout your learning journey""",
            course_content='[{"title": "Module 1: Advanced Front-End Development", "duration": "25 hours", "description": "Advanced JavaScript concepts (ES6+), front-end frameworks (React, Angular, or Vue), state management and advanced component design."}, {"title": "Module 2: Back-End Development & APIs", "duration": "30 hours", "description": "Node.js & Express.js for REST APIs, authentication, security, and user management, database design and connections (MongoDB, SQL)."}, {"title": "Module 3: Advanced Tools & Techniques", "duration": "20 hours", "description": "Version control with Git & GitHub, introduction to GraphQL, WebSockets, and real-time applications, server-side rendering and caching strategies."}, {"title": "Module 4: Deployment & Scalability", "duration": "15 hours", "description": "Deployment pipelines and cloud platforms (AWS, Azure, GCP), containerization with Docker, basics of microservices and load balancers."}, {"title": "Module 5: Modern Development Practices", "duration": "15 hours", "description": "Test-Driven Development (TDD) and debugging, Continuous Integration & Continuous Deployment (CI/CD) pipelines, web performance optimization and best practices."}, {"title": "Module 6: Final Project & Presentation", "duration": "15 hours", "description": "Build a complete, end-to-end web application, present your project and showcase it as a portfolio piece."}]',
            requirements="Basic understanding of HTML, CSS, and JavaScript. Familiarity with programming concepts and willingness to learn advanced technologies. Prior experience with any programming language is helpful but not required.",
            image="web-development.png"
        )
        db.session.add(web_dev_college_course)

        # Data Scientist College Course
        data_scientist_college_course = Course(
            id=18,
            title="Advanced Data Science Course",
            subtitle="Master advanced statistical modeling, machine learning, AI, and deep learning for data science careers",
            description="The Advanced Data Science Course is designed for those with a basic understanding of data analytics or programming and want to advance their careers as skilled Data Scientists. This hands‑on program covers advanced statistical modeling, machine learning, AI, and deep learning, making you job‑ready for roles in data analytics, AI engineering, and more.",
            stream="Data Science",
            price=45000,
            duration="120+ Hours",
            level="Advanced",
            total_lectures=100,
            rating=4.8,
            total_reviews=250,
            last_updated=datetime.now().date(),
            instructor_name="Senior Data Science Expert",
            instructor_title="Lead Data Scientist & AI/ML Specialist",
            instructor_bio="Expert in advanced data science with 15+ years of experience in statistical modeling, machine learning, and deep learning. Certified in TensorFlow, PyTorch, and Apache Spark. Has worked with top tech companies and research institutions, specializing in AI/ML pipelines and big data analytics.",
            what_youll_learn="""• Master Advanced Techniques: Learn deep learning, AI, and big data tools for high‑impact roles
• Industry‑Relevant Skills: Gain proficiency in Python, R, TensorFlow, PyTorch, and Apache Spark
• Real‑World Projects: Build a portfolio of impactful projects for interviews and job applications
• Better Career Opportunities: Prepare for roles like Senior Data Analyst, Data Scientist, AI/ML Specialist, and Business Analyst
• Future‑Focused Expertise: Stay ahead of the curve in an AI‑driven industry
• Personalized Mentorship: Get guidance for your projects, career planning, and interviews""",
            course_content='[{"title": "Module 1: Advanced Statistical Modeling & Probability", "duration": "20 hours", "description": "Statistical inference and hypothesis testing, advanced statistical methods for predictive analytics, probability theory and distributions."}, {"title": "Module 2: Machine Learning Techniques", "duration": "25 hours", "description": "Supervised and unsupervised learning (regression, clustering, classification), model optimization, feature engineering, and model evaluation metrics."}, {"title": "Module 3: Deep Learning & AI", "duration": "30 hours", "description": "Introduction to neural networks, CNN, RNN, and LSTM, introduction to frameworks like TensorFlow and PyTorch, advanced AI concepts."}, {"title": "Module 4: Big Data & Advanced Analytics", "duration": "20 hours", "description": "Handling and analyzing large data sets, introduction to Apache Spark, Hadoop ecosystems, and cloud platforms (AWS, Azure, GCP)."}, {"title": "Module 5: Data Visualization & Storytelling", "duration": "15 hours", "description": "Creating dashboards and visual narratives with Power BI, Tableau, and Plotly, communicating data insights effectively to stakeholders."}, {"title": "Module 6: Capstone Project & Presentation", "duration": "10 hours", "description": "Build and present an end‑to‑end data science solution, showcase proficiency with AI/ML pipelines, deployment, and storytelling."}]',
            requirements="Basic understanding of data analytics or programming concepts. Familiarity with Python and statistics is helpful but not required. A passion for working with data and solving complex problems is essential.",
            image="data-scientist.png"
        )
        db.session.add(data_scientist_college_course)

        # Advanced UI/UX Design Course
        advanced_uiux_course = Course(
            id=19,
            title="Advanced UI/UX Design Course",
            subtitle="Master advanced design methodologies and create seamless user-centric digital experiences",
            description="The Advanced UI/UX Design Course is crafted for those who have a basic understanding of design and want to build expertise in creating seamless, user-centric digital experiences. You'll learn advanced design methodologies, work on complex projects, and gain hands-on experience with industry-leading tools and practices — making you job-ready as a UI/UX Designer or Product Designer.",
            stream="UI/UX Design",
            price=35000,
            duration="80+ Hours",
            level="Advanced",
            total_lectures=65,
            rating=4.9,
            total_reviews=350,
            last_updated=datetime.now().date(),
            instructor_name="Senior UI/UX Design Expert",
            instructor_title="Lead Product Designer & Design Systems Specialist",
            instructor_bio="Expert in UI/UX design with 12+ years of experience in creating user-centric digital experiences. Certified in Figma, Adobe XD, and design thinking methodologies. Has worked with top tech companies and startups.",
            what_youll_learn="""• Master Advanced Tools & Techniques: Build proficiency in Figma, Adobe XD, and prototyping platforms
• Real-World Projects: Learn by doing — work on complex projects that mimic industry demands
• Industry-Relevant Skills: Stay updated with the latest design trends, patterns, and methodologies
• Better Career Opportunities: Build a strong portfolio for roles like UI/UX Designer, Product Designer, and Interaction Designer
• User-Centric Mindset: Develop deep expertise in user behavior, psychology, and design thinking
• Personal Branding Advantage: Learn how to showcase your work, build a strong design portfolio, and stand out to employers""",
            course_content='[{"title": "Module 1: Advanced Design Thinking & User Research", "duration": "15 hours", "description": "Deep dive into user research methods, understanding psychology and behavior in design, advanced user research techniques and methodologies."}, {"title": "Module 2: Information Architecture & User Flows", "duration": "12 hours", "description": "Creating sitemaps, user journeys, and personas for complex products, designing for multi-user platforms and mobile-first approaches."}, {"title": "Module 3: Interaction Design & Prototyping", "duration": "18 hours", "description": "Advanced Figma and Adobe XD techniques, responsive design, micro-interactions, and design systems."}, {"title": "Module 4: UI Patterns & Branding", "duration": "12 hours", "description": "Understanding design trends and branding in UI, creating design guides and component libraries."}, {"title": "Module 5: Usability Testing & Optimization", "duration": "10 hours", "description": "Techniques for testing and validating design ideas, gathering user feedback and iterating for better experience."}, {"title": "Module 6: Final Project & Presentation", "duration": "13 hours", "description": "Build an end-to-end UI/UX project for a live case or portfolio piece, presentation and review to showcase your design thinking and execution skills."}]',
            requirements="Basic understanding of design principles and familiarity with design tools. Prior experience with Figma or Adobe XD is helpful but not required. A passion for creating user-centered experiences is essential.",
            image="advanced-uiux-design.png"
        )
        db.session.add(advanced_uiux_course)

        # Full Stack Development Course (For College Students)
        fullstack_college_course = Course(
            id=20,
            title="FULL STACK DEVELOPMENT COURSE",
            subtitle="Comprehensive hands-on program for college students aspiring to become proficient Full Stack Developers",
            description="A comprehensive, hands‑on program designed for college students aspiring to become proficient Full Stack Developers. This course covers both the Front‑End (HTML, CSS, JavaScript, React) and Back‑End (Node.js, Express, MongoDB) — equipping you with industry‑ready coding, database, and deployment skills for a successful career in web and app development.",
            stream="Full Stack Development",
            price=35000,
            duration="100+ Hours",
            level="Intermediate",
            total_lectures=80,
            rating=4.8,
            total_reviews=300,
            last_updated=datetime.now().date(),
            instructor_name="Senior Full Stack Development Expert",
            instructor_title="Lead Software Engineer & Full Stack Specialist",
            instructor_bio="Expert in full stack development with 10+ years of experience in building end-to-end web applications. Certified in React, Node.js, MongoDB, and modern web technologies. Has worked with top tech companies and startups, specializing in scalable web applications.",
            what_youll_learn="""• Learn to build end‑to‑end websites and web applications
• Gain in‑demand coding, database, and deployment skills
• Build projects that appeal to employers and recruiters
• Get hands‑on experience and a strong portfolio
• Receive a Certificate upon successful completion
• Master both front-end and back-end technologies""",
            course_content='[{"title": "Module 1: Introduction to Full Stack Development", "duration": "10 hours", "description": "Understanding the full stack development ecosystem, setting up development environment, and overview of technologies to be learned."}, {"title": "Module 2: Front‑End Development: HTML5, CSS3, JavaScript, React.js", "duration": "30 hours", "description": "Building responsive user interfaces with HTML5 and CSS3, JavaScript fundamentals, React.js components and state management."}, {"title": "Module 3: Back‑End Development: Node.js, Express.js, REST APIs", "duration": "25 hours", "description": "Server-side development with Node.js, building REST APIs with Express.js, handling HTTP requests and responses."}, {"title": "Module 4: Database Management: MongoDB and SQL", "duration": "15 hours", "description": "Working with MongoDB for NoSQL databases, SQL fundamentals, database design and optimization."}, {"title": "Module 5: Version Control with Git and GitHub", "duration": "10 hours", "description": "Git fundamentals, branching strategies, collaboration workflows, and deploying projects to GitHub."}, {"title": "Module 6: Final Project: Build and Deploy a Complete Web Application", "duration": "10 hours", "description": "End-to-end project development, deployment strategies, and portfolio building for job applications."}]',
            requirements="Basic programming knowledge (HTML/CSS) is ideal, but absolute beginners can also join as it starts from scratch. A passion for web development and willingness to learn new technologies is essential.",
            image="fullstack-college.png"
        )
        db.session.add(fullstack_college_course)

        # Trading Course
        trading_course = Course(
            id=21,
            title="TRADING COURSE",
            subtitle="Master the art of financial markets with advanced trading strategies and risk management",
            description="Master the art of financial markets with our advanced Trading Course. Learn technical analysis, price patterns, risk management, and trading psychology. Build a strong foundation for making informed trading decisions across equity, forex, and crypto markets.",
            stream="Trading & Finance",
            price=25000,
            duration="80+ Hours",
            level="Intermediate",
            total_lectures=60,
            rating=4.7,
            total_reviews=200,
            last_updated=datetime.now().date(),
            instructor_name="Senior Trading Expert",
            instructor_title="Professional Trader & Financial Analyst",
            instructor_bio="Expert in financial markets with 12+ years of experience in equity, forex, and crypto trading. Certified in technical analysis and risk management. Has worked with top financial institutions and helped hundreds of students become successful traders.",
            what_youll_learn="""• Learn in‑demand trading skills for financial independence
• Build the ability to read charts, spot opportunities, and manage risk
• Get hands‑on practice with live market simulations
• Become confident in making trading decisions
• Launch a career as a Trader or Analyst
• Receive personalized guidance and expert support""",
            course_content='[{"title": "Module 1: Introduction to Financial Markets (Stocks, Forex, Crypto)", "duration": "15 hours", "description": "Understanding different financial markets, market structure, and trading instruments across stocks, forex, and cryptocurrency."}, {"title": "Module 2: Technical Analysis, Indicators & Patterns", "duration": "20 hours", "description": "Learning chart patterns, technical indicators, support/resistance levels, and price action analysis."}, {"title": "Module 3: Risk Management & Trading Psychology", "duration": "15 hours", "description": "Position sizing, stop-loss strategies, emotional control, and developing a trader\'s mindset."}, {"title": "Module 4: Trading Strategies & Practice (Swing, Day Trading, Scalping)", "duration": "20 hours", "description": "Different trading timeframes, strategy development, and practical application of trading methods."}, {"title": "Module 5: Live Market Practice & Simulation", "duration": "8 hours", "description": "Hands-on practice with live market data, paper trading, and real-time decision making."}, {"title": "Module 6: Final Project: Build Your Trading Plan", "duration": "2 hours", "description": "Creating a comprehensive trading plan, risk management strategy, and portfolio management approach."}]',
            requirements="Basic understanding of financial concepts and mathematics. No prior trading experience required. A passion for financial markets and willingness to learn risk management is essential.",
            image="trading-course.png"
        )
        db.session.add(trading_course)

        # E-Commerce Course
        ecommerce_course = Course(
            id=22,
            title="E‑COMMERCE COURSE",
            subtitle="Launch your online shop with ease and master digital commerce strategies",
            description="Launch your online shop with ease! This course teaches you how to set up, manage, and grow an e‑commerce business. Learn the essentials — from listing products and pricing strategies to website optimization and digital marketing.",
            stream="E-Commerce & Digital Marketing",
            price=20000,
            duration="60+ Hours",
            level="Beginner",
            total_lectures=45,
            rating=4.8,
            total_reviews=180,
            last_updated=datetime.now().date(),
            instructor_name="E-Commerce Expert",
            instructor_title="Digital Commerce Specialist & Business Consultant",
            instructor_bio="Expert in e-commerce with 8+ years of experience in online business development. Certified in Shopify, WooCommerce, and digital marketing. Has helped hundreds of entrepreneurs launch successful online stores.",
            what_youll_learn="""• Learn how to launch an online business from scratch
• Get hands‑on experience with platforms like Shopify and WooCommerce
• Discover pricing, marketing, and sales strategies for online products
• Build a rewarding career in e‑commerce or launch your own online brand
• Receive personalized guidance and actionable feedback
• Stay relevant in the growing digital commerce space""",
            course_content='[{"title": "Module 1: Introduction to E‑Commerce & Market Trends", "duration": "10 hours", "description": "Understanding e-commerce landscape, market trends, and business opportunities in digital commerce."}, {"title": "Module 2: Store Development (Shopify, WooCommerce)", "duration": "15 hours", "description": "Building online stores using popular platforms, store customization, and user experience optimization."}, {"title": "Module 3: Product Listing & Pricing Strategies", "duration": "12 hours", "description": "Product photography, compelling descriptions, competitive pricing, and inventory management."}, {"title": "Module 4: Payment Gateways & Customer Experience", "duration": "10 hours", "description": "Setting up payment systems, customer service, order fulfillment, and building customer trust."}, {"title": "Module 5: E‑Commerce Marketing: Social Media & Advertising", "duration": "13 hours", "description": "Digital marketing strategies, social media promotion, paid advertising, and customer acquisition."}, {"title": "Module 6: Final Project: Build and Launch Your Own Online Store", "duration": "10 hours", "description": "End-to-end project to create, optimize, and launch a fully functional e-commerce store."}]',
            requirements="Basic computer skills and internet familiarity. No prior e-commerce experience required. A passion for online business and willingness to learn digital tools is essential.",
            image="ecommerce-course.png"
        )
        db.session.add(ecommerce_course)

        # Drop-shipping Course
        dropshipping_course = Course(
            id=23,
            title="DROP‑SHIPPING COURSE",
            subtitle="Master the drop-shipping model and build a successful online business with minimal investment",
            description="Master the drop‑shipping model — one of the best ways to launch an online business with low investment. Learn to source trending products, set up a website, run marketing campaigns, and manage logistics to build a successful drop‑shipping business.",
            stream="E-Commerce & Business",
            price=18000,
            duration="50+ Hours",
            level="Beginner",
            total_lectures=40,
            rating=4.6,
            total_reviews=150,
            last_updated=datetime.now().date(),
            instructor_name="Drop-shipping Expert",
            instructor_title="E-Commerce Entrepreneur & Business Coach",
            instructor_bio="Successful drop-shipping entrepreneur with 6+ years of experience in online business. Expert in product sourcing, supplier management, and digital marketing. Has helped hundreds of students launch profitable drop-shipping businesses.",
            what_youll_learn="""• Learn how to launch an online shop with minimal investment
• Build a fully functional drop‑shipping website from scratch
• Get actionable marketing strategies for online sales
• Understand supplier sourcing and import best practices
• Build a long‑term income stream online
• Receive expert guidance every step of the way""",
            course_content='[{"title": "Module 1: Introduction to Drop‑Shipping & Its Business Model", "duration": "8 hours", "description": "Understanding the drop-shipping business model, advantages, challenges, and market opportunities."}, {"title": "Module 2: Product Selection & Market Research", "duration": "12 hours", "description": "Finding trending products, market research techniques, and identifying profitable niches."}, {"title": "Module 3: Finding Reliable Suppliers & Importing Products", "duration": "10 hours", "description": "Supplier research, communication, quality control, and import logistics management."}, {"title": "Module 4: Creating Your Drop‑Shipping Store (Tools & Platforms)", "duration": "12 hours", "description": "Building online stores, store optimization, and creating compelling product pages."}, {"title": "Module 5: Marketing Techniques for Drop‑Shipping (Ads & Social Media)", "duration": "8 hours", "description": "Digital marketing strategies, paid advertising, social media promotion, and customer acquisition."}, {"title": "Module 6: Final Project: Launch Your Own Drop‑Shipping Business", "duration": "10 hours", "description": "Complete project to launch a fully functional drop-shipping business with real products."}]',
            requirements="Basic computer skills and internet familiarity. No prior business experience required. A passion for entrepreneurship and willingness to learn online business is essential.",
            image="dropshipping-course.png"
        )
        db.session.add(dropshipping_course)

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
            Statistics(name="Students Trained", value=1000, icon="👥"),  # 1000+ students
            Statistics(name="Colleges Supported", value=50, icon="🏫"),  # 50+ colleges
            Statistics(name="MOE Signed", value=10, icon="🤝"),  # 10+ MOE
            Statistics(name="Google Rating", value=48, icon="⭐"),  # 4.8 rating
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

        # Create Testimonials based on One Percentage
        testimonials = [
            Testimonial(
                student_name="Anitha",
                feedback="One Percentage transformed my career completely. The hands-on training and real-world projects helped me land my dream job at a top tech company.",
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
                feedback="One Percentage's approach to learning is unique. They focus on creating leaders, not just employees. This mindset has helped me excel in my career.",
                rating=5,
                image_url="mohankumar.jpg"
            ),
            # Data Analyst Course Specific Testimonials
            Testimonial(
                student_name="Priya S.",
                feedback="This course gave me the confidence to start my career as a data analyst. The hands-on practice and projects were exactly what I needed!",
                rating=5,
                image_url="priya.jpg",
                position="B.Sc Computer Science Student",
                company=""
            ),
            Testimonial(
                student_name="Arjun R.",
                feedback="I learned to clean, analyze, and visualize data like a pro. The trainers made complex concepts simple and easy to understand!",
                rating=5,
                image_url="arjun.jpg",
                position="Aspiring Business Analyst",
                company=""
            ),
            Testimonial(
                student_name="Sneha K.",
                feedback="Excellent teaching and support! The Excel and Power BI lessons really boosted my analytical and presentation skills for my first job.",
                rating=5,
                image_url="sneha.jpg",
                position="Commerce Graduate",
                company=""
            ),
            Testimonial(
                student_name="Rahul V.",
                feedback="The trainers gave personal attention and guidance throughout the course. I landed an internship right after finishing the program!",
                rating=5,
                image_url="rahul.jpg",
                position="Final-Year Engineering Student",
                company=""
            ),
            Testimonial(
                student_name="Nisha M.",
                feedback="Perfect for anyone looking to switch careers. The practical exercises and real-world examples made learning enjoyable and relevant!",
                rating=5,
                image_url="nisha.jpg",
                position="Career Switcher (HR to Data Analyst)",
                company=""
            ),
            Testimonial(
                student_name="Karthik A.",
                feedback="Highly recommend this program for students and working professionals. It gave me the tools and mindset I needed for a successful career in analytics.",
                rating=5,
                image_url="karthik.jpg",
                position="Junior Data Analyst",
                company=""
            ),
            # Advanced UI/UX Design Course Specific Testimonials
            Testimonial(
                student_name="Aarthi S.",
                feedback="This advanced course taught me how to think like a designer and build beautiful, functional interfaces. It boosted my confidence and my portfolio!",
                rating=5,
                image_url="aarthi.jpg",
                position="Aspiring Product Designer",
                company=""
            ),
            Testimonial(
                student_name="Raghav K.",
                feedback="The focus on real-world projects and advanced techniques gave me the edge I needed to land a job in UX design!",
                rating=5,
                image_url="raghav.jpg",
                position="Final-Year Student",
                company=""
            ),
            Testimonial(
                student_name="Sneha R.",
                feedback="I came in with basic design knowledge and left with advanced skills and a strong portfolio. This program made all the difference!",
                rating=5,
                image_url="sneha_r.jpg",
                position="Junior UX/UI Designer",
                company=""
            ),
            Testimonial(
                student_name="Karthik P.",
                feedback="Learning advanced design thinking and interaction design here was a game-changer for me. I now approach design problems creatively and strategically.",
                rating=5,
                image_url="karthik_p.jpg",
                position="Web Developer and Aspiring UX Designer",
                company=""
            ),
            Testimonial(
                student_name="Priya N.",
                feedback="The trainers were highly supportive and explained complex ideas clearly. This course gave me the tools and mindset I needed for a successful design career.",
                rating=5,
                image_url="priya_n.jpg",
                position="Graphic Designer Transitioning to UI/UX",
                company=""
            ),
            Testimonial(
                student_name="Arvind K.",
                feedback="With hands-on practice and feedback, I felt job-ready by the end. The advanced techniques and tools learned here are in high demand in the design industry.",
                rating=5,
                image_url="arvind.jpg",
                position="Final-Year Engineering Student",
                company=""
            ),
            # Advanced Web Development Course Specific Testimonials
            Testimonial(
                student_name="Rahul K.",
                feedback="The advanced concepts and real-world projects boosted my coding skills and gave me the confidence to apply for developer roles!",
                rating=5,
                image_url="rahul_k.jpg",
                position="Final-Year Computer Science Student",
                company=""
            ),
            Testimonial(
                student_name="Priya S.",
                feedback="Learning React, Node.js, and deployment strategies gave me the edge I needed to land my first full-stack developer job.",
                rating=5,
                image_url="priya_s.jpg",
                position="Junior Developer",
                company=""
            ),
            Testimonial(
                student_name="Arjun R.",
                feedback="The hands-on training was excellent! I can now build and deploy end-to-end applications thanks to this advanced course.",
                rating=5,
                image_url="arjun_r.jpg",
                position="Aspiring Software Engineer",
                company=""
            ),
            Testimonial(
                student_name="Sneha M.",
                feedback="The trainers were supportive and explained advanced concepts clearly. The capstone project was a game-changer for my portfolio!",
                rating=5,
                image_url="sneha_m.jpg",
                position="Recent Graduate",
                company=""
            ),
            Testimonial(
                student_name="Karthik S.",
                feedback="The advanced tools and best practices taught in this program gave me a solid foundation for a successful career in web development.",
                rating=5,
                image_url="karthik_s.jpg",
                position="Aspiring Tech Entrepreneur",
                company=""
            ),
            Testimonial(
                student_name="Ananya G.",
                feedback="Learning from scratch to advanced deployment has been an amazing experience. This course made me job-ready and confident!",
                rating=5,
                image_url="ananya.jpg",
                position="Career Switcher",
                company=""
            ),
            # Advanced Data Science Course Specific Testimonials
            Testimonial(
                student_name="Rahul S.",
                feedback="This course helped me move from basic analytics to advanced data science. The hands‑on projects made learning enjoyable and practical!",
                rating=5,
                image_url="rahul_s.jpg",
                position="Aspiring Data Scientist",
                company=""
            ),
            Testimonial(
                student_name="Priya R.",
                feedback="Learning deep learning and big data analytics opened new career doors for me. The trainers were excellent and always available for help!",
                rating=5,
                image_url="priya_r.jpg",
                position="Junior Data Analyst",
                company=""
            ),
            Testimonial(
                student_name="Karthik M.",
                feedback="The focus on practical projects and advanced techniques gave me the edge I needed to land a role as a data scientist!",
                rating=5,
                image_url="karthik_m.jpg",
                position="Final‑Year Student",
                company=""
            ),
            Testimonial(
                student_name="Ananya G.",
                feedback="The trainers made complex concepts like neural networks and deep learning easy to understand. Highly recommend for anyone looking to specialize in data science!",
                rating=5,
                image_url="ananya_g.jpg",
                position="Aspiring AI/ML Specialist",
                company=""
            ),
            Testimonial(
                student_name="Sneha K.",
                feedback="From statistics to deep learning, this course covers it all! The capstone project gave me hands‑on experience to impress potential employers.",
                rating=5,
                image_url="sneha_k.jpg",
                position="Recent Graduate",
                company=""
            ),
            Testimonial(
                student_name="Arvind K.",
                feedback="Excellent training for advanced data science. The trainers and mentors gave personalized guidance every step of the way!",
                rating=5,
                image_url="arvind_k.jpg",
                position="Career Switcher",
                company=""
            ),
            # Full Stack Development Course Specific Testimonials
            Testimonial(
                student_name="Varun R.",
                feedback="This Full Stack Development program taught me to build complete websites — from design to deployment!",
                rating=5,
                image_url="varun_r.jpg",
                position="College Student",
                company=""
            ),
            Testimonial(
                student_name="Meera K.",
                feedback="I gained hands‑on experience with Node.js and React — making me job‑ready!",
                rating=5,
                image_url="meera_k.jpg",
                position="Final-Year Student",
                company=""
            ),
            Testimonial(
                student_name="Arjun S.",
                feedback="Best program for college students aiming for a career in Web Development!",
                rating=5,
                image_url="arjun_s.jpg",
                position="Aspiring Developer",
                company=""
            ),
            Testimonial(
                student_name="Sneha R.",
                feedback="Helped me understand both front‑end and back‑end — making coding exciting and fun!",
                rating=5,
                image_url="sneha_r.jpg",
                position="Computer Science Student",
                company=""
            ),
            Testimonial(
                student_name="Rishi P.",
                feedback="Now I can build, launch, and maintain websites — thanks to this training!",
                rating=5,
                image_url="rishi_p.jpg",
                position="Recent Graduate",
                company=""
            ),
            # Trading Course Specific Testimonials
            Testimonial(
                student_name="Arvind K.",
                feedback="Excellent trainers! This course gave me the knowledge and confidence I needed to start trading successfully.",
                rating=5,
                image_url="arvind_trading.jpg",
                position="Aspiring Trader",
                company=""
            ),
            Testimonial(
                student_name="Sneha M.",
                feedback="The risk management and live exercises were the best part. Highly recommend for aspiring traders!",
                rating=5,
                image_url="sneha_trading.jpg",
                position="Finance Student",
                company=""
            ),
            Testimonial(
                student_name="Rajesh G.",
                feedback="Learning advanced trading strategies changed the way I approach the market. Worth every rupee!",
                rating=5,
                image_url="rajesh_trading.jpg",
                position="Working Professional",
                company=""
            ),
            Testimonial(
                student_name="Ananya G.",
                feedback="The trainers made trading simple to understand. I started seeing results within a few weeks of practice!",
                rating=5,
                image_url="ananya_trading.jpg",
                position="College Student",
                company=""
            ),
            # E-Commerce Course Specific Testimonials
            Testimonial(
                student_name="Priya R.",
                feedback="Learning to build and launch my online shop was a game‑changer. Now I run my e‑commerce site successfully!",
                rating=5,
                image_url="priya_ecommerce.jpg",
                position="Entrepreneur",
                company=""
            ),
            Testimonial(
                student_name="Rajesh G.",
                feedback="The trainers gave practical tips for setting pricing and promoting products online. Very valuable program!",
                rating=5,
                image_url="rajesh_ecommerce.jpg",
                position="Business Owner",
                company=""
            ),
            Testimonial(
                student_name="Ananya G.",
                feedback="Excellent learning experience. The hands‑on exercises gave me the confidence to launch my online business.",
                rating=5,
                image_url="ananya_ecommerce.jpg",
                position="Recent Graduate",
                company=""
            ),
            Testimonial(
                student_name="Karthik S.",
                feedback="This course made e‑commerce simple and actionable. Highly recommend for entrepreneurs and students!",
                rating=5,
                image_url="karthik_ecommerce.jpg",
                position="Aspiring Entrepreneur",
                company=""
            ),
            # Drop-shipping Course Specific Testimonials
            Testimonial(
                student_name="Ananya G.",
                feedback="The drop‑shipping lessons taught me how to launch a website and make sales quickly. Very practical training!",
                rating=5,
                image_url="ananya_dropshipping.jpg",
                position="Online Entrepreneur",
                company=""
            ),
            Testimonial(
                student_name="Karthik S.",
                feedback="Excellent trainers and helpful exercises. This gave me the confidence and knowledge to start my drop‑shipping business.",
                rating=5,
                image_url="karthik_dropshipping.jpg",
                position="Business Student",
                company=""
            ),
            Testimonial(
                student_name="Arvind K.",
                feedback="Learning this business model was a game‑changer for me. The trainers explained everything clearly, making it easy to implement.",
                rating=5,
                image_url="arvind_dropshipping.jpg",
                position="Aspiring Business Owner",
                company=""
            ),
            Testimonial(
                student_name="Sneha M.",
                feedback="Highly recommend for entrepreneurs starting online! This course gave me all the tools I needed for drop‑shipping success.",
                rating=5,
                image_url="sneha_dropshipping.jpg",
                position="Digital Entrepreneur",
                company=""
            ),
            # Advanced AI & Machine Learning Course Specific Testimonials
            Testimonial(
                student_name="Rahul K.",
                feedback="This AI/ML course transformed my understanding of artificial intelligence. The hands-on projects with TensorFlow and PyTorch gave me the confidence to pursue a career in AI engineering.",
                rating=5,
                image_url="rahul_ai.jpg",
                position="AI Engineering Student",
                company=""
            ),
            Testimonial(
                student_name="Priya S.",
                feedback="Dr. Chen's expertise in AI is incredible! I learned to build neural networks, implement computer vision, and develop NLP applications. This course opened doors to exciting AI opportunities.",
                rating=5,
                image_url="priya_ai.jpg",
                position="ML Research Assistant",
                company=""
            ),
            Testimonial(
                student_name="Arjun M.",
                feedback="The deep learning modules were game-changing. I can now build and deploy ML models to production. The focus on AI ethics and responsible development was particularly valuable.",
                rating=5,
                image_url="arjun_ai.jpg",
                position="Computer Science Graduate",
                company=""
            ),
            Testimonial(
                student_name="Sneha R.",
                feedback="From basic ML concepts to advanced neural networks, this course covered everything. The real-world projects helped me build a strong portfolio for AI/ML roles.",
                rating=5,
                image_url="sneha_ai.jpg",
                position="Aspiring Data Scientist",
                company=""
            ),
            Testimonial(
                student_name="Karthik V.",
                feedback="The course structure is excellent - starting with fundamentals and progressing to cutting-edge AI techniques. I'm now confident in my ability to contribute to AI research and development.",
                rating=5,
                image_url="karthik_ai.jpg",
                position="AI Research Student",
                company=""
            ),
            Testimonial(
                student_name="Ananya G.",
                feedback="Learning about AI ethics and responsible AI development was eye-opening. This course not only taught me technical skills but also the importance of building AI systems that benefit society.",
                rating=5,
                image_url="ananya_ai.jpg",
                position="Computer Vision Enthusiast",
                company=""
            ),
            # Python Programming Course Specific Testimonials
            Testimonial(
                student_name="Vikram S.",
                feedback="Rajesh sir's Python course is amazing! I went from knowing nothing about programming to building web applications and data analysis projects. The hands-on approach made learning so much easier.",
                rating=5,
                image_url="vikram_python.jpg",
                position="Computer Science Student",
                company=""
            ),
            Testimonial(
                student_name="Priya M.",
                feedback="The Python course structure is perfect - starting with basics and progressing to advanced topics. I learned Flask, pandas, and even machine learning basics. Highly recommend for beginners!",
                rating=5,
                image_url="priya_python.jpg",
                position="Aspiring Developer",
                company=""
            ),
            Testimonial(
                student_name="Arjun K.",
                feedback="Rajesh sir explains complex concepts in simple terms. The projects were practical and helped me build a strong portfolio. I'm now confident in my Python skills!",
                rating=5,
                image_url="arjun_python.jpg",
                position="Engineering Student",
                company=""
            ),
            # Java Programming Course Specific Testimonials
            Testimonial(
                student_name="Sneha R.",
                feedback="Priya ma'am's Java course is comprehensive and well-structured. I learned OOP concepts, Spring Framework, and even built a complete web application. Perfect for enterprise development!",
                rating=5,
                image_url="sneha_java.jpg",
                position="Software Engineering Student",
                company=""
            ),
            Testimonial(
                student_name="Karthik P.",
                feedback="The Java course covers everything from basics to advanced topics like multithreading and Spring Boot. The real-world projects helped me understand enterprise development practices.",
                rating=5,
                image_url="karthik_java.jpg",
                position="Aspiring Java Developer",
                company=""
            ),
            Testimonial(
                student_name="Meera S.",
                feedback="Learning Java with Priya ma'am was a great experience. The course prepared me well for technical interviews and I'm now working as a Java developer!",
                rating=5,
                image_url="meera_java.jpg",
                position="Junior Java Developer",
                company=""
            ),
            # C++ Programming Course Specific Testimonials
            Testimonial(
                student_name="Rahul V.",
                feedback="Amit sir's C++ course is excellent! I learned memory management, STL, and modern C++ features. The focus on system programming and algorithms was very helpful for my career.",
                rating=5,
                image_url="rahul_cpp.jpg",
                position="Computer Science Graduate",
                company=""
            ),
            Testimonial(
                student_name="Ananya K.",
                feedback="The C++ course helped me understand low-level programming concepts. Learning about pointers, memory management, and performance optimization was eye-opening.",
                rating=5,
                image_url="ananya_cpp.jpg",
                position="System Programming Student",
                company=""
            ),
            Testimonial(
                student_name="Vikram M.",
                feedback="Amit sir explains complex C++ concepts clearly. The course covers everything from basics to advanced topics like templates and modern C++ features. Highly recommend!",
                rating=5,
                image_url="vikram_cpp.jpg",
                position="Aspiring C++ Developer",
                company=""
            ),
            # JavaScript Programming Course Specific Testimonials
            Testimonial(
                student_name="Kavya S.",
                feedback="Kavya ma'am's JavaScript course is fantastic! I learned modern JavaScript, DOM manipulation, and even Node.js backend development. Now I can build full-stack applications!",
                rating=5,
                image_url="kavya_js.jpg",
                position="Full-Stack Developer",
                company=""
            ),
            Testimonial(
                student_name="Arjun R.",
                feedback="The JavaScript course covers everything from ES6+ features to async programming and Node.js. The projects were practical and helped me build a strong portfolio.",
                rating=5,
                image_url="arjun_js.jpg",
                position="Web Development Student",
                company=""
            ),
            Testimonial(
                student_name="Priya K.",
                feedback="Learning JavaScript with Kavya ma'am was a great experience. The course structure is perfect for beginners and the hands-on projects made learning fun and engaging.",
                rating=5,
                image_url="priya_js.jpg",
                position="Front-End Developer",
                company=""
            ),
            # HTML & CSS Course Specific Testimonials
            Testimonial(
                student_name="Meera I.",
                feedback="Meera ma'am's HTML & CSS course is excellent! I learned responsive design, Flexbox, CSS Grid, and modern web design principles. Now I can create beautiful websites!",
                rating=5,
                image_url="meera_html.jpg",
                position="Web Designer",
                company=""
            ),
            Testimonial(
                student_name="Rahul S.",
                feedback="The HTML & CSS course is perfect for beginners. I learned semantic HTML, modern CSS techniques, and responsive design. The projects helped me build a strong foundation.",
                rating=5,
                image_url="rahul_html.jpg",
                position="UI/UX Student",
                company=""
            ),
            Testimonial(
                student_name="Ananya P.",
                feedback="Learning HTML & CSS with Meera ma'am was amazing! The course covers everything from basics to advanced topics like animations and CSS Grid. Highly recommend!",
                rating=5,
                image_url="ananya_html.jpg",
                position="Front-End Enthusiast",
                company=""
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
            ),
            # Data Analyst Course Specific FAQs
            FAQ(
                question="What tools will I learn in this Data Analyst course?",
                answer="You will learn Excel for data analysis, SQL for database queries, Power BI/Tableau for data visualization, and statistical analysis techniques.",
                course_id=16
            ),
            FAQ(
                question="Do I need prior experience with Excel or programming?",
                answer="Basic computer skills and familiarity with Microsoft Office are sufficient. No prior programming or statistics knowledge is required.",
                course_id=16
            ),
            FAQ(
                question="What kind of projects will I work on?",
                answer="You'll work on real-world data analysis projects including business dashboards, sales analysis, customer insights, and a comprehensive final project for your portfolio.",
                course_id=16
            ),
            FAQ(
                question="What career opportunities will this course open up?",
                answer="This course prepares you for roles like Data Analyst, Business Analyst, MIS Analyst, Market Research Analyst, and other data-driven positions across industries.",
                course_id=16
            ),
            FAQ(
                question="Will I get hands-on practice with real data?",
                answer="Yes! You'll work with real business datasets, practice data cleaning, create visualizations, and build interactive dashboards throughout the course.",
                course_id=16
            ),
            FAQ(
                question="Is this course suitable for career switchers?",
                answer="Absolutely! This course is designed for both students and working professionals looking to transition into data analytics. The curriculum starts from fundamentals and builds up to advanced concepts.",
                course_id=16
            ),
            # Advanced UI/UX Design Course Specific FAQs
            FAQ(
                question="What design tools will I learn in this Advanced UI/UX course?",
                answer="You will master Figma, Adobe XD, prototyping platforms, and learn advanced design system creation and component library development.",
                course_id=19
            ),
            FAQ(
                question="Do I need prior design experience to enroll?",
                answer="Basic understanding of design principles and familiarity with design tools is recommended. Prior experience with Figma or Adobe XD is helpful but not required.",
                course_id=19
            ),
            FAQ(
                question="What kind of projects will I work on?",
                answer="You'll work on complex, real-world projects including mobile apps, web applications, design systems, and end-to-end UI/UX projects that you can showcase in your portfolio.",
                course_id=19
            ),
            FAQ(
                question="Will I learn about user research and testing?",
                answer="Yes! The course covers advanced user research methods, usability testing techniques, and how to gather and implement user feedback to improve your designs.",
                course_id=19
            ),
            FAQ(
                question="What career opportunities will this advanced course open up?",
                answer="This course prepares you for senior roles like UI/UX Designer, Product Designer, Interaction Designer, Design Systems Specialist, and UX Researcher.",
                course_id=19
            ),
            FAQ(
                question="Will I build a professional portfolio?",
                answer="Absolutely! You'll create a comprehensive portfolio showcasing your design thinking, user research, and final projects that will help you stand out to employers.",
                course_id=19
            ),
            # Advanced Web Development Course Specific FAQs
            FAQ(
                question="What technologies will I learn in this Advanced Web Development course?",
                answer="You will master React, Node.js, Express.js, MongoDB, SQL, Git, Docker, AWS/Azure deployment, and modern development practices like CI/CD.",
                course_id=17
            ),
            FAQ(
                question="Do I need prior programming experience to enroll?",
                answer="Basic understanding of HTML, CSS, and JavaScript is required. Familiarity with programming concepts and willingness to learn advanced technologies is essential.",
                course_id=17
            ),
            FAQ(
                question="What kind of projects will I build?",
                answer="You'll build complete, end-to-end web applications including full-stack projects, REST APIs, real-time applications, and deploy them to cloud platforms.",
                course_id=17
            ),
            FAQ(
                question="Will I learn about deployment and cloud platforms?",
                answer="Yes! You'll learn deployment strategies, containerization with Docker, cloud platforms (AWS, Azure, GCP), and CI/CD pipelines for professional development.",
                course_id=17
            ),
            FAQ(
                question="What career opportunities will this advanced course open up?",
                answer="This course prepares you for roles like Full-Stack Developer, Software Developer, Technical Lead, Front-End Specialist, and Back-End Developer.",
                course_id=17
            ),
            FAQ(
                question="Will I get hands-on experience with modern development tools?",
                answer="Absolutely! You'll work with Git, GitHub, Docker, cloud platforms, and learn industry-standard development practices and workflows.",
                course_id=17
            ),
            # Advanced Data Science Course Specific FAQs
            FAQ(
                question="What advanced technologies will I learn in this Data Science course?",
                answer="You will master Python, R, TensorFlow, PyTorch, Apache Spark, statistical modeling, machine learning, deep learning, and big data analytics.",
                course_id=18
            ),
            FAQ(
                question="Do I need prior experience with data analytics or programming?",
                answer="Basic understanding of data analytics or programming concepts is recommended. Familiarity with Python and statistics is helpful but not required.",
                course_id=18
            ),
            FAQ(
                question="What kind of projects will I work on?",
                answer="You'll work on advanced projects including statistical modeling, machine learning pipelines, deep learning applications, big data analysis, and a comprehensive capstone project.",
                course_id=18
            ),
            FAQ(
                question="Will I learn about deep learning and AI?",
                answer="Yes! The course covers neural networks, CNN, RNN, LSTM, TensorFlow, PyTorch, and advanced AI concepts for real-world applications.",
                course_id=18
            ),
            FAQ(
                question="What career opportunities will this advanced course open up?",
                answer="This course prepares you for roles like Senior Data Analyst, Data Scientist, AI/ML Specialist, Business Analyst, and Research Scientist.",
                course_id=18
            ),
            FAQ(
                question="Will I get hands-on experience with big data tools?",
                answer="Absolutely! You'll work with Apache Spark, Hadoop ecosystems, cloud platforms (AWS, Azure, GCP), and learn to handle large-scale data analysis.",
                course_id=18
            ),
            # Full Stack Development Course Specific FAQs
            FAQ(
                question="What is this course about?",
                answer="This is an intermediate‑level Full Stack Development program focusing on both front‑end and back‑end technologies like HTML, CSS, JavaScript, React.js, Node.js, and MongoDB.",
                course_id=20
            ),
            FAQ(
                question="Do I need any prior coding experience?",
                answer="It's ideal for students with basic programming knowledge (HTML/CSS), but absolute beginners can also join as it starts from scratch.",
                course_id=20
            ),
            FAQ(
                question="What will I be able to do after this course?",
                answer="Build and deploy end‑to‑end websites, work with databases, APIs, and create fully functional applications.",
                course_id=20
            ),
            FAQ(
                question="Will I get a certificate?",
                answer="Yes! Upon successful completion, you'll receive a Certificate from One Percentage Edu‑Tech.",
                course_id=20
            ),
            FAQ(
                question="Will this help for future careers?",
                answer="Definitely! Full Stack Development is highly in demand, opening doors to careers as a Software Developer, Web Developer, or App Developer.",
                course_id=20
            ),
            # Trading Course Specific FAQs
            FAQ(
                question="What markets will I learn to trade?",
                answer="You will learn to trade across equity (stocks), forex (currency pairs), and cryptocurrency markets with comprehensive strategies for each.",
                course_id=21
            ),
            FAQ(
                question="Do I need prior trading experience?",
                answer="No prior trading experience required. The course starts from basics and progresses to advanced strategies suitable for beginners and intermediate learners.",
                course_id=21
            ),
            FAQ(
                question="Will I get hands-on practice?",
                answer="Yes! You'll practice with live market simulations, paper trading, and real-time decision making to build confidence before trading with real money.",
                course_id=21
            ),
            FAQ(
                question="What career opportunities will this open up?",
                answer="This course prepares you for careers as a Professional Trader, Financial Analyst, Portfolio Manager, or to trade independently for financial freedom.",
                course_id=21
            ),
            FAQ(
                question="Is risk management covered?",
                answer="Absolutely! Risk management and trading psychology are core components of the course, teaching you to protect your capital and manage emotions.",
                course_id=21
            ),
            # E-Commerce Course Specific FAQs
            FAQ(
                question="What platforms will I learn?",
                answer="You will learn to build stores on popular platforms like Shopify, WooCommerce, and other e-commerce tools used by successful online businesses.",
                course_id=22
            ),
            FAQ(
                question="Do I need technical skills?",
                answer="Basic computer skills and internet familiarity are sufficient. No prior technical or business experience required.",
                course_id=22
            ),
            FAQ(
                question="Will I learn digital marketing?",
                answer="Yes! The course covers social media marketing, paid advertising, SEO, and other digital marketing strategies essential for e-commerce success.",
                course_id=22
            ),
            FAQ(
                question="Can I launch my own business after this?",
                answer="Absolutely! You'll build and launch your own e-commerce store as a final project, giving you a real business to start with.",
                course_id=22
            ),
            FAQ(
                question="What support will I receive?",
                answer="You'll receive personalized guidance, actionable feedback, and ongoing support to help you succeed in your e-commerce journey.",
                course_id=22
            ),
            # Drop-shipping Course Specific FAQs
            FAQ(
                question="What is drop-shipping and why learn it?",
                answer="Drop-shipping is a business model where you sell products without holding inventory. It's perfect for starting an online business with minimal investment.",
                course_id=23
            ),
            FAQ(
                question="Do I need money to start?",
                answer="Drop-shipping requires minimal investment compared to traditional businesses. You'll learn to start with very low capital requirements.",
                course_id=23
            ),
            FAQ(
                question="Will I learn to find suppliers?",
                answer="Yes! You'll learn supplier research, communication, quality control, and how to build relationships with reliable suppliers.",
                course_id=23
            ),
            FAQ(
                question="What marketing strategies will I learn?",
                answer="You'll learn digital marketing, paid advertising, social media promotion, and customer acquisition strategies specifically for drop-shipping.",
                course_id=23
            ),
            FAQ(
                question="Can I start earning immediately?",
                answer="While results vary, you'll have all the tools and knowledge to launch your drop-shipping business and start making sales quickly.",
                course_id=23
            ),
            # Advanced AI & Machine Learning Course Specific FAQs
            FAQ(
                question="What AI and ML technologies will I learn in this course?",
                answer="You will master Python, TensorFlow, PyTorch, scikit-learn, pandas, NumPy, and learn to build neural networks, implement computer vision, and develop NLP applications.",
                course_id=14
            ),
            FAQ(
                question="Do I need prior experience with AI or machine learning?",
                answer="Strong foundation in Python programming and basic understanding of linear algebra and calculus is required. Prior experience with data analysis or programming is recommended.",
                course_id=14
            ),
            FAQ(
                question="What kind of projects will I work on?",
                answer="You'll build real-world AI projects including image recognition systems, chatbots, recommendation engines, predictive models, and deploy ML models to production environments.",
                course_id=14
            ),
            FAQ(
                question="Will I learn about deep learning and neural networks?",
                answer="Yes! The course covers neural network architecture, backpropagation, CNNs for computer vision, RNNs and LSTM for sequence data, and transfer learning techniques.",
                course_id=14
            ),
            FAQ(
                question="What career opportunities will this advanced course open up?",
                answer="This course prepares you for roles like AI Engineer, ML Engineer, Data Scientist, Research Scientist, Computer Vision Engineer, and NLP Specialist.",
                course_id=14
            ),
            FAQ(
                question="Will I learn about AI ethics and responsible AI development?",
                answer="Absolutely! The course covers AI bias detection and mitigation, model interpretability, responsible AI practices, and ethical considerations in AI development.",
                course_id=14
            ),
            FAQ(
                question="Will I get hands-on experience with cloud platforms?",
                answer="Yes! You'll learn to deploy ML models using cloud platforms like AWS, Azure, and GCP, and work with production-ready AI infrastructure.",
                course_id=14
            ),
            FAQ(
                question="Is this course suitable for research and innovation?",
                answer="Yes! The course covers cutting-edge AI techniques and prepares you to contribute to AI research, stay updated with latest trends, and work on innovative AI projects.",
                course_id=14
            ),
            # Python Programming Course Specific FAQs
            FAQ(
                question="What will I learn in this Python course?",
                answer="You will master Python fundamentals, object-oriented programming, web development with Flask, data analysis with pandas, and database integration. The course covers everything from basics to advanced topics.",
                course_id=8
            ),
            FAQ(
                question="Do I need prior programming experience?",
                answer="No prior programming experience required. The course starts from absolute basics and progresses to advanced concepts. Basic computer knowledge and logical thinking are sufficient.",
                course_id=8
            ),
            FAQ(
                question="What kind of projects will I build?",
                answer="You'll build web applications, data analysis projects, automation scripts, and real-world applications using Python. Each module includes hands-on projects to reinforce learning.",
                course_id=8
            ),
            FAQ(
                question="Will I learn web development with Python?",
                answer="Yes! You'll learn Flask framework, build web applications, work with databases, and create RESTful APIs. The course covers both frontend and backend development.",
                course_id=8
            ),
            FAQ(
                question="What career opportunities will this course open up?",
                answer="This course prepares you for roles like Python Developer, Web Developer, Data Analyst, Automation Engineer, and Software Developer.",
                course_id=8
            ),
            # Java Programming Course Specific FAQs
            FAQ(
                question="What will I learn in this Java course?",
                answer="You will master Java fundamentals, object-oriented programming, advanced Java concepts, multithreading, database connectivity, web development, and Spring Framework.",
                course_id=9
            ),
            FAQ(
                question="Do I need prior programming experience?",
                answer="No prior programming experience required. The course starts from basics and progresses to enterprise-level development. Basic computer knowledge is sufficient.",
                course_id=9
            ),
            FAQ(
                question="Will I learn Spring Framework?",
                answer="Yes! You'll learn Spring Core, dependency injection, Spring Boot, and build RESTful APIs. The course covers modern Java development practices.",
                course_id=9
            ),
            FAQ(
                question="What kind of projects will I build?",
                answer="You'll build web applications, enterprise applications, database-driven applications, and RESTful APIs. Each module includes practical projects.",
                course_id=9
            ),
            FAQ(
                question="What career opportunities will this course open up?",
                answer="This course prepares you for roles like Java Developer, Software Engineer, Backend Developer, Enterprise Developer, and Spring Developer.",
                course_id=9
            ),
            # C++ Programming Course Specific FAQs
            FAQ(
                question="What will I learn in this C++ course?",
                answer="You will master C++ fundamentals, object-oriented programming, memory management, advanced C++ features, STL, modern C++ features, and algorithm design.",
                course_id=10
            ),
            FAQ(
                question="Do I need prior programming experience?",
                answer="No prior programming experience required. The course starts from basics and progresses to advanced system programming concepts. Basic computer knowledge is sufficient.",
                course_id=10
            ),
            FAQ(
                question="Will I learn about memory management?",
                answer="Yes! You'll learn pointers, references, dynamic memory allocation, smart pointers, and memory leak prevention. Memory management is a core focus of the course.",
                course_id=10
            ),
            FAQ(
                question="What kind of projects will I build?",
                answer="You'll build system applications, algorithm implementations, data structure projects, and performance-optimized applications. Each module includes hands-on projects.",
                course_id=10
            ),
            FAQ(
                question="What career opportunities will this course open up?",
                answer="This course prepares you for roles like C++ Developer, System Programmer, Game Developer, Embedded Systems Developer, and Performance Engineer.",
                course_id=10
            ),
            # JavaScript Programming Course Specific FAQs
            FAQ(
                question="What will I learn in this JavaScript course?",
                answer="You will master JavaScript fundamentals, modern ES6+ features, DOM manipulation, asynchronous programming, object-oriented JavaScript, and Node.js backend development.",
                course_id=11
            ),
            FAQ(
                question="Do I need prior programming experience?",
                answer="No prior programming experience required. Basic understanding of HTML/CSS is helpful but not required. The course starts from absolute basics.",
                course_id=11
            ),
            FAQ(
                question="Will I learn Node.js backend development?",
                answer="Yes! You'll learn Node.js, Express.js framework, build RESTful APIs, and develop server-side JavaScript applications. Full-stack development is covered.",
                course_id=11
            ),
            FAQ(
                question="What kind of projects will I build?",
                answer="You'll build interactive web applications, dynamic websites, RESTful APIs, and full-stack applications. Each module includes practical projects.",
                course_id=11
            ),
            FAQ(
                question="What career opportunities will this course open up?",
                answer="This course prepares you for roles like JavaScript Developer, Frontend Developer, Full-Stack Developer, Node.js Developer, and Web Developer.",
                course_id=11
            ),
            # HTML & CSS Course Specific FAQs
            FAQ(
                question="What will I learn in this HTML & CSS course?",
                answer="You will master HTML5 semantic markup, advanced CSS3 techniques, responsive design, Flexbox, CSS Grid, animations, and modern web design principles.",
                course_id=12
            ),
            FAQ(
                question="Do I need prior programming or design experience?",
                answer="No prior programming or design experience required. Basic computer knowledge and familiarity with web browsers is sufficient. The course starts from absolute basics.",
                course_id=12
            ),
            FAQ(
                question="Will I learn responsive design?",
                answer="Yes! You'll learn mobile-first design, media queries, responsive images, and create websites that work perfectly on all devices and screen sizes.",
                course_id=12
            ),
            FAQ(
                question="What kind of projects will I build?",
                answer="You'll build responsive websites, modern layouts using Flexbox and CSS Grid, animated web pages, and professional-looking web designs. Each module includes hands-on projects.",
                course_id=12
            ),
            FAQ(
                question="What career opportunities will this course open up?",
                answer="This course prepares you for roles like Frontend Developer, Web Designer, UI Developer, HTML/CSS Specialist, and Web Development roles.",
                course_id=12
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
        print("Database seeded successfully with exact One Percentage content!")

if __name__ == "__main__":
    seed_database() 