import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "bd1882222b03b6dff3173d324d07e1c8"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]

        result_text = (
            f"Temperature: {temperature}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Weather: {weather_description.capitalize()}"
        )
        result_label.config(text=result_text)
    else:
        result_label.config(text="City not found. Please try again.")

root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")
root.configure(bg="#87CEEB")

title_label = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"), bg="#87CEEB")
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter city name:", font=("Arial", 12), bg="#87CEEB")
city_label.pack(pady=5)
city_entry = tk.Entry(root, width=20, font=("Arial", 12))
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#87CEEB", activebackground="#87CEEB", relief="flat")
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#87CEEB", wraplength=250, justify="left")
result_label.pack(pady=10)

root.mainloop()