# Django Blog Project

A Django-based blog application with user authentication, post management, and media upload functionality.

## Features

- 📝 **Blog Post Management**: Create, edit, and delete blog posts
- 👤 **User Authentication**: Login, registration, and user profiles
- 🖼️ **Media Upload**: Upload and manage images for posts
- 📱 **Responsive Design**: Mobile-friendly interface
- 🔐 **Secure**: Environment variables for sensitive data

## Project Structure

```
Project/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .env                     # Environment variables (not in repo)
├── Project/                 # Main project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL configuration
│   └── ...
├── posts/                   # Blog posts app
│   ├── models.py            # Post models
│   ├── views.py             # Post views
│   ├── urls.py              # Post URLs
│   └── templates/           # Post templates
├── Users/                   # User authentication app
│   ├── models.py            # User models
│   ├── views.py             # User views
│   └── templates/           # User templates
├── templates/               # Global templates
├── static/                  # Static files (CSS, JS)
└── media/                   # User uploads (not in repo)
```

## Technologies Used

- **Backend**: Django 5.2.4
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS, JavaScript
- **Environment**: Python 3.13
- **Dependencies**: python-dotenv, Pillow

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Vicky16032205/Django-blog-project.git
cd Django-blog-project
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r Project/requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the `Project/` directory with:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Setup
```bash
cd Project
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
python manage.py collectstatic
```

### 7. Run the Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

## Development

### Project Apps
- **posts**: Handles blog post functionality
- **Users**: Manages user authentication and profiles

### Key Features
- **Environment Variables**: Secure configuration management
- **Media Handling**: File upload and management
- **User Authentication**: Login/logout functionality
- **Admin Interface**: Django admin for content management

## Deployment

For production deployment:
1. Set `DEBUG=False` in your `.env` file
2. Update `ALLOWED_HOSTS` with your domain
3. Configure a production database (PostgreSQL recommended)
4. Set up static file serving
5. Configure media file handling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Contact

- **Developer**: Vicky
- **Email**: vickyguptagkp55@gmail.com
- **GitHub**: [Vicky16032205](https://github.com/Vicky16032205)
