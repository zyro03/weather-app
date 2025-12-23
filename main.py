import customtkinter as ctk
import os
import requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
load_dotenv()

ICON_SIZE = (50, 50)

icon_feels = ctk.CTkImage(
    light_image=Image.open("icon_feels.png"),
    size=ICON_SIZE
)

icon_humidity = ctk.CTkImage(
    light_image=Image.open("icon_humidity.png"),
    size=ICON_SIZE
)

icon_wind = ctk.CTkImage(
    light_image=Image.open("icon_wind.png"),
    size=ICON_SIZE
)

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
        feels = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        label_temp.configure(text=f"{round(temp,1)} °C")
        label_desc.configure(text=descr)
        
        card_feels_value.configure(text=f"{round(feels,1)} °C")
        card_humidity_value.configure(text=f"{humidity} %")
        card_wind_value.configure(text=f"{round(wind,1)} km/h")


    except:
        print("Blad")

def get_city():
    city=entry_location.get()
    label_city.configure(text=city.capitalize())
    if not city:
        label_temp.configure(text="Enter city")
        return
    result_frame.pack(pady=30)
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

result_frame = ctk.CTkFrame(app, width=540, height=350, corner_radius=20)

result_frame.pack_propagate(False)

label_icon = ctk.CTkLabel(result_frame, text="")
label_icon.pack()

label_temp = ctk.CTkLabel(result_frame, text="", font=ctk.CTkFont(size=30, weight="bold"))
label_temp.pack()

label_desc = ctk.CTkLabel(result_frame, text="", font=ctk.CTkFont(size=15, weight="bold"))
label_desc.pack()

label_city = ctk.CTkLabel(result_frame, text="", font=ctk.CTkFont(size=15, weight="bold"))
label_city.pack(pady=(0,30))

details_frame = ctk.CTkFrame(result_frame, fg_color="transparent")
details_frame.pack()

card_feels = ctk.CTkFrame(details_frame, width=180, height=90)
card_feels.pack(side="left")
card_feels.pack_propagate(False)

row = ctk.CTkFrame(card_feels, fg_color="transparent")
row.pack()

card_feels_icon = ctk.CTkLabel(row, image=icon_feels, text="")
card_feels_icon.pack(side="left")

text_col = ctk.CTkFrame(row, fg_color="transparent")
text_col.pack(side="left")

card_feels_title = ctk.CTkLabel(
    text_col,
    text="Feels like",font=ctk.CTkFont(size=15, weight="bold")
)
card_feels_title.pack(anchor="w")

card_feels_value = ctk.CTkLabel(
    text_col,
    text="",
)
card_feels_value.pack(anchor="w")


card_humidity = ctk.CTkFrame(details_frame, width=180, height=90)
card_humidity.pack(side="left")
card_humidity.pack_propagate(False)

row_humidity = ctk.CTkFrame(card_humidity, fg_color="transparent")
row_humidity.pack()

card_humidity_icon = ctk.CTkLabel(row_humidity, image=icon_humidity, text="")
card_humidity_icon.pack(side="left")

text_col_humidity = ctk.CTkFrame(row_humidity, fg_color="transparent")
text_col_humidity.pack(side="left")

card_humidity_title = ctk.CTkLabel(text_col_humidity, text="Humidity",font=ctk.CTkFont(size=15, weight="bold"))
card_humidity_title.pack(anchor="w")

card_humidity_value = ctk.CTkLabel(text_col_humidity, text="")
card_humidity_value.pack(anchor="w")


card_wind = ctk.CTkFrame(details_frame, width=180, height=90)
card_wind.pack(side="left")
card_wind.pack_propagate(False)

row_wind = ctk.CTkFrame(card_wind, fg_color="transparent")
row_wind.pack()

card_wind_icon = ctk.CTkLabel(row_wind, image=icon_wind, text="")
card_wind_icon.pack(side="left")

text_col_wind = ctk.CTkFrame(row_wind, fg_color="transparent")
text_col_wind.pack(side="left")

card_wind_title = ctk.CTkLabel(text_col_wind, text="Wind",font=ctk.CTkFont(size=15, weight="bold"))
card_wind_title.pack(anchor="w")

card_wind_value = ctk.CTkLabel(text_col_wind, text="")
card_wind_value.pack(anchor="w")




app.mainloop() 