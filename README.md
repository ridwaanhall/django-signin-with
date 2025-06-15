# 🚀 Django Social - Live Chat Application

A modern, real-time chat application built with Django, featuring Google OAuth authentication, reply system, and a beautiful dark mode interface with minimalist design focused purely on chat functionality.

![Django](https://img.shields.io/badge/Django-5.2.3-092E20?style=flat&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-7952B3?style=flat&logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

## 🆕 Latest Updates

- ✅ **Full Date & Time Display** - Messages now show complete timestamps (DD/MM/YYYY, HH:MM)
- ✅ **Minimalist UI** - Clean interface with only chat functionality
- ✅ **Dark Mode Theme** - Beautiful dark mode with gradient backgrounds
- ✅ **Integrated Sign-out** - Seamless sign-out button at chat bottom
- ✅ **Author System** - Special recognition for site owners/authors
- ✅ **Asia/Jakarta Timezone** - Proper timezone support for Indonesian users

## ✨ Features

### 🔐 **Authentication & Profiles**
- **Google OAuth Integration** - Seamless sign-in with Google accounts
- **Profile Pictures** - Automatic profile image sync from Google
- **Full Name Display** - Shows users' real names from Google profiles
- **Author System** - Special badges for site owners/authors

### 💬 **Chat Functionality**
- **Real-time Messaging** - Instant message delivery with AJAX
- **Reply System** - Reply to specific messages with context
- **Message History** - Persistent chat history stored in database
- **Auto-refresh** - Automatic chat updates every 30 seconds
- **Message Counter** - Live count of total messages
- **Date & Time Stamps** - Full date and time display (DD/MM/YYYY, HH:MM)
- **Timezone Support** - Displays messages in Asia/Jakarta timezone

### 🎨 **Modern UI/UX**
- **Dark Mode Interface** - Beautiful dark theme for better user experience
- **Minimalist Design** - Clean, focused interface with only the chat card
- **Responsive Design** - Works perfectly on desktop and mobile devices
- **Smooth Animations** - Elegant fade-in animations for new messages
- **Hover Effects** - Interactive message bubbles and buttons
- **Custom Scrollbars** - Styled scrollbars that match the dark theme
- **Centered Layout** - Full-screen gradient background with centered chat
- **Integrated Sign-out** - Sign-out button seamlessly integrated at bottom

### 👑 **Author Management**
- **Author Designation** - Mark specific users as site authors/owners
- **Visual Badges** - Golden star badges to identify authors
- **Management Commands** - Easy CLI tools to manage author status

## 🛠️ Technologies Used

- **Backend**: Django 5.2.3, Python 3.12+
- **Frontend**: Bootstrap 5.3.0, HTML5, CSS3, JavaScript
- **Authentication**: Django Allauth with Google OAuth
- **Database**: SQLite (development), PostgreSQL ready
- **Styling**: Custom CSS with dark mode theme
- **Icons**: Bootstrap Icons

## 📦 Installation

### Prerequisites
- Python 3.12 or higher
- pip package manager
- Google OAuth credentials

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-social.git
cd django-social
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django django-environ django-allauth
```

### 4. Environment Setup
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### 5. Database Migration
```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## ⚙️ Configuration

### Google OAuth Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google+ API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URIs:
   - `http://127.0.0.1:8000/accounts/google/login/callback/` (development)
   - `https://yourdomain.com/accounts/google/login/callback/` (production)

### Author Management

Check a user:
```bash
python manage.py shell -c "from django.contrib.auth.models import User; print('Available users:'); [print(f'- {user.username} ({user.email})') for user in User.objects.all()]"
```

Make a user an author:
```bash
python manage.py make_author username
```

Remove author status:
```bash
python manage.py make_author username --remove
```

## 🏗️ Project Structure

```
django-social/
├── base/                           # Main application
│   ├── management/
│   │   └── commands/
│   │       └── make_author.py      # Author management command
│   ├── migrations/                 # Database migrations
│   ├── templates/base/
│   │   └── home.html              # Chat interface template
│   ├── models.py                  # Data models
│   ├── views.py                   # View functions
│   └── urls.py                    # URL routing
├── gglinks/                       # Project settings
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Main URL configuration
│   └── wsgi.py                    # WSGI configuration
├── templates/
│   └── base.html                  # Base template
├── manage.py                      # Django management script
└── README.md                      # Project documentation
```

## 🎯 Usage

### Basic Chat Usage
1. **Sign In**: Click "Sign in with Google" to authenticate
2. **Send Messages**: Type your message and press Enter or click send
3. **Reply to Messages**: Click the reply button on any message
4. **View Timestamps**: All messages show full date and time (DD/MM/YYYY, HH:MM)
5. **Sign Out**: Use the sign out button at the bottom of the chat

### Admin Features
- **Make Authors**: Use management commands to designate authors
- **Monitor Chat**: Authors get special visual recognition with star badges
- **Manage Users**: Access Django admin panel for user management

## 🚀 Deployment

### Environment Variables for Production
```env
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### Database Configuration
For production, update `settings.py` to use PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 API Endpoints

- `GET /` - Home page with chat interface
- `POST /send-message/` - Send new chat message (AJAX)
- `POST /logout/` - User logout
- `/accounts/google/login/` - Google OAuth login

## 🔧 Customization

### Theming
The application uses CSS custom properties for easy theming. Modify the CSS variables in `templates/base.html` to change colors:

```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --dark-bg: #2d2d2d;
    --message-bg: #3a3a3a;
}
```

### Features Extension Ideas
- Add message editing functionality
- Implement message deletion
- Add file/image sharing
- Create private messaging
- Add emoji reactions
- Message search functionality
- User typing indicators
- Message status (sent, delivered, read)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Django team for the amazing framework
- Bootstrap team for the UI components
- Google for OAuth integration
- All contributors and users

## 📊 Stats

- **Lines of Code**: ~1,500
- **Models**: 2 (ChatMessage, UserProfile)
- **Views**: 2 (home, send_message)
- **Templates**: 2 (base.html, home.html)
- **Management Commands**: 1 (make_author)

---

**Made with ❤️ using Django and Bootstrap**
