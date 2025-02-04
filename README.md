# course4_proj
OMDB project in Course 4 of Advanced Django specialization

A repository containing all the assignments completed from <br>

Advanced Django: Mastering Django and Django Rest Framework Specialization:  
https://www.coursera.org/specializations/codio-advanced-django-and-django-rest-framework <br>
4. Advanced Django: External APIs and Task Queuing  <br> 
https://www.coursera.org/learn/codio-advanced-django-external-apis-task-queuing?specialization=codio-advanced-django-and-django-rest-framework <br>


---
## WHAT YOU NEED TO RUN THE PROJECT
The Open Movie Database is a free REST web service that can be queried to get information about movies. 
You’ll need an API key. One can be obtained free from https://www.omdbapi.com/apikey.aspx.

You will have to set an environment variable as follows (in the command line): <br>
`export DJANGO_OMDB_KEY=your_omdb_api_key`  <br>
OR prepend it to the command like so: <br>
`DJANGO_OMDB_KEY=your_omdb_api_key python manage.py ...`


Custom django commands to run queries: <br>

Populate movie data in our local database <br>
- `python manage.py movie_search movie_titel_here` <br>

Updating movie details <br>
- `python manage.py movie_fill tt1853728` <br>
- `python manage.py movie_fill movie_id_omdb`


You will also need a GitHub access token, which can be obtained here: <br>
https://github.com/settings/tokens/new


Starting celery worker: <br>
`celery -A course4_proj worker -l DEBUG`

Starting Celery beat  tasks that have been scheduled by calling the add_periodic_task():<br>
`celery -A course4_proj beat -l INFO`

Starting Celery beat to read the schedule from the Django database (or a different schedule store): <br>
`celery -A course4_proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`


---
## ABOUT
The site is a platform where users can discuss movies. It focuses on designing models based on OMDb data. 
Users can comment on or read about movies. When searching for a movie, the site prioritizes its local database, only querying OMDb if necessary. Basic movie data is stored locally, and detailed data is fetched as needed. If a movie's details change, it's updated in real-time. Here's how it works: users search for a movie, the site checks its database, fetches from OMDb if needed, and displays results. If more detail is needed, it fetches it from the API.


---

## What you'll learn (4. Advanced Django: External APIs and Task Queuing) :
- Connecting to external APIs
- Implement task queuing (Schedule tasks with Celery and Redis)
- Leverage various Django skills to create portfolio-quality projects
- Get and parse content from an API with the Requests library
- Use the OMDb API to fetch information about movies
- Generate a GitHub access token and integrate it with Django to query GitHub
- Implementig Celery - task queue, register celery task for asynchronous tasks
- Signals, asynchronous signals, custom signals
- Create a periodic task with Celery
- Celery Beat - Schedule tasks that run on an interval or on a specified date/time

---

The modules in this course cover connecting to external APIs, task queuing, and pulling together the topics across the specialization in capstone projects.

--

Skills:
  - Django (Web Framework)
  - Python Programming

---
