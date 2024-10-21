import os
import json
import requests as rq

API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")


def get_data(place: str) -> tuple[bool, dict]:
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response: rq.Response = rq.get(url)
    content = response.json()
    if response.ok:
        return True, content
    return False, content


if __name__ == "__main__":
    print(get_data("London", 5, "Temperature"))
