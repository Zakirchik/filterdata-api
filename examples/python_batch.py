import os
import sys

import requests


def main() -> None:
    api_key = os.getenv("FILTERDATA_API_KEY") or os.getenv("API_KEY")
    if not api_key:
        print("Missing API key. Set env var FILTERDATA_API_KEY (or API_KEY).", file=sys.stderr)
        sys.exit(2)

    url = "https://filterdata.ru/api/v1/batch"
    payload = {
        "contacts": [
            {"phone": "8 (999) 123-45-67", "name": "иван иванов", "email": "EXAMPLE@gmail.com"},
            {"phone": "+7 912 000-00-00", "name": "Иванov", "email": "user@agmil.com"},
        ]
    }

    r = requests.post(
        url,
        json=payload,
        headers={"X-API-Key": api_key},
        timeout=30,
    )
    r.raise_for_status()
    print(r.json())


if __name__ == "__main__":
    main()
