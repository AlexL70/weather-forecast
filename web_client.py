import os
import json
import requests as rq

API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")


class DataKey:
    DK_TEMPERATURE = "Temperature"
    DK_SKY = "Sky"


def get_data(place: str, forcast_days: int = 1, kind: str | None = None) -> tuple[bool, dict]:
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    response: rq.Response = rq.get(url)
    content = response.json()
    if not response.ok:
        return False, content
    print(len(content['list']))
    filtered = content["list"][:forcast_days*8]
    match kind:
        case DataKey.DK_TEMPERATURE:
            filtered = [{"date": item["dt_txt"],
                         "temperature": item["main"]["temp"]} for item in filtered]
        case DataKey.DK_SKY:
            filtered = [{"date": item["dt_txt"],
                         "sky": item["weather"][0]["main"]} for item in filtered]
        case _:
            return False, {"message": f"Invalid data key: {kind}"}
    print(filtered)
    print(len(filtered))
    return True, filtered


if __name__ == "__main__":
    print(get_data("London", 3, "Temperature"))
