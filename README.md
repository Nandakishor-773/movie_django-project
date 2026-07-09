# 🎬 Movie Management Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.0%2B-green?style=for-the-badge&logo=django)
![API](https://img.shields.io/badge/API-REST-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen?style=for-the-badge)

**Modern Movie Discovery & Management Platform with Advanced Search & Recommendations**

[Features](#features) • [Architecture](#system-architecture) • [Installation](#installation) • [API](#api-reference) • [Contributing](#contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Installation Guide](#installation)
- [API Reference](#api-reference)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Performance Optimization](#performance-optimization)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

A sophisticated **Movie Management & Discovery Platform** built with Django and Django REST Framework. This production-ready application demonstrates advanced web development practices including API-first architecture, caching strategies, and scalable design patterns.

**Perfect for:**
- 🎬 Movie enthusiasts & collectors
- 🎥 Entertainment platforms
- 📊 Content management systems
- 🔍 Search & discovery platforms

---

## ✨ Features

### **Movie Catalog Management**
- 🎬 Comprehensive movie database with metadata
- 🎭 Multi-genre classification system
- 🌟 Director & cast information
- 📅 Release date & availability tracking
- 🎯 Movie categorization & tagging
- 📸 Poster & multimedia support

### **Advanced Search & Discovery**
- 🔍 Full-text search functionality
- 🎭 Genre-based filtering
- 📅 Year range filtering
- ⭐ Rating-based sorting
- 👥 Actor & director search
- 💡 Autocomplete suggestions
- 📊 Search analytics & trending

### **Intelligent Rating System**
- ⭐ 5-star rating scale
- 📝 Detailed movie reviews
- 👥 User ratings aggregation
- 🔝 Top-rated movies ranking
- 📊 Rating distribution analysis
- 🎯 Personalized recommendations

### **User Engagement**
- 👤 User profiles with watchlists
- 💾 Save favorite movies
- 📋 Personal movie collections
- 🔔 New release notifications
- 📊 Viewing history
- 👥 Social features (follow, share)

### **Recommendation Engine**
- 🤖 AI-powered suggestions
- 🎯 Content-based filtering
- 👥 Collaborative filtering
- 📊 Trend analysis
- 🔥 Popular movies ranking
- 📈 Personalized recommendations

### **Admin Dashboard**
- 📊 Movie analytics
- 📈 User statistics
- 📋 Content management
- 🔐 Moderation tools
- 📉 Performance metrics
- 🎯 System health monitoring

### **API-First Design**
- 🔌 RESTful API endpoints
- 📱 Mobile app ready
- 🔐 Token authentication
- ⚡ Efficient pagination
- 🔄 Real-time updates
- 📚 Comprehensive documentation

---

## 🛠️ Technology Stack

### **Backend**
| Component | Technology |
|-----------|-----------|
| **Framework** | Django 4.0+ |
| **Language** | Python 3.8+ |
| **API** | Django REST Framework 3.13+ |
| **Authentication** | Token-based (DRF) |
| **ORM** | Django ORM |

### **Database**
| Component | Technology |
|-----------|-----------|
| **Primary DB** | PostgreSQL 12+ / MySQL 8+ |
| **Development DB** | SQLite 3 |
| **Caching** | Django Cache Framework, Redis (optional) |
| **Search** | Full-text search via database |

### **Frontend**
| Component | Technology |
|-----------|-----------|
| **Markup** | HTML5 |
| **Styling** | CSS3, Bootstrap 5 |
| **Interactivity** | JavaScript ES6+, AJAX |
| **UI Components** | Bootstrap components |

### **DevOps & Tools**
| Component | Technology |
|-----------|-----------|
| **Version Control** | Git, GitHub |
| **Package Manager** | pip, requirements.txt |
| **Virtual Environment** | Python venv |
| **Web Server** | Gunicorn (production) |
| **Reverse Proxy** | Nginx (production) |
| **Containerization** | Docker (optional) |

---

## 🏗️ System Architecture

### **Architecture Overview**
```
┌─────────────────────────────────────────────────────┐
│              Frontend Layer                         │
│  (Web Browser: HTML5, CSS3, Bootstrap, JavaScript)  │
└────────────────────┬────────────────────────────────┘
                     │ HTTP/REST API
┌────────────────────▼────────────────────────────────┐
│          Django REST API Layer                      │
│  ┌──────────────────────────────────────────────┐  │
│  │  URL Routing → ViewSets → Serializers       │  │
│  └──────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────┐  │
│  │  Authentication → Permissions → Throttling   │  │
│  └──────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────┘
                     │ Query
┌────────────────────▼────────────────────────────────┐
│          Business Logic Layer                       │
│  (Serializers, Services, Permissions)               │
└────────────────────┬────────────────────────────────┘
                     │ ORM Query
┌────────────────────▼────────────────────────────────┐
│          Data Access Layer (Django ORM)             │
│  (Models, Querysets, Managers)                      │
└────────────────────┬────────────────────────────────┘
                     │ SQL
┌────────────────────▼────────────────────────────────┐
│          Database Layer                             │
│  (PostgreSQL - ACID Transactions, Indexing)         │
└─────────────────────────────────────────────────────┘
```

### **Design Patterns Used**
- **ViewSets & Routers** - DRF patterns for RESTful APIs
- **Serializers** - Data validation & transformation
- **Permissions & Authentication** - Security layer
- **Manager & QuerySets** - Custom database queries
- **Mixins** - Code reusability
- **Middleware** - Request/response processing

---

## 🚀 Installation

### **Prerequisites**
```bash
# System Requirements
- Python 3.8+
- pip (Python Package Manager)
- virtualenv or venv
- Git
- PostgreSQL or MySQL (optional for production)
```

### **Step 1: Clone Repository**
```bash
git clone https://github.com/Nandakishor-773/movie_django-project.git
cd movie_django-project
```

### **Step 2: Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### **Step 3: Install Dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### **Step 4: Environment Setup**
```bash
# Create .env file
cp .env.example .env

# Configure your settings:
# SECRET_KEY, DEBUG, DATABASE_URL, etc.
```

### **Step 5: Database Configuration**
```bash
# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser
```

### **Step 6: Load Sample Data** (Optional)
```bash
# Load initial movie data
python manage.py loaddata movies_initial_data.json
```

### **Step 7: Run Development Server**
```bash
python manage.py runserver
# Access: http://localhost:8000
# API: http://localhost:8000/api/v1/
# Admin: http://localhost:8000/admin/
```

---

## 📡 API Reference

### **Base URL**
```
http://localhost:8000/api/v1/
```

### **Authentication**
```
Header: Authorization: Token <your-auth-token>
```

### **Movie Endpoints**

#### List All Movies
```http
GET /movies/?page=1&page_size=20&ordering=-rating

Query Parameters:
  - page: Page number (default: 1)
  - page_size: Results per page (default: 20)
  - search: Search by title/description
  - genre: Filter by genre
  - year: Filter by year
  - min_rating: Minimum rating (0-5)
  - ordering: Sort field (-rating, title, etc.)

Response: 200 OK
{
  "count": 1000,
  "next": "http://localhost:8000/api/v1/movies/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Inception",
      "description": "A skilled thief...",
      "genre": "Sci-Fi, Thriller",
      "release_date": "2010-07-16",
      "director": "Christopher Nolan",
      "cast": ["Leonardo DiCaprio", "Ellen Page"],
      "rating": 4.8,
      "poster_url": "http://...",
      "url": "http://localhost:8000/api/v1/movies/1/"
    }
  ]
}
```

#### Get Movie Details
```http
GET /movies/{id}/

Response: 200 OK
{
  "id": 1,
  "title": "Inception",
  "description": "...",
  "genre": ["Sci-Fi", "Thriller"],
  "release_date": "2010-07-16",
  "director": "Christopher Nolan",
  "cast": ["Leonardo DiCaprio", "Ellen Page"],
  "rating": 4.8,
  "total_reviews": 1250,
  "poster_url": "...",
  "runtime": 148,
  "language": "English",
  "reviews": [
    {
      "id": 1,
      "user": "john_doe",
      "rating": 5,
      "review": "Amazing movie!",
      "created_at": "2026-07-01T10:30:00Z"
    }
  ]
}
```

#### Search Movies
```http
GET /movies/search/?q=inception&genre=sci-fi

Response: 200 OK
[
  {
    "id": 1,
    "title": "Inception",
    "rating": 4.8
  }
]
```

### **Rating Endpoints**

#### Rate a Movie
```http
POST /movies/{id}/rate/
Content-Type: application/json
Authorization: Token <token>

{
  "rating": 5,
  "review": "Outstanding movie!"
}

Response: 201 Created
{
  "id": 1,
  "user": "john_doe",
  "movie": 1,
  "rating": 5,
  "review": "Outstanding movie!",
  "created_at": "2026-07-09T12:00:00Z"
}
```

#### Get Movie Ratings
```http
GET /movies/{id}/ratings/

Response: 200 OK
{
  "average_rating": 4.8,
  "total_ratings": 1250,
  "rating_distribution": {
    "5": 750,
    "4": 300,
    "3": 150,
    "2": 40,
    "1": 10
  }
}
```

### **Watchlist Endpoints**

#### Get User Watchlist
```http
GET /users/watchlist/
Authorization: Token <token>

Response: 200 OK
{
  "count": 5,
  "results": [
    {
      "id": 1,
      "movie_id": 1,
      "title": "Inception",
      "added_at": "2026-07-01T10:00:00Z"
    }
  ]
}
```

#### Add to Watchlist
```http
POST /users/watchlist/
Authorization: Token <token>

{
  "movie_id": 1
}

Response: 201 Created
```

#### Remove from Watchlist
```http
DELETE /users/watchlist/{id}/
Authorization: Token <token>

Response: 204 No Content
```

### **Recommendation Endpoints**

#### Get Recommendations
```http
GET /movies/recommendations/?user_id=1

Response: 200 OK
[
  {
    "id": 2,
    "title": "The Matrix",
    "rating": 4.7,
    "reason": "Similar to movies you've rated highly"
  }
]
```

#### Get Trending Movies
```http
GET /movies/trending/?period=week

Response: 200 OK
[
  {
    "id": 1,
    "title": "Inception",
    "trending_score": 98.5
  }
]
```

---

## 🗄️ Database Schema

### **Core Models**

#### **Movie Model**
```python
class Movie(models.Model):
    - id (AutoField, Primary Key)
    - title (CharField, max_length=255)
    - description (TextField)
    - genre (JSONField or M2M relationship)
    - release_date (DateField)
    - director (CharField)
    - cast (JSONField or M2M relationship)
    - runtime (IntegerField, in minutes)
    - language (CharField)
    - poster_url (URLField, nullable)
    - rating (FloatField, default=0)
    - created_at (DateTimeField, auto_now_add)
    - updated_at (DateTimeField, auto_now)
```

#### **Rating/Review Model**
```python
class Review(models.Model):
    - id (AutoField, Primary Key)
    - movie (ForeignKey: Movie)
    - user (ForeignKey: User)
    - rating (IntegerField, 1-5 stars)
    - review_text (TextField)
    - helpful_count (IntegerField)
    - created_at (DateTimeField, auto_now_add)
    - updated_at (DateTimeField, auto_now)
```

#### **Watchlist Model**
```python
class Watchlist(models.Model):
    - id (AutoField, Primary Key)
    - user (ForeignKey: User)
    - movie (ForeignKey: Movie)
    - added_at (DateTimeField, auto_now_add)
    - status (CharField: watching/completed/dropped)
```

#### **User Model** (Extended)
```python
class UserProfile(models.Model):
    - user (OneToOneField: User)
    - bio (TextField, nullable)
    - favorite_genres (JSONField)
    - watchlist_count (IntegerField)
    - review_count (IntegerField)
    - created_at (DateTimeField, auto_now_add)
```

---

## 📁 Project Structure

```
movie_django-project/
│
├── manage.py                       # Django management script
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment template
├── .gitignore
├── README.md
│
├── config/                         # Project configuration
│   ├── __init__.py
│   ├── settings.py                 # Main settings
│   ├── urls.py                     # URL routing
│   ├── wsgi.py                     # WSGI configuration
│   ├── asgi.py                     # ASGI configuration
│   └── settings/
│       ├── base.py
│       ├── development.py
│       └── production.py
│
├── apps/                           # Django applications
│   │
│   ├── movies/                     # Movie management
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py               # Movie, Genre models
│   │   ├── views.py                # Movie views
│   │   ├── viewsets.py             # DRF ViewSets
│   │   ├── serializers.py          # DRF serializers
│   │   ├── urls.py
│   │   ├── filters.py              # Search & filter logic
│   │   ├── services.py             # Business logic
│   │   ├── admin.py                # Django admin
│   │   ├── forms.py
│   │   └── templates/
│   │
│   ├── reviews/                    # Review & rating system
│   │   ├── migrations/
│   │   ├── models.py               # Review, Rating models
│   │   ├── viewsets.py             # Review ViewSets
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── permissions.py
│   │
│   ├── users/                      # User management
│   │   ├── migrations/
│   │   ├── models.py               # UserProfile model
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── templates/
│   │
│   ├── watchlist/                  # Watchlist management
│   │   ├── migrations/
│   │   ├── models.py
│   │   ├── viewsets.py
│   │   ├── serializers.py
│   │   └── urls.py
│   │
│   ├── recommendations/            # Recommendation engine
│   │   ├── views.py
│   │   ├── algorithms.py
│   │   ├── services.py
│   │   └── urls.py
│   │
│   ├── api/                        # API configuration
│   │   ├── __init__.py
│   │   ├── urls.py                 # API URL routing
│   │   ├── permissions.py          # Custom permissions
│   │   ├── throttles.py            # Rate limiting
│   │   ├── pagination.py           # Pagination settings
│   │   └── filters.py              # DRF filters
│   │
│   └── accounts/                   # Authentication
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── urls.py
│
├── static/                         # Static files
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   └── style.css
│   ├── js/
│   │   ├── bootstrap.bundle.min.js
│   │   ├── jquery.min.js
│   │   └── app.js
│   └── images/
│
├── templates/                      # HTML templates
│   ├── base.html
│   ├── navbar.html
│   ├── footer.html
│   ├── home.html
│   ├── movies/
│   │   ├── movie_list.html
│   │   └── movie_detail.html
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   └── 404.html, 500.html
│
├── fixtures/                       # Initial data
│   └── movies_initial_data.json
│
├── tests/                          # Test suite
│   ├── test_models.py
│   ├── test_views.py
│   ├── test_apis.py
│   ├── test_serializers.py
│   └── test_services.py
│
├── logs/                           # Application logs
│   └── movie_app.log
│
└── docs/                           # Documentation
    ├── API_GUIDE.md
    ├── SETUP_GUIDE.md
    └── USER_GUIDE.md
```

---

## ⚙️ Configuration

### **Environment Variables** (.env)
```bash
# Django Configuration
DEBUG=False
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=movies_db
DB_USER=postgres
DB_PASSWORD=secure_password
DB_HOST=localhost
DB_PORT=5432

# API Settings
API_PAGINATION_PAGE_SIZE=20
API_THROTTLE_RATE=100/hour

# Email (for notifications)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=app-password

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000

# Caching (optional)
CACHE_BACKEND=django.core.cache.backends.redis.RedisCache
CACHE_LOCATION=redis://127.0.0.1:6379/1
```

---

## ⚡ Performance Optimization

### **Database Optimization**
```python
# Indexing on frequently searched fields
class Meta:
    indexes = [
        models.Index(fields=['title']),
        models.Index(fields=['genre']),
        models.Index(fields=['-rating']),
    ]

# Select related for foreign keys
queryset = Movie.objects.select_related('genre')

# Prefetch related for reverse relationships
queryset = Movie.objects.prefetch_related('reviews')
```

### **Query Optimization**
```python
# Use only() and defer() to limit fields
queryset = Movie.objects.only('id', 'title', 'rating')

# Aggregate ratings instead of fetching all
avg_rating = Review.objects.filter(movie=movie).aggregate(
    Avg('rating')
)['rating__avg']
```

### **Caching Strategies**
```python
# Cache expensive queries
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # Cache for 5 minutes
def movie_list(request):
    ...

# Cache templates fragments
{% load cache %}
{% cache 300 movie_detail movie.id %}
    ...expensive template rendering...
{% endcache %}
```

### **API Response Optimization**
- ✅ Pagination for large datasets
- ✅ Lazy loading of related objects
- ✅ Response compression (gzip)
- ✅ CDN for static files
- ✅ Database connection pooling

---

## 🧪 Testing

### **Run Tests**
```bash
# All tests
python manage.py test

# Specific app
python manage.py test apps.movies

# With verbose output
python manage.py test -v 2

# Generate coverage report
coverage run --source='.' manage.py test
coverage report
coverage html
```

### **Test Coverage Areas**
- ✅ Model tests
- ✅ View tests
- ✅ API endpoint tests
- ✅ Authentication tests
- ✅ Permission tests
- ✅ Service layer tests

---

## 🚢 Deployment

### **Production Deployment Steps**

1. **Prepare Environment**
   ```bash
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com
   ```

2. **Collect Static Files**
   ```bash
   python manage.py collectstatic --noinput
   ```

3. **Run Migrations**
   ```bash
   python manage.py migrate --run-syncdb
   ```

4. **Configure Web Server** (Gunicorn + Nginx)
   ```bash
   gunicorn config.wsgi:application --bind 0.0.0.0:8000
   ```

5. **Set Up Database** (PostgreSQL)
   - Create production database
   - Configure backups
   - Set up monitoring

6. **Enable HTTPS** (SSL/TLS)
   - Use Let's Encrypt
   - Configure secure headers

### **Deployment Platforms**
- Heroku (`Procfile` ready)
- AWS (EC2, ECS, Elastic Beanstalk)
- DigitalOcean (Droplet)
- Render
- Replit

---

## 🤝 Contributing

### **How to Contribute**
1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

### **Code Guidelines**
- Follow PEP 8
- Write tests for new features
- Update documentation
- Use clear commit messages
- Keep code DRY

---

## 📄 License

Licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Nandakishor**
- GitHub: [@Nandakishor-773](https://github.com/Nandakishor-773)
- Email: nandakishor.dev@example.com
- LinkedIn: [Nandakishor](https://linkedin.com/in/nandakishor)

---

## 📞 Support

- 🐛 [Report Issues](https://github.com/Nandakishor-773/movie_django-project/issues)
- 💬 [Discussions](https://github.com/Nandakishor-773/movie_django-project/discussions)
- 📧 nandakishor.dev@example.com

---

<div align="center">

### ⭐ Star this repository if you find it useful!

**Made with ❤️ by Nandakishor**

</div>
