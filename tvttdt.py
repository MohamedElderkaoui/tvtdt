import streamlit as st
import requests
import json

# URL con la lista de canales
URL = 'https://www.tdtchannels.com/lists/tv.json'
res = requests.get(URL)
data = res.json()

def obtener_datos(URL):
    res = requests.get(URL)
    data = res.json()
    return data
# guardar json
# with open('tdt.json', 'w') as f:
#     json.dump(data, f)

def country(data):
    [c['name '] for c in data['countries']]

st.title("TDT")

st.bhc