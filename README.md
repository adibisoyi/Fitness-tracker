# Fitness Tracker

Fitness Tracker is a web application designed to help users monitor and manage their fitness activities. Built with Python and Django, it offers a user-friendly interface for tracking workouts, setting goals, and analyzing progress.

## Features
- **User Authentication**: Secure sign-up and login processes to manage personal accounts.
- **Workout Logging**: Record details of exercises, including type, duration, and intensity.
- **Goal Setting**: Define and track fitness objectives to stay motivated.
- **Progress Analysis**: Visualize workout data to monitor improvements over time.
- **Responsive Design**: Access the application seamlessly across various devices.

## Getting Started

### Prerequisites
- Python 3.x
- Django 3.x
- SQLite (default database)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/adibisoyi/Fitness-tracker.git
   cd Fitness-tracker
    ```
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
5. **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```
Access the application at http://127.0.0.1:8000/.

### Usage
**User Registration:** Sign up to create a new account.
**Workout Logging:** Add new workouts with relevant details.
**Goal Management:** Set and monitor fitness goals.
**Progress Tracking:** View charts and statistics to assess progress.

### Contributing
Contributions are welcome! To contribute:

### Fork the repository.
- Create a new branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature/your-feature).
- Create a new Pull Request.

### Acknowledgments
- Django for the robust web framework.
- Bootstrap for responsive design components.
