import time

import streamlit as st
import pandas as pd
import requests


# Constants
API_URL = "http://localhost:8000"


def get_prediction(endpoint, data):
    """Send a POST request to the API and return the response."""
    try:
        response = requests.post(f"{API_URL}/{endpoint}/", json=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        st.write("An Http Error occurred:", errh)
    except requests.exceptions.ConnectionError as errc:
        st.write("An Error Connecting to the API occurred:", errc)
    except requests.exceptions.Timeout as errt:
        st.write("A Timeout Error occurred:", errt)
    except requests.exceptions.RequestException as err:
        st.write("An Unknown Error occurred", err)
    else:
        return response.json()


def get_prediction_result():
    """Send a GET request to the API and return the response."""
    try:
        response = requests.get(f"{API_URL}/result/")
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        st.write("An Http Error occurred:", errh)
    except requests.exceptions.ConnectionError as errc:
        st.write("An Error Connecting to the API occurred:", errc)
    except requests.exceptions.Timeout as errt:
        st.write("A Timeout Error occurred:", errt)
    except requests.exceptions.RequestException as err:
        st.write("An Unknown Error occurred", err)
    else:
        return response.text


def display_prediction(prediction):
    """Display the prediction result."""
    if prediction and 'prediction' in prediction:
        st.write("La prediction est : ", prediction['prediction'])
    else:
        st.write("Une erreur s'est produite lors de la récupération de la prédiction.")


def main():
    """Main function to run the Streamlit interface."""
    st.title("API de prediction")
    st.write("Bienvenue sur l'API de prediction")
    model = st.selectbox("Choisir le model", ["Model 1", "Model 2"])

    if model == "Model 1":
        st.write("Vous avez choisi le Model 1")
        data = {
            'Gender': st.selectbox('quel est votre genre ? selectionner 0 pour un homme ou 1 pour une femme ',
                                   ('0', '1'), index=None, placeholder="Selectionner votre genre ..."),
            'Age': st.number_input('Age', min_value=0, max_value=100, value=20),
            'PhysicalActivityLevel': st.number_input('PhysicalActivityLevel', min_value=0, max_value=100, value=20),
            'HeartRate': st.number_input('HeartRate', min_value=0, max_value=100, value=20),
            'DailySteps': st.number_input('DailySteps', min_value=0, max_value=100, value=20),
            'BloodPressure_high': st.number_input('BloodPressure_high', min_value=0, max_value=100, value=20),
            'BloodPressure_low': st.number_input('BloodPressure_low', min_value=0, max_value=100, value=20),
            'SleepDisorder': st.number_input('SleepDisorder', min_value=0, max_value=100, value=0)
        }
        endpoint = "predict"
    else:
        st.write("Vous avez choisi le Model 2")
        data = {
            'PhysicalActivityLevel': st.number_input('PhysicalActivityLevel', min_value=0, max_value=100, value=20),
            'HeartRate': st.number_input('HeartRate', min_value=0, max_value=100, value=20),
            'DailySteps': st.number_input('DailySteps', min_value=0, max_value=100, value=20),
            'SleepDisorder': st.number_input('sleepDisorder', min_value=0, max_value=100, value=0)
        }
        endpoint = "predict2"

    st.write(data)
    if st.button("Predict"):
        prediction = get_prediction(endpoint, data)
        display_prediction(prediction)

    if st.button("Get Prediction Result"):
        with st.spinner("Loading..."):
            time.sleep(5)
        st.success("Done!")
        prediction_result = get_prediction_result()
        prediction_list = prediction_result.split(str() + '\n')
        st.table(prediction_list)

        if st.download_button(
                label="Télécharger les prédictions du modèle 1",
                data=prediction_result,
                file_name='predictions-model.txt',
                mime='text/plain',
        ):
            st.write("Merci d'avoir utilisé l'API de prediction")
        st.balloons()


if __name__ == "__main__":
    main()
