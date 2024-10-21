import streamlit as st


class DataKey:
    DK_TEMPERATURE = "Temperature"
    DK_SKY = "Sky"


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
