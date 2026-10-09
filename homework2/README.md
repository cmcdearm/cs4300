# Movie Theater Booking Application

This project is a Django + Django REST Framework movie theater booking app built for Homework 2.

## Features
- Movie listing page with Bootstrap styling
- Seat booking flow
- Booking history page
- RESTful API endpoints for movies, seats, and bookings
- Unit and API tests

## Project structure
- `movie_theater_booking/` – Django project configuration
- `bookings/` – models, serializers, views, templates, and tests

## Requirements
- Python 3.12+
- Django 6.x
- djangorestframework

## Setup
1. Open a terminal inside the project folder.
2. Create and activate a virtual environment:
   ```bash
   cd /coursework/cs4300/homework2
   python3 -m venv myenv
   source myenv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install django djangorestframework
   ```
4. Run the database setup:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver 0.0.0.0:3000
   ```
6. Open the app in the browser using the DevEdu app link or local host.

## API endpoints
- `GET /api/movies/` – list all movies
- `GET /api/seats/` – list seat records
- `GET /api/bookings/` – list booking history

## UI routes
- `/` – movie listing page
- `/book/<movie_id>/` – seat booking page
- `/history/` – booking history page

## Testing
Run:
```bash
python manage.py test bookings
```

## AI usage disclosure
This project was developed with guidance from the homework PDF and GitHub Copilot for scaffold planning, Django structure suggestions, and debugging support. The generated code was reviewed and adapted to fit the project requirements.

## Deployment
Add your Render URL here once the app is deployed.
