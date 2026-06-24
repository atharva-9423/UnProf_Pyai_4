# UnProf_Pyai_4

<div align="center">

# 🌤️ Weather CLI Application

A Python terminal app that fetches **real-time weather data** for any city in the world.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Atharva%20Phatangare-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/atharva-phatangare)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![API](https://img.shields.io/badge/API-OpenWeatherMap-orange?style=for-the-badge)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌍 Real-time Weather | Live data fetched from OpenWeatherMap API |
| 🌡️ Full Details | Temperature, humidity, wind speed & visibility |
| 🔍 Any City | Supports 200,000+ cities worldwide |
| ❌ Error Handling | Invalid cities and network errors handled gracefully |
| 📋 Logging | All events and errors logged to `weather.log` |

---

## 📺 Example Output

```
Enter city name: Mumbai

========================================
  🌍 Weather Report: Mumbai, IN
========================================
  🌤️  Condition    : Haze
  🌡️  Temperature  : 32.4°C  (Feels like 38.1°C)
  🔼  Max / Min    : 33.0°C  /  31.2°C
  💧 Humidity     : 74%
  💨 Wind Speed   : 4.1 m/s
  👁️  Visibility   : 3.0 km
========================================
```

---

## 🚀 How To Run

**Step 1** — Install the required library:
```bash
pip install requests
```

**Step 2** — Get a free API key from [openweathermap.org](https://openweathermap.org/api)

**Step 3** — Paste your API key in `weather_app.py`:
```python
API_KEY = "your_api_key_here"
```

**Step 4** — Run the app:
```bash
python3 weather_app.py
```

---

## 📁 Project Structure

```
📂 Project Folder
├── weather_app.py   ← Main application
├── weather.log      ← Auto-generated log file
└── README.md        ← This file
```

---

## 🎓 What I Learned

Built as part of **Day 4 of my Python & AI Internship**, covering:

- Making GET requests using the `requests` library
- Parsing JSON responses from a real public API
- Handling API errors (invalid city, bad key, timeout)
- Custom exceptions & logging (applied from Day 3)

---

<div align="center">

Made with ❤️ by **Atharva Phatangare**

[![LinkedIn](https://img.shields.io/badge/Let's%20Connect-LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/atharva-phatangare)

</div>
