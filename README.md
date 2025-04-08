 📝 Task Manager API

A scalable and professional-grade Task Manager API built using **Django** and **Django REST Framework**. This project is ideal for learning how to build real-world RESTful APIs with clean architecture, custom user models, task management features, and best practices followed by experienced Django developers.

---

 🚀 Features

- 🔐 Custom user model (using `AbstractUser`)
- ✅ Full CRUD for tasks
- 🏷️ Task tagging support
- 📊 Task priorities (`Low`, `Medium`, `High`)
- 🔄 Task status tracking (`Pending`, `In Progress`, `Completed`)
- 📅 Due dates with automatic overdue detection
- 🧠 Clean, reusable model structure using abstract base classes
- 🌐 RESTful API ready for frontend or mobile integration

---

🧰 Tech Stack

- Python 
- Django 
- Django REST Framework
- SQLite (for dev, can be upgraded to PostgreSQL)
- JWT Authentication (to be added)

---

 ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver



🧑‍💻 Author
Hassan Buruhani
Learning Django the professional way.
Feel free to follow or contribute!
