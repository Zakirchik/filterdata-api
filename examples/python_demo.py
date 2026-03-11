import requests


def main() -> None:
    url = "https://filterdata.ru/demo/normalize"
    payload = {
        "phone": "8 (999) 123-45-67",
        "name": "иван иванов",
        "email": "user@agmil.com",
    }

    r = requests.post(url, json=payload, timeout=10)
    r.raise_for_status()
    print(r.json())


if __name__ == "__main__":
    main()

