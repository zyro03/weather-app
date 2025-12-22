import customtkinter as ctk

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

button_search = ctk.CTkButton(buttons_frame, text="Search", height=30)
button_search.pack(side="left")

button_location = ctk.CTkButton(buttons_frame, text="Use current location", height=30)
button_location.pack(side="left")

result_frame = ctk.CTkFrame(app, width=450, height=450, corner_radius=20)
result_frame.pack(pady=30)
result_frame.pack_propagate(False)

label_temp = ctk.CTkLabel(result_frame, text="--*C")
label_temp.pack()

label_city = ctk.CTkLabel(result_frame, text="--*C")
label_city.pack()

app.mainloop()