# Weather-app-using-Django-Python
In this project, we will learn how to create a Weather app that uses Django as backend. Django provides a Python Web framework based web framework that allows rapid development and clean, pragmatic design.

# Weather App with Django

### Basic Setup
1. Change directory to weather: `cd weather`
2. Start the server: `python manage.py runserver`
3. Open http://127.0.0.1:8000/ in a web browser.

### Implementation
1. Create a Django app: `python manage.py startapp main`
2. Edit `settings.py` to include the 'main' app.
3. Create `main/templates/main/index.html` for the frontend.
4. Implement weather fetching in `views.py` using OpenWeatherMap API.

### Running the App
1. Navigate to the project directory.
2. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`.
3. Start the server: `python manage.py runserver`.

---

