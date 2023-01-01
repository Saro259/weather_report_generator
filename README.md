# weather_report_generator
A concise weather reporter written in python language which gives the current weather report of a city in india.
# Usage
A weather result of the city name given as an input by the user gets returned. The function 'weather_page' when invoked takes the input from the user and also returns 
the weather output by constructing the target url link which hits over the API.
# Rest API
Start the webserver django application python manage.py runserver http://127.0.0.1:8000/
Send a POST Request(using postman) http://127.0.0.1:8000/weatherReport/
The Server will respond with the following JSON format: {
    "city": "ahmedabad",
    "main": "Clear"
}
