# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:16:33 2022

@author: jahop_fz60h0
"""


import json
#import pathlib 
#import shutil
import streamlit as st
import streamlit.components.v1 as components

from streamlit_player import st_player

from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import requests  # pip install requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    



lottie_hello = load_lottieurl("https://assets6.lottiefiles.com/datafiles/dfaiWZ3E8y0S6sz/data.json")




st_lottie(lottie_hello, key = "hello")


st.title("jahoperi Chusconoticias-Episodio #2")
st.subheader(" ")

st.subheader("Mejores frases de nuestro PRESIDENTE DE LOS ESTADOS UNIDOS MEXICANOS, Lic. AMLO ------- vs ----- Mejores frases de quien fuera presidente, EPN")

st.subheader(" ")

st_player("https://www.youtube.com/watch?v=Lk7I5Qqo95U")


st.subheader("Frases de AMLO")
st.subheader("Me canso ganso")
st.subheader(" ")
st.subheader("Que se porten bien, porque hacen sufrir mucho a sus mamás")
st.subheader(" ")
st.subheader("Al carajo la delincuencia, fuchi, guácala")
st.subheader(" ")
st.subheader("Los voy acusar con sus: mamás, papás...abuelos")
st.subheader(" ")
st.subheader("Ríndanse, los tenemos rodeados")
st.subheader(" ")
st.subheader("Irse a la Palenque (la Chingada), ya está permitido por la Real Academia Española")
st.subheader(" ")
st.subheader("Pañuelito blanco")

st.subheader(" ")
st.subheader(" ")

st.subheader("Frases de EPN")
st.subheader("burrada, tras burrada y más burradas")

st_player("https://www.youtube.com/watch?v=llqa00fwLmE")

st.subheader(" ")
st.subheader(" ")
st.subheader("jahoperi@gmail.com")


###########################################################################################################


    



