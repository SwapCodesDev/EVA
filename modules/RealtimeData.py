from datetime import datetime
import pytz

def get_time_by_city(city_timezone):
    try:
        # Get the timezone object for the city
        timezone = pytz.timezone(city_timezone)
        
        # Get current time in the specified timezone
        city_time = datetime.now(timezone)
        
        # Extract components
        return {
            "year": city_time.year,
            "month": city_time.month,
            "day": city_time.day,
            "hour": city_time.hour,
            "minute": city_time.minute,
            "second": city_time.second,
        }
    except pytz.UnknownTimeZoneError:
        print(f"Error: '{city_timezone}' is not a valid timezone.")
        return None


def get_timezones():
    timezones = pytz.all_timezones
    return sorted(timezones)