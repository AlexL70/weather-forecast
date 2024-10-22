import os
import json
import requests as rq

API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")


class DataKey:
    DK_TEMPERATURE = "Temperature"
    DK_SKY = "Sky"


def get_data(place: str) -> tuple[bool, dict]:
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    response: rq.Response = rq.get(url)
    content = response.json()
    if not response.ok:
        return False, content
    return True, content


if __name__ == "__main__":
    print(get_data("London", 3, "Temperature"))
