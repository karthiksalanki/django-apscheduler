# django-apscheduler

*   Project Overview:

    *   Django APScheduler for Scheduler Jobs. Advanced Python Scheduler (APScheduler) is a Python library
        that lets you schedule your Python code to be executed later, either just once or periodically. You can add new jobs or to view old jobs. 


*   Features:
    *   Task Scheduling: Schedule tasks using interval and cron-based scheduling.
    *   API Endpoints: APIs to create, retrieve, and manage scheduled jobs.
    *   Scalability: Designed to handle high loads and complex scheduling tasks.
    *   API Documentation: Integrated with Swagger for interactive API documentation.

*   Prerequisites:

    *   Python 3.x
    *   Django 3.x or higher
    *   Required packages listed in requirements.txt

*   Installation:

    1.Clone the repository:
        git clone https://github.com/your-username/your-repository.git

    2.Navigate to the project directory:
        cd project-repository

    3.Set up a virtual environment:
        python -m venv venv
        venv\Scripts\activate   # on Linux venv/bin/activate

    4.Install dependencies:
        pip install -r requirements.txt

    5.Set up the database:
        Default sqlite3 Database
        python manage.py migrate

    6.Run the development server:
        python manage.py runserver


*   Usage:
        1.Starting the Scheduler:
            The scheduler is initiated automatically when the server starts.

        2.Using the APIs:

            Create a Job:
            curl -X POST http://localhost:8000/api/job/ -H "Content-Type: application/json" -d '{"name": "Test Job", "schedule_type": "interval", "schedule_details": {"minutes": 2}}'

        3.List Jobs:
            curl http://localhost:8000/api/jobs/

*   API Documentation:
    *   Your API is documented using drf-spectacular. Once the server is running, you can access the API
        http://localhost:8000/api/schema/docs/

*   Load Testing with Locust:
    *   To ensure the scalability of our application, we used Locust for load testing. Locust is an
        open-source load testing tool that allows us to simulate concurrent users and generate high volumes of API requests.

*   Purpose:
    *   The load testing aimed to validate the application's ability to handle approximately:

    *   10,000 users spread globally
    *   1,000 services
    *   6,000 API requests per minute

*   Setup and Execution:
    *   Install Locust:
            pip install locust
    
    *   Run Locust:
            locust

    *   Monitor Results:
            Access the Locust web interface at http://localhost:8089 to configure the number of users, hatch rate, and monitor the performance under load.