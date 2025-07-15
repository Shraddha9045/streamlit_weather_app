import streamlit as st
import requests

# ✅ Hardcoded API Key
import streamlit as st

API_KEY = st.secrets["API_KEY"]

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "location": f"{data['name']}, {data['sys']['country']}",
            "temp": f"{data['main']['temp']}°C (Feels like {data['main']['feels_like']}°C)",
            "desc": data['weather'][0]['description'].title(),
            "humidity": f"{data['main']['humidity']}%",
            "wind": f"{data['wind']['speed']} m/s",
            "pressure": f"{data['main']['pressure']} hPa"
        }
        return weather
    elif response.status_code == 404:
        return "City not found"
    elif response.status_code == 401:
        return "Invalid API Key"
    else:
        return "Something went wrong"

# 🔵 Streamlit GUI Part
st.set_page_config(page_title="Weather App", page_icon="🌦️")
st.title("🌦️ Weather Forecast App")

city = st.text_input("🏙️ Enter city name")  # Only city is asked!

if st.button("Get Weather"):
    if not city:
        st.warning("Please enter a city name.")
    else:
        result = get_weather(city)
        if isinstance(result, dict):
            st.success("✅ Weather Data Fetched Successfully!")
            st.write("📍 **Location:**", result['location'])
            st.write("🌡️ **Temperature:**", result['temp'])
            st.write("🌥️ **Condition:**", result['desc'])
            st.write("💧 **Humidity:**", result['humidity'])
            st.write("🌬️ **Wind Speed:**", result['wind'])
            st.write("📊 **Pressure:**", result['pressure'])
        else:
            st.error(f"❌ {result}")
