from weather.business.fiveDay_weather import FiveDayWeather


def get_weather_5days(api_key: str, lat: float, lon: float, weather: FiveDayWeather):
    """
    Show the weather of a location on 5 days
    :param api_key: key of openweather api
    :param lat: latitude
    :param lon: longitude
    :param weather: instance of class FiveDayWeather
    """
    data = weather.get_five_day_weather(api_key, lat, lon)
    if data:
        name = data['city']['name']
        print(f"{name}")
        for forecast in data['list']:
            date = forecast['dt_txt']
            temp_min = forecast['main']['temp_min'] - 273.15
            temp_max = forecast['main']['temp_max'] - 273.15
            print(f"{date} - Température min: {temp_min:.1f}, Température max: {temp_max:.1f}")
    else:
        print('Erreur avec la requête API')


def valid_integer(prompt: str, min_int: int, max_int: int) -> int:
    """
    Verify if the user enter the right entry
    :param prompt: question to the user
    :param min_int: value minimum
    :param max_int: value maximum
    :return:
    """
    valid_number: bool = False
    number: int = 0

    print(prompt)
    while not valid_number:
        number_str: str = input().strip()
        if number_str.isdigit():
            number = int(number_str)
            valid_number = (min_int <= number <= max_int)
            if not valid_number:
                print(f"Merci de saisir un nombre entier compris entre {min_int} et {max_int}")
        else:
            print("Merci de saisir un nombre entier positif !")

    return number


def main_menu():
    """Display main menu and ask user to choose an action"""
    api_key = '839e140902042b7e9b60ee41fc9f4940'
    is_continue = True
    enter_key_str = "Saisir la touche Entrée pour continuer"
    while is_continue:
        print("""\
        ------------------------------
        Prévisions météo de la semaine
        ------------------------------""")

        print("[1] - Afficher les prévisions météo de Toulouse sur 5 jours")
        print("[2] - Afficher les prévisions météo de St-Geours de Marenne sur 5 jours")
        print("[3] - Quitter l'application")

        user_choice: int = valid_integer("Que souhaitez-vous faire?", 1, 6)
        match user_choice:
            case 1:
                toulouse_lat = 43.6
                toulouse_lon = 1.433333
                five_day_weather = FiveDayWeather()
                get_weather_5days(api_key, toulouse_lat, toulouse_lon, five_day_weather)
                input(enter_key_str)
            case 2:
                st_geours_lat = 43.683331
                st_geours_lon = -1.23333
                five_day_weather = FiveDayWeather()
                get_weather_5days(api_key, st_geours_lat, st_geours_lon, five_day_weather)
                input(enter_key_str)
            case 3:
                is_continue = False
                exit()


def main():
    """
    Main program
    """
    main_menu()


if __name__ == '__main__':
    main()
