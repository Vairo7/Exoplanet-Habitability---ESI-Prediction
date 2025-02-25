import streamlit as st
import requests
import pandas as pd

url = "http://127.0.0.1:5000/ayy"

st.set_page_config(layout='wide')
st.header('Welcome, Fellow Star Explorer!')
st.subheader('--- Predict ESI of Exoplanets ---')
col1, col2 =st.columns(2)
with col1:
    with st.expander('For reference'):
        earth = [1, 1, 1, 1, 0]
        venus = [0.949, 0.72, 1, 1, 0]
        mars = [0.532, 1.52, 1, 1, 0]
        jupiter = [11.2, 5.2, 1, 1, 0]
        score_test = pd.DataFrame([earth, venus, mars, jupiter], columns=['P_RADIUS','P_SEMI_MAJOR_AXIS','S_MASS','S_RADIUS','S_LOG_LUM'],index = ['earth','venus','mars','jupiter'])
        st.dataframe(score_test)

col1, col2, col3 = st.columns(3)
with col1:
    p_radius = st.number_input('Planet Radius', min_value= 0.0, format='%.5f')
with col2:
    p_semi_major_axis = st.number_input('Semi Major Axis', min_value=0.0, format = '%.5f') 
col1, col2, col3 = st.columns(3)
with col1:
    s_mass = st.number_input('Mass of Star', min_value= 0.0, format = '%.5f')
with col2:
    s_radius = st.number_input('Radius of Star', min_value=0.0, format = '%.5f')
with col3:
    s_lum = st.number_input('Luminosity of Star', format = '%.5f')

if st.button('Predict ESI :D'):
    if p_radius == 0 or p_semi_major_axis == 0 or s_mass == 0 or s_radius == 0:
        st.warning('Please Enter Valid Values :)')
    else:
        planet = {'features':
                    [
                    p_radius,
                    p_semi_major_axis,
                    s_mass,
                    s_radius,
                    s_lum
                    ]}
        response = requests.post(url, json = planet)
        score = response.json().get('ESI_Score','Error')
        st.write(f"ESI Score: {score:.6f}")

