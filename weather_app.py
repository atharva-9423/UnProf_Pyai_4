import requests
import logging

API_KEY  = "0b9042dcc2a0afd3e6e6e5f4ee69f3e9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
LOG_FILE = "weather.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class CityNotFoundError(Exception):
    pass


class APIKeyError(Exception):
    pass


class NetworkError(Exception):
    pass


def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        logging.debug(f"API response status for '{city}': {response.status_code}")

        if response.status_code == 404:
            raise CityNotFoundError(f"City '{city}' not found. Please check the spelling.")
        elif response.status_code == 401:
            raise APIKeyError("Invalid API key. Please check your API key and try again.")
        elif response.status_code != 200:
            raise NetworkError(f"Unexpected error from API. Status code: {response.status_code}")

        data = response.json()
        logging.info(f"Weather data fetched successfully for '{city}'.")
        return data

    except requests.exceptions.ConnectionError:
        raise NetworkError("No internet connection. Please check your network.")
    except requests.exceptions.Timeout:
        raise NetworkError("Request timed out. The server took too long to respond.")


def display_weather(data, city):
    name        = data["name"]
    country     = data["sys"]["country"]
    condition   = data["weather"][0]["description"].title()
    temp        = data["main"]["temp"]
    feels_like  = data["main"]["feels_like"]
    temp_min    = data["main"]["temp_min"]
    temp_max    = data["main"]["temp_max"]
    humidity    = data["main"]["humidity"]
    wind_speed  = data["wind"]["speed"]
    visibility  = data.get("visibility", "N/A")

    if visibility != "N/A":
        visibility = f"{visibility / 1000:.1f} km"

    print("\n" + "=" * 40)
    print(f"  🌍 Weather Report: {name}, {country}")
    print("=" * 40)
    print(f"  🌤️  Condition    : {condition}")
    print(f"  🌡️  Temperature  : {temp}°C  (Feels like {feels_like}°C)")
    print(f"  🔼  Max / Min    : {temp_max}°C  /  {temp_min}°C")
    print(f"  💧 Humidity     : {humidity}%")
    print(f"  💨 Wind Speed   : {wind_speed} m/s")
    print(f"  👁️  Visibility   : {visibility}")
    print("=" * 40)


def main():
    logging.info("===== Weather CLI Application Started =====")
    print("🌤️  Weather CLI Application")
    print("Type 'exit' at any time to quit.\n")

    while True:
        try:
            city = input("Enter city name: ").strip()

            if not city:
                print("❌ City name cannot be empty.")
                continue

            if city.lower() == "exit":
                print("✅ Goodbye!")
                logging.info("===== Weather CLI Application Exited =====")
                break

            data = fetch_weather(city)
            display_weather(data, city)
            logging.info(f"Displayed weather for '{city}'.")

        except CityNotFoundError as e:
            logging.warning(str(e))
            print(f"⚠️  {e}")

        except APIKeyError as e:
            logging.error(str(e))
            print(f"❌ {e}")
            break

        except NetworkError as e:
            logging.error(str(e))
            print(f"❌ {e}")

        except KeyboardInterrupt:
            logging.warning("Program interrupted by user.")
            print("\n\n⚠️  Interrupted. Goodbye!")
            break


if __name__ == "__main__":
    main()
    
