import os
import requests


def main() -> None:
    api_key = os.getenv("FILTERDATA_API_KEY") or os.getenv("API_KEY")

    if api_key:
        url = "https://filterdata.ru/api/v1/normalize"
        headers = {"X-API-Key": api_key}
        payload = {"phone": "8 (999) 123-45-67", "name": "Иванov", "email": "EXAMPLE@gmail.com"}
    else:
        url = "https://filterdata.ru/demo/normalize"
        headers = {}
        payload = {"phone": "8 (999) 123-45-67", "name": "иван иванов", "email": "user@agmil.com"}

    r = requests.post(url, json=payload, headers=headers, timeout=10)
    r.raise_for_status()
    print(r.json())


if __name__ == "__main__":
    main()

