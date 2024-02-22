# Weather App for Evaluation

## Setup

### 1. Create a Virtual Environment (Optional but Recommended)

# Using venv (Python 3)
python3 -m venv env

# Activate the virtual environment (Linux/Mac)
source env/bin/activate

# Activate the virtual environment (Windows)
env\Scripts\activate

# install requiremnts
pip install -r requirments.txt

# Run the application
python manage.py runserver


# Functionality
# Features
User Authentication
Users can login, and logout.
# credential 
username : admin
password : admin

The login_required decorator is used to restrict access to certain views.
Dashboard
Authenticated users have access to a dashboard where they can view weather information for their favorite cities.

Weather Data Fetching
Asynchronous data fetching using aiohttp to fetch weather information from the OpenWeather API.
Favorite Cities Management
Authenticated users can add  cities from their list of favorite cities.
# Usage
login with an existing account whose credenial is already given.
Add your favorite cities using the "Add to Favorites" button.
View weather information for your favorite cities on the dashboard.
# API Reference
GET /checkweather
Retrieves weather information for a specific city.
Parameters:
cityname: Name of the city to retrieve weather information for.
POST /addfavorite
Adds a city to the user's list of favorite cities.
Parameters:
cityvalue: Name of the city to add to favorites.
# Authors
Sohaib Ahmad