import requests

API_URL = 'https://www.cbr-xml-daily.ru/latest.js'
currencies: dict = {}


def get_currencies_from_file(filename: str) -> dict:
    print(f"read file {filename}")
    currs: dict[str, float] = {}
    with open(filename) as curs:
        for line in curs:
            code, value = line.split(" ", maxsplit=1)
            currs[code] = float(value)
    return currs


def get_currencies_from_api() -> dict:
    currs: dict = {}
    res = requests.get(API_URL)

    if res.status_code == 200:
        json = res.json()
        for rate in json['rates']:
            currs[rate] = float(json['rates'][rate])
    if len(currs) > 0:
        write_currencies_to_file(currs)

    return currs


def write_currencies_to_file(rates: dict):
    try:
        with open("currencies.txt", "w") as curs_w:
            for code in rates:
                curs_w.write(f"{code} {rates[code]}\n")
    except PermissionError:
        print("Access denied. Can't write to file")


def to_rub(value: float, code: str, currencies: dict) -> float:
    if code in currencies.keys():
        return value / currencies[code]
    else:
        return 0


def from_rub(value: float, code: str, currencies: dict) -> float:
    if code in currencies.keys():
        return value * currencies[code]
    else:
        return 0


def calc_result(query: str, currencies: dict) -> str:
    value, codes = query.split(" ", maxsplit=1)
    value = float(value)
    from_code, to_code = codes.split(">", maxsplit=1)
    from_code = from_code.strip().upper()
    to_code = to_code.strip().upper()

    if from_code != "RUB":
        rub_value = to_rub(value, from_code, currencies)
    else:
        rub_value = value

    if to_code != "RUB":
        res_value = from_rub(rub_value, to_code, currencies)
    else:
        res_value = rub_value

    return f"Result: {value:_.2f} {from_code} = {res_value:_.2f} {to_code}".replace("_", " ")


if __name__ == '__main__':

    try:
        currencies = get_currencies_from_file("currencies.txt")
    except FileNotFoundError:
        currencies = get_currencies_from_api()

    if len(currencies) > 0:
        i = 0
        for code in currencies:
            print(f"{code}: {currencies[code]:9.4f}", end="  |  ")
            i += 1
            if i == 4:
                i = 0
                print("")
        print("\n")

        while True:
            print("Query format: 100 USD>RUB")
            query = input("Input your query: ")
            if query.strip() == "" or query.strip() == "0":
                break
            print(calc_result(query, currencies), "\n")
