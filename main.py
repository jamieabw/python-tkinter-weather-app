import requests
from tkinter import Tk, Label, Button, Entry, END, Toplevel, messagebox

# API Key for OpenWeatherMap
KEY = "ENTER YOUR API KEY HERE"

# Get the public IP address
IP = requests.get('https://api.ipify.org').content.decode('utf8')

class App:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        self.window.geometry("320x160")
        self.window.resizable(False, False)
        self.window.title("Weather App")
        
        # Create UI elements
        self.lat_label = Label(self.window, text="Enter latitude:")
        self.long_label = Label(self.window, text="Enter longitude:")
        self.lat_label.pack()
        self.latitude = Entry(self.window, width=30)
        self.longitude = Entry(self.window, width=30)
        self.submit = Button(self.window, text="Submit", command=self.display_weather)
        self.locate_button = Button(self.window, text="Auto detect location", command=self.get_location)
        self.warning = Label(self.window, text="Auto detect can occasionally incorrectly locate you.", foreground="red")
        self.latitude.pack()
        self.long_label.pack()
        self.longitude.pack()
        self.warning.pack()
        self.locate_button.pack()
        self.submit.pack()
        
        # Start the main event loop
        self.window.mainloop()

    def get_location(self):
        # Clear latitude and longitude entries
        self.latitude.delete(0, END)
        self.longitude.delete(0, END)
        
        # Use IP address to get location data
        location_data = requests.get(f"http://ip-api.com/json/{IP}").json()
        latitude = location_data["lat"]
        longitude = location_data["lon"]
        
        # Update the latitude and longitude entries with detected values
        self.latitude.insert(0, latitude)
        self.longitude.insert(0, longitude)

    def display_weather(self):
        try:
            # Check if latitude and longitude inputs are valid floats
            float(self.latitude.get())
            float(self.longitude.get())
        except Exception as x:
            # Clear latitude and longitude entries if not valid floats
            self.latitude.delete(0, END)
            self.longitude.delete(0, END)
            return

        # Build the URL for weather data using latitude, longitude, and API key
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude.get()}&lon={self.longitude.get()}&appid={KEY}"
        
        # Check if API request was successful
        if requests.get(url).status_code != 200:
            messagebox.showerror(title="Error", message="There is an error with the API, try again later.")
            return

        # Create a new window to display weather data
        weather_window = Toplevel()

        # Get weather and main data from the API response
        weather_data = requests.get(url).json()["weather"][0]
        main_data = requests.get(url).json()["main"]
    

        # Create labels to display weather information
        temp = Label(weather_window, text=f"Temperature: {round((main_data['temp'] - 273.15), 0)}°C")
        feels_temp = Label(weather_window, text=f"Feels like: {round((main_data['feels_like'] - 273.15), 0)}°C")
        weather = Label(weather_window, text=f"Weather: {weather_data['description']}")
        humidity = Label(weather_window, text=f"Humidity: {main_data['humidity']}%")
        
        # Pack the labels into the weather window
        weather.pack()
        temp.pack()
        feels_temp.pack()
        humidity.pack()

def main():
    # Create an instance of the App class
    weather = App()

if __name__ == "__main__":
    # Call the main function to start the application
    main()
