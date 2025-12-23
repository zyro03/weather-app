import customtkinter as ctk
import os
import requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
load_dotenv()


API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {
            "q":city,
            "appid":API_KEY,
            "units":"metric"
            }
        r = requests.get(URL, params=params, timeout=8)
        r.raise_for_status()
        data = r.json()
       
        icon_code = data["weather"][0]["icon"]
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}.png"
        
        img = Image.open(BytesIO(requests.get(icon_url).content))
        icon_image = ctk.CTkImage(light_image=img, size=(120,120))

        label_icon.configure(image=icon_image)
        label_icon.image = icon_image

        temp = data['main']['temp']
        descr = data['weather'][0]['description']
        label_temp.configure(text=f"{round(temp,1)} °C")
        label_desc.configure(text=descr)
    except:
        print("Blad")

def get_city():
    city=entry_location.get()
    label_city.configure(text=city.capitalize())
    if not city:
        label_temp.configure(text="Enter city")
        return
    get_weather(city)
    

app = ctk.CTk()
app.title("weather-app")
app.geometry("800x600")

title = ctk.CTkLabel(app, text="What's the weather like today?", font=ctk.CTkFont(size=22, weight="bold"))
title.pack()

search_frame = ctk.CTkFrame(app, width=450, height=120, corner_radius=20)
search_frame.pack()
search_frame.pack_propagate(False)

title_location = ctk.CTkLabel(search_frame, text="Set location",font=ctk.CTkFont(size=12, weight="bold"))
title_location.pack()

entry_location = ctk.CTkEntry(search_frame, placeholder_text="Enter city", height=30, width=350)
entry_location.pack()

buttons_frame = ctk.CTkFrame(search_frame, fg_color="transparent")
buttons_frame.pack()

button_search = ctk.CTkButton(buttons_frame, text="Search", height=30, command=get_city)
button_search.pack(side="left")

button_location = ctk.CTkButton(buttons_frame, text="Use current location", height=30)
button_location.pack(side="left")

result_frame = ctk.CTkFrame(app, width=450, height=450, corner_radius=20)
result_frame.pack(pady=30)
result_frame.pack_propagate(False)

label_icon = ctk.CTkLabel(result_frame, text="")
label_icon.pack()

label_temp = ctk.CTkLabel(result_frame, text="", font=ctk.CTkFont(size=30, weight="bold"))
label_temp.pack()

label_desc = ctk.CTkLabel(result_frame, text="", font=ctk.CTkFont(size=15, weight="bold"))
label_desc.pack()

label_city = ctk.CTkLabel(result_frame, text="")
label_city.pack()

app.mainloop()