import requests


class FiveDayWeather:

    @staticmethod
    def get_five_day_weather(api_key: str, lat: float, lon: float):
        """
        Show the weather of a location on 5 days
        :param api_key: key of api OpenWeather
        :param lat: latitude
        :param lon: longitude
        :return: weather
        """
        api_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                weather = response.json()
                return weather
            else:
                print('There is a problem with API, error ', response.status_code)
                return None
        except requests.exceptions.RequestException as e:
            print('Error ', e)
            return None
