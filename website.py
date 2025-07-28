#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
اسکریپت ساخت وب‌سایت معرفی شخصی مدرن با پایتون و Flask

محتویات:
1. وب سرور با Flask
2. قالب HTML5 مدرن با Bootstrap 5
3. بخش‌های مختلف شامل: درباره من، مهارت‌ها، نمونه کارها، تماس با من
4. پشتیبانی از ریسپانسیو (واکنش‌گرا)
5. امکان شخصی‌سازی آسان

نیازمندی‌ها:
- Python 3.6+
- Flask
"""

from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

# تنظیمات وب‌سایت
SITE_CONFIG = {
    "title": "وب‌سایت شخصی من",
    "author": "نام شما",
    "description": "این وب‌سایت شخصی من است که مهارت‌ها و نمونه کارهایم را نمایش می‌دهد.",
    "keywords": "وب‌سایت شخصی, نمونه کار, مهارت‌ها, رزومه",
    "theme_color": "#3498db",
    "year": datetime.now().year
}

# اطلاعات شخصی
ABOUT_ME = {
    "name": "نام شما",
    "title": "عنوان شغلی شما",
    "about": "این بخشی درباره شما و سوابق کاری‌تان است. می‌توانید در چند خط خودتان را معرفی کنید.",
    "image": "static/images/profile.jpg"  # مسیر تصویر پروفایل
}

# مهارت‌ها
SKILLS = [
    {"name": "پایتون", "level": 90},
    {"name": "Flask", "level": 85},
    {"name": "HTML/CSS", "level": 80},
    {"name": "JavaScript", "level": 70},
    {"name": "پایگاه داده", "level": 75},
    {"name": "Git", "level": 65}
]

# نمونه کارها
PORTFOLIO = [
    {
        "title": "پروژه اول",
        "description": "توضیح کوتاهی درباره پروژه اول",
        "image": "static/images/project1.jpg",
        "tags": ["پایتون", "Flask"],
        "link": "#"
    },
    {
        "title": "پروژه دوم",
        "description": "توضیح کوتاهی درباره پروژه دوم",
        "image": "static/images/project2.jpg",
        "tags": ["HTML", "CSS"],
        "link": "#"
    },
    {
        "title": "پروژه سوم",
        "description": "توضیح کوتاهی درباره پروژه سوم",
        "image": "static/images/project3.jpg",
        "tags": ["JavaScript"],
        "link": "#"
    }
]

# اطلاعات تماس
CONTACT_INFO = {
    "email": "email@example.com",
    "phone": "+98 912 345 6789",
    "address": "آدرس شما",
    "social_media": [
        {"name": "LinkedIn", "icon": "fab fa-linkedin", "link": "#"},
        {"name": "GitHub", "icon": "fab fa-github", "link": "#"},
        {"name": "Twitter", "icon": "fab fa-twitter", "link": "#"},
        {"name": "Instagram", "icon": "fab fa-instagram", "link": "#"}
    ]
}

@app.route('/')
def home():
    return render_template(
        'index.html',
        config=SITE_CONFIG,
        about=ABOUT_ME,
        skills=SKILLS,
        portfolio=PORTFOLIO,
        contact=CONTACT_INFO
    )

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # در اینجا می‌توانید ایمیل را ارسال کنید یا در دیتابیس ذخیره کنید
        print(f"پیام جدید از: {name} <{email}>\nمتن پیام: {message}")
        
        return redirect(url_for('home'))

# ساخت پوشه‌های مورد نیاز
def create_folders():
    folders = ['static/images', 'static/css', 'static/js', 'templates']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

# ساخت فایل‌های اولیه
def create_files():
    # ساخت فایل index.html
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ config.title }}</title>
    <meta name="description" content="{{ config.description }}">
    <meta name="keywords" content="{{ config.keywords }}">
    <meta name="author" content="{{ config.author }}">
    
    <!-- Bootstrap 5 RTL -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.rtl.min.css" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- سبک‌های سفارشی -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    
    <style>
        :root {
            --primary-color: {{ config.theme_color }};
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        }
        
        .hero-section {
            background: linear-gradient(135deg, var(--primary-color), #2c3e50);
            color: white;
            padding: 100px 0;
        }
        
        .profile-img {
            width: 200px;
            height: 200px;
            object-fit: cover;
            border: 5px solid white;
        }
        
        .skill-bar {
            height: 20px;
            background-color: #e9ecef;
            border-radius: 5px;
            margin-bottom: 15px;
        }
        
        .skill-level {
            height: 100%;
            border-radius: 5px;
            background-color: var(--primary-color);
        }
        
        .portfolio-item {
            margin-bottom: 30px;
            transition: transform 0.3s;
        }
        
        .portfolio-item:hover {
            transform: translateY(-5px);
        }
        
        .tag {
            display: inline-block;
            background-color: var(--primary-color);
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            margin-right: 5px;
        }
    </style>
</head>
<body>
    <!-- نوار ناوبری -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
        <div class="container">
            <a class="navbar-brand" href="#">{{ config.title }}</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#about">درباره من</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#skills">مهارت‌ها</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#portfolio">نمونه کارها</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#contact">تماس با من</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- بخش هیرو -->
    <section class="hero-section text-center">
        <div class="container">
            <img src="{{ url_for('static', filename=about.image) }}" alt="{{ about.name }}" class="profile-img rounded-circle mb-4">
            <h1>{{ about.name }}</h1>
            <p class="lead">{{ about.title }}</p>
        </div>
    </section>

    <!-- درباره من -->
    <section id="about" class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center mb-5">درباره من</h2>
            <div class="row">
                <div class="col-lg-8 mx-auto text-center">
                    <p>{{ about.about }}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- مهارت‌ها -->
    <section id="skills" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">مهارت‌های من</h2>
            <div class="row">
                {% for skill in skills %}
                <div class="col-md-6 mb-4">
                    <div class="d-flex justify-content-between">
                        <h5>{{ skill.name }}</h5>
                        <span>{{ skill.level }}%</span>
                    </div>
                    <div class="skill-bar">
                        <div class="skill-level" style="width: {{ skill.level }}%"></div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- نمونه کارها -->
    <section id="portfolio" class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center mb-5">نمونه کارهای من</h2>
            <div class="row">
                {% for item in portfolio %}
                <div class="col-md-4 portfolio-item">
                    <div class="card h-100">
                        <img src="{{ url_for('static', filename=item.image) }}" class="card-img-top" alt="{{ item.title }}">
                        <div class="card-body">
                            <h5 class="card-title">{{ item.title }}</h5>
                            <p class="card-text">{{ item.description }}</p>
                            <div class="mb-3">
                                {% for tag in item.tags %}
                                <span class="tag">{{ tag }}</span>
                                {% endfor %}
                            </div>
                            <a href="{{ item.link }}" class="btn btn-primary">مشاهده جزئیات</a>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- تماس با من -->
    <section id="contact" class="py-5">
        <div class="container">
            <h2 class="text-center mb-5">تماس با من</h2>
            <div class="row">
                <div class="col-lg-6 mb-4">
                    <h4>اطلاعات تماس</h4>
                    <ul class="list-unstyled">
                        <li class="mb-2"><i class="fas fa-envelope me-2"></i> {{ contact.email }}</li>
                        <li class="mb-2"><i class="fas fa-phone me-2"></i> {{ contact.phone }}</li>
                        <li class="mb-2"><i class="fas fa-map-marker-alt me-2"></i> {{ contact.address }}</li>
                    </ul>
                    
                    <h4 class="mt-4">شبکه‌های اجتماعی</h4>
                    <div class="social-icons">
                        {% for social in contact.social_media %}
                        <a href="{{ social.link }}" class="text-decoration-none me-3" target="_blank">
                            <i class="{{ social.icon }} fa-2x"></i>
                        </a>
                        {% endfor %}
                    </div>
                </div>
                
                <div class="col-lg-6">
                    <form action="{{ url_for('contact') }}" method="POST">
                        <div class="mb-3">
                            <label for="name" class="form-label">نام شما</label>
                            <input type="text" class="form-control" id="name" name="name" required>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">ایمیل</label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        <div class="mb-3">
                            <label for="message" class="form-label">پیام</label>
                            <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary">ارسال پیام</button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- پاورقی -->
    <footer class="bg-dark text-white py-4">
        <div class="container text-center">
            <p>&copy; {{ config.year }} {{ config.title }}. تمامی حقوق محفوظ است.</p>
        </div>
    </footer>

    <!-- اسکریپت‌ها -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
''')

    # ساخت فایل style.css
    with open('static/css/style.css', 'w', encoding='utf-8') as f:
        f.write('''
/* سبک‌های سفارشی */

body {
    padding-top: 56px;
}

section {
    padding: 60px 0;
}

.social-icons a {
    color: var(--primary-color);
    transition: color 0.3s;
}

.social-icons a:hover {
    color: #2c3e50;
}

/* انیمیشن‌ها */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.fade-in {
    animation: fadeIn 1s ease-in;
}
''')

    # ساخت فایل main.js
    with open('static/js/main.js', 'w', encoding='utf-8') as f:
        f.write('''
// اسکریپت‌های جاوااسکریپت سفارشی

document.addEventListener('DOMContentLoaded', function() {
    // انیمیشن اسکرول
    const sections = document.querySelectorAll('section');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, { threshold: 0.1 });
    
    sections.forEach(section => {
        observer.observe(section);
    });
    
    // اسموت اسکرول برای لینک‌های منو
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });
});
''')

if __name__ == '__main__':
    create_folders()
    create_files()
    
    # اگر تصاویر پیش‌فرض وجود ندارند، می‌توانید تصاویر نمونه را دانلود کنید
    print("در حال راه‌اندازی وب‌سایت...")
    print(f"وب‌سایت در حال اجرا است. لطفا به آدرس http://localhost:5000 مراجعه کنید.")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
