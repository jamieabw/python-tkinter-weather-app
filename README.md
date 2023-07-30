# python-tkinter-weather-app
Weather App
This is a simple weather application that allows users to retrieve weather information by specifying their latitude and longitude or by using auto-detection based on their IP address. The application utilizes the OpenWeatherMap API to fetch weather data.

Prerequisites
To run this application, you need to have the following:

Python 3 installed on your machine
The requests library installed (pip install requests)
Installation
Clone or download this repository to your local machine.

Open a terminal or command prompt and navigate to the project directory.

Run the application by executing the following command:
```bash
python weather_app.py
```

Usage
Upon launching the application, a window will appear with latitude and longitude input fields, a submit button, and an auto-detect location button.
To manually enter the coordinates, type the latitude and longitude values into the respective input fields.
Click the "Submit" button to retrieve the weather information for the specified location.
To use auto-detection, click the "Auto detect location" button. Note that auto-detection may occasionally incorrectly locate you.
If the latitude and longitude values are valid floats, a new window will appear displaying the weather information, including temperature, feels like temperature, weather description, and humidity.
If there is an error with the API or the latitude/longitude values are not valid floats, an error message will be displayed.
API Key
To fetch weather data, this application requires an API key from OpenWeatherMap. The API key should be assigned to the KEY variable in the main.py file. You can obtain an API key by signing up on the OpenWeatherMap website.
