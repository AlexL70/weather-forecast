import streamlit as st
import plotly.express as px
from web_client import get_data, DataKey


class SkyKeys:
    SKY_CLEAR = "Clear"
    SKY_CLOUDS = "Clouds"
    SKY_RAIN = "Rain"
    SKY_SNOW = "Snow"


sky_dict = {
    SkyKeys.SKY_CLEAR: "images/clear.png",
    SkyKeys.SKY_CLOUDS: "images/cloud.png",
    SkyKeys.SKY_RAIN: "images/rain.png",
    SkyKeys.SKY_SNOW: "images/snow.png"
}

st.title("Weather Forecast for the Next 5 Days")
place = st.text_input("Place:", placeholder="The name of the place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 value=2, help="Select the number of forecasted days")
option = st.selectbox("Select data to view:",
                      (DataKey.DK_TEMPERATURE, DataKey.DK_SKY))

if place:
    if option == DataKey.DK_TEMPERATURE:
        st.subheader(f"Temperature for the next {days} days in {place}")
    else:
        st.subheader(f"Sky condition for the next {days} days in {place}")
    success, data = get_data(place)
    if success:
        filtered = data["list"][:days*8]
        match option:
            case DataKey.DK_TEMPERATURE:
                filtered = [{"date": item["dt_txt"],
                             "temperature": item["main"]["temp"]} for item in filtered]
                date_data = [item["date"] for item in filtered]
                sky_data = [item["temperature"] for item in filtered]
                label_y = "Temperature(C)"
                figure = px.line(x=date_data, y=sky_data,
                                 labels={"x": "Date", "y": label_y})
                st.plotly_chart(figure)
            case DataKey.DK_SKY:
                filtered = [{"date": item["dt_txt"],
                             "sky": item["weather"][0]["main"]} for item in filtered]
                date_data = [item["date"] for item in filtered]
                sky_data = [sky_dict[item["sky"]] for item in filtered]
                label_y = "Sky"
                col1, col2, col3, col4 = st.columns(4)
                for index in range(0, len(sky_data), 4):
                    with col1:
                        st.image(sky_data[index],
                                 caption=date_data[index], width=120)
                    with col2:
                        st.image(sky_data[index+1],
                                 caption=date_data[index+1], width=120)
                    with col3:
                        st.image(sky_data[index+2],
                                 caption=date_data[index+2], width=120)
                    with col4:
                        st.image(sky_data[index+3],
                                 caption=date_data[index+3], width=120)

    else:
        st.error(data["message"])
