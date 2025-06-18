// Enhanced Counter Animation for Cybernaut Design
document.addEventListener('DOMContentLoaded', function() {
    // Counter animation function
    function animateCounters() {
        const counters = document.querySelectorAll('.stat-number');
        
        counters.forEach(counter => {
            const target = parseFloat(counter.getAttribute('data-count'));
            const increment = target / 200;
            let current = 0;
            
            const updateCounter = () => {
                if (current < target) {
                    current += increment;
                    counter.textContent = Math.ceil(current);
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.textContent = target;
                }
            };
            
            updateCounter();
        });
    }

    // Intersection Observer for triggering animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    // Observe statistics sections
    const statisticsSections = document.querySelectorAll('.statistics, .hero-stats');
    statisticsSections.forEach(section => {
        observer.observe(section);
    });
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offsetTop = target.offsetTop - 80; // Account for fixed navbar
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.getElementById('mainNav');
    if (navbar) {
        if (window.scrollY > 50) {
            navbar.classList.add('shadow');
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.98)';
        } else {
            navbar.classList.remove('shadow');
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
        }
    }
});

// Form validation and submission
const enrollmentForm = document.getElementById('enrollmentForm');
if (enrollmentForm) {
    enrollmentForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Show loading state
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerText;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
        submitBtn.disabled = true;

        // Simulate form submission (replace with actual API call)
        setTimeout(() => {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
            
            // Show success message
            const modal = document.getElementById('enrollmentModal');
            if (modal) {
                const modalInstance = bootstrap.Modal.getInstance(modal);
                modalInstance.hide();
            }

            // Show success toast
            showToast('Enrollment successful! Please join the WhatsApp group.', 'success');
        }, 2000);
    });
}

// Toast notification function
function showToast(message, type = 'info') {
    const toastContainer = document.getElementById('toastContainer') || createToastContainer();
    
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    
    toastContainer.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    // Remove toast after it's hidden
    toast.addEventListener('hidden.bs.toast', () => {
        toast.remove();
    });
}

// Create toast container if it doesn't exist
function createToastContainer() {
    const container = document.createElement('div');
    container.id = 'toastContainer';
    container.className = 'toast-container position-fixed top-0 end-0 p-3';
    container.style.zIndex = '9999';
    document.body.appendChild(container);
    return container;
}

// Initialize tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

// Course filter functionality
document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('#courseTabs .nav-link');
    const courseCards = document.querySelectorAll('.course-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.getAttribute('data-filter');

            courseCards.forEach(card => {
                if (filter === 'all' || card.getAttribute('data-category') === filter) {
                    card.style.display = 'block';
                    card.classList.add('fade-in-up');
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});

// Mobile menu toggle with enhanced functionality
const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

if (navbarToggler && navbarCollapse) {
    navbarToggler.addEventListener('click', function() {
        this.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        });
    });
}

// Scroll to top button
window.addEventListener('scroll', function() {
    const scrollToTop = document.querySelector('.scroll-to-top');
    if (scrollToTop) {
        if (window.pageYOffset > 100) {
            scrollToTop.classList.add('show');
        } else {
            scrollToTop.classList.remove('show');
        }
    }
});

// Handle course enrollment with enhanced UX
function handleEnrollment(courseId) {
    const enrollBtn = document.querySelector(`[data-course-id="${courseId}"]`);
    if (enrollBtn) {
        const originalText = enrollBtn.innerText;
        enrollBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
        enrollBtn.disabled = true;

        // Simulate API call (replace with actual implementation)
        setTimeout(() => {
            enrollBtn.innerHTML = originalText;
            enrollBtn.disabled = false;
            
            showToast('Course enrollment successful!', 'success');
        }, 1500);
    }
}

// Image lazy loading with enhanced performance
document.addEventListener('DOMContentLoaded', function() {
    const lazyImages = document.querySelectorAll('img[loading="lazy"]');
    
    if ('loading' in HTMLImageElement.prototype) {
        lazyImages.forEach(img => {
            if (img.dataset.src) {
                img.src = img.dataset.src;
            }
        });
    } else {
        // Fallback for browsers that don't support lazy loading
        const lazyImageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.classList.add('fade-in-up');
                    }
                    observer.unobserve(img);
                }
            });
        });

        lazyImages.forEach(function(img) {
            lazyImageObserver.observe(img);
        });
    }
});

