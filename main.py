import streamlit as st
import plotly.express as px
from web_client import get_data, DataKey


st.title("Weather Forecast for the Next 5 Days")
place = st.text_input("Place:", placeholder="The name of the place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 value=2, help="Select the number of forecasted days")
option = st.selectbox("Select data to view:",
                      (DataKey.DK_TEMPERATURE, DataKey.DK_SKY))

if len(place) > 0:
    if option == DataKey.DK_TEMPERATURE:
        st.subheader(f"Temperature for the next {days} days in {place}")
    else:
        st.subheader(f"Sky condition for the next {days} days in {place}")
    success, data = get_data(place, days, option)
    if success:
        x_data = [item["date"] for item in data]
        match option:
            case DataKey.DK_TEMPERATURE:
                y_data = [item["temperature"] for item in data]
                label_y = "Temperature(C)"
                figure = px.line(x=x_data, y=y_data,
                                 labels={"x": "Date", "y": label_y})
                st.plotly_chart(figure)
            case DataKey.DK_SKY:
                y_data = [item["sky"] for item in data]
                label_y = "Sky"
                st.warning("The sky condition is under construction")

    else:
        st.error(data["message"])
