# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:16:33 2022

@author: jahop_fz60h0
"""


import json
import pathlib 
import shutil
import streamlit as st
import streamlit.components.v1 as components

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

st.subheader("Mejores frases de nuestro PRESIDENTE DE LOS ESTADOS UNIDOS MEXICANOS, Lic. AMLO")

st.subheader(" ")


# HACK This only works when we've installed streamlit with pipenv, so the
# permissions during install are the same as the running process
STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
# We create a videos directory within the streamlit static asset directory
# and we write output files to it
VIDEOS_PATH = (STREAMLIT_STATIC_PATH / "videos")
if not VIDEOS_PATH.is_dir():
    VIDEOS_PATH.mkdir()

uno_video = VIDEOS_PATH / "amlo.mp4"
if not uno_video.exists():
    shutil.copy("amlo.mp4", uno_video)  # For newer Python.



st.subheader('')

def main_0():
    components.html("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
.main-div h1
{
 font-size: 21px;
}


#color1{color:red;}
#color2{color:blue;}
#color3{color:pink;}
</style>

  </head>
  
   <div class="main-div">
    <video src = "videos/amlo.mp4" width="500" height="400" controls controlsList="nodownload"></video>
    <p></p>
    <video src = "videos/epn.mp4" width="500" height="400" controls controlsList="nodownload"></video>
    <p> </p>
    <H1><FONT COLOR="red">Mejores frases de quien fuera presidente, EPN</FONT></H1>
    <p> </p>
    <p> </p>
    <H1><FONT COLOR="navy">burrada, tras burrada y más burrada</FONT></H1>
<script type="text/javascript">
//Script for disabling right click on mouse
var message="Function Disabled!";
function clickdsb(){
if (event.button==2){
alert(message);
return false;
}
}
function clickbsb(e){
if (document.layers||document.getElementById&&!document.all){
if (e.which==2||e.which==3){
alert(message);
return false;
}
}
}
if (document.layers){
document.captureEvents(Event.MOUSEDOWN);
document.onmousedown=clickbsb;
}
else if (document.all&&!document.getElementById){
document.onmousedown=clickdsb;
}
document.oncontextmenu=new Function("alert(message);return false")
</script>

</div>


</html>""", width=1300, height=2200)


#########################################################################################################

st.header("Resumen")
st.header("")
st.header("Frases de AMLO")
st.header("Me canso ganso")
st.header("")
st.header("Que se porten bien, porque hacen sufrir mucho a sus mamás")
st.header("")
st.header("Al CARAJO, la delincuencia, fuchi, guácala")
st.header("")
st.header("Los voy acusar con sus: mamás, papás...abuelos")
st.header("Ríndanse, los tenemos rodeados")
st.header("")
st.header("Irse a la Palenque (a la chingada), ya está permitido por la Real Academia Española")
st.header("Pañuelito blanco")
st.header("")



###########################################################################################################

if __name__ == "__main__":
    main_0()
    
