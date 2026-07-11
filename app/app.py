import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Road Accident Severity Analyzer",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Road Accident Severity and Safety Hotspot Analyzer")

st.write("""
This application predicts the severity of a road accident
based on accident-related information.
""")

model = joblib.load("../models/random_forest_model.pkl")

weather = st.selectbox(
    "Weather Condition",
    [
        "Normal",
        "Raining",
        "Fog",
        "Cloudy"
    ]
)

if st.button("Predict Severity"):
    st.success("Prediction Completed")

input_data = [[
    weather_encoded,
    road_surface_encoded,
    light_condition_encoded,
    driver_age_encoded,
    vehicle_type_encoded,
    driving_experience_encoded,
    cause_encoded
]]
prediction = model.predict(input_data)


st.subheader("Prediction")
st.write(prediction)

severity_labels = {
    0: "Fatal Injury",
    1: "Serious Injury",
    2: "Slight Injury"
}
st.success(f"Predicted Severity: {severity_labels[prediction[0]]}")


if prediction[0] == 0:

    st.error("High Risk")
    st.write("Reduce speed and increase road monitoring.")

elif prediction[0] == 1:

    st.warning("Moderate Risk")
    st.write("Drive carefully and follow traffic rules.")

else:

    st.success("Lower Risk")
    st.write("Continue following safe driving practices.")


    st.sidebar.title("Project Information")

st.sidebar.write("""
Road Accident Severity Prediction

Developed using:

- Python
- Streamlit
- Scikit-learn
- Random Forest
""")