// Add scroll-triggered animations
document.addEventListener('DOMContentLoaded', function() {
    const animatedElements = document.querySelectorAll('.service-card, .program-category, .team-card, .course-card');
    
    const animationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                animationObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    animatedElements.forEach(element => {
        animationObserver.observe(element);
    });
});

// Enhanced mobile responsiveness
function handleResize() {
    const isMobile = window.innerWidth <= 768;
    const navbar = document.getElementById('mainNav');
    
    if (navbar) {
        if (isMobile) {
            navbar.classList.add('mobile-nav');
        } else {
            navbar.classList.remove('mobile-nav');
        }
    }
}

window.addEventListener('resize', handleResize);
handleResize(); // Initial call

// Add scroll progress indicator
window.addEventListener('scroll', function() {
    const scrollProgress = document.getElementById('scrollProgress');
    if (scrollProgress) {
        const scrollTop = window.pageYOffset;
        const docHeight = document.body.offsetHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;
        scrollProgress.style.width = scrollPercent + '%';
    }
});

// Initialize scroll progress bar if it doesn't exist
document.addEventListener('DOMContentLoaded', function() {
    if (!document.getElementById('scrollProgress')) {
        const progressBar = document.createElement('div');
        progressBar.id = 'scrollProgress';
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 3px;
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
            z-index: 9999;
            transition: width 0.1s ease;
        `;
        document.body.appendChild(progressBar);
    }
});

// Contact form handling
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');
    const submitBtn = document.getElementById('submitBtn');
    const submitText = document.getElementById('submitText');
    const submitSpinner = document.getElementById('submitSpinner');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Show loading state
            submitBtn.disabled = true;
            submitText.textContent = 'Sending...';
            submitSpinner.style.display = 'inline-block';
            
            // Hide any existing messages
            if (successMessage) successMessage.style.display = 'none';
            if (errorMessage) errorMessage.style.display = 'none';
            
            // Get form data
            const formData = new FormData(contactForm);
            
            // Submit form
            fetch(contactForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => {
                if (response.ok) {
                    // Show success message
                    if (successMessage) {
                        successMessage.style.display = 'block';
                        successMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                    
                    // Reset form
                    contactForm.reset();
                    
                    // Show toast notification
                    showToast('Message sent successfully! We\'ll get back to you soon.', 'success');
                } else {
                    throw new Error('Network response was not ok');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                
                // Show error message
                if (errorMessage) {
                    errorMessage.style.display = 'block';
                    errorMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
                
                // Show toast notification
                showToast('Error sending message. Please try again.', 'error');
            })
            .finally(() => {
                // Reset button state
                submitBtn.disabled = false;
                submitText.textContent = 'Send Message';
                submitSpinner.style.display = 'none';
            });
        });
    }
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            if (alert.style.display !== 'none') {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, 5000);
    });
});

// Counter animation and pop effect for hero stats
function animateCounter(el, target, suffix = '', duration = 1200) {
    let start = 0;
    let startTime = null;
    function animate(ts) {
        if (!startTime) startTime = ts;
        const progress = Math.min((ts - startTime) / duration, 1);
        const value = Math.floor(progress * target);
        el.textContent = value + suffix;
        if (progress < 1) {
            requestAnimationFrame(animate);
        } else {
            el.textContent = target + suffix;
        }
    }
    requestAnimationFrame(animate);
}

document.addEventListener('DOMContentLoaded', function() {
    // Animate stats on load
    const statStudents = document.getElementById('stat-students');
    const statMentors = document.getElementById('stat-mentors');
    const statSuccess = document.getElementById('stat-success');
    if (statStudents) animateCounter(statStudents, 5000, '+');
    if (statMentors) animateCounter(statMentors, 50, '+');
    if (statSuccess) animateCounter(statSuccess, 95, '%');

    // Pop effect on click/touch
    document.querySelectorAll('.stat-counter').forEach(function(el) {
        el.addEventListener('click', function() {
            el.style.transform = 'scale(1.18)';
            setTimeout(() => { el.style.transform = 'scale(1)'; }, 180);
        });
        el.addEventListener('touchstart', function() {
            el.style.transform = 'scale(1.18)';
            setTimeout(() => { el.style.transform = 'scale(1)'; }, 180);
        });
    });

    // Smooth scroll for hero buttons
    document.querySelectorAll('.hero-scroll').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            const href = btn.getAttribute('href');
            if (href && href.startsWith('#')) {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    window.scrollTo({
                        top: target.offsetTop - 70,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}); 