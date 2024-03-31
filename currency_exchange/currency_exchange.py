import requests

# Кеш для збереження обмінних курсів
cache = {}


def get_exchange_rate(currency_code):
    if currency_code in cache:
        print("Checking the cache...")
        return cache[currency_code]
    else:
        print("Sorry, but it is not in the cache!")
        url = f"http://www.floatrates.com/daily/{currency_code}.json"
        response = requests.get(url)
        data = response.json()
        cache[currency_code] = data
        return data


def currency_exchange():
    while True:
        # Зчитуємо код валюти, яку маємо, та код валюти, на яку хочемо обміняти
        from_currency = input("Please, enter the currency code you have (or leave empty to exit): ").upper()
        if not from_currency:
            break
        to_currency = input("Please, enter the currency code you want to exchange to: ").upper()

        # Зчитуємо суму грошей для обміну
        amount = float(input("Please, enter the amount of money you want to exchange: "))

        # Отримуємо обмінний курс для поточних валют
        exchange_rate_data = get_exchange_rate(from_currency)

        # Обчислюємо результат обміну
        exchange_rate = exchange_rate_data[to_currency]['rate']
        exchanged_amount = amount * exchange_rate

        # Виводимо результат
        print(f"You received {round(exchanged_amount, 2)} {to_currency}.")


if __name__ == "__main__":
    currency_exchange()
