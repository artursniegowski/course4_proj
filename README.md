# course4_proj
OMDB project in Course 4 of Advanced Django specialization

A repository containing all the assignments completed from <br>
Advanced Django: Mastering Django and Django Rest Framework Specialization: <br>  https://www.coursera.org/specializations/codio-advanced-django-and-django-rest-framework 
4. Advanced Django: External APIs and Task Queuing  <br> https://www.coursera.org/learn/codio-advanced-django-external-apis-task-queuing?specialization=codio-advanced-django-and-django-rest-framework <br>


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

---
## ABOUT
The site is a platform where users can discuss movies. It focuses on designing models based on OMDb data. 
Users can comment on or read about movies. When searching for a movie, the site prioritizes its local database, only querying OMDb if necessary. Basic movie data is stored locally, and detailed data is fetched as needed. If a movie's details change, it's updated in real-time. Here's how it works: users search for a movie, the site checks its database, fetches from OMDb if needed, and displays results. If more detail is needed, it fetches it from the API.


---

## What you'll learn (4. Advanced Django: External APIs and Task Queuing) :
- Connecting to external APIs
- Implement task queuing (Schedule tasks with Celery and Redis)
- Leverage various Django skills to create portfolio-quality projects

---

The modules in this course cover connecting to external APIs, task queuing, and pulling together the topics across the specialization in capstone projects.

--

Skills:
  - Django (Web Framework)
  - Python Programming

---
