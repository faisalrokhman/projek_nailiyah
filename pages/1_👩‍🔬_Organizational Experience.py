import streamlit as st

st.set_page_config(
    page_title="Organizational Experience|Nailiyah",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("Organizational Experience")
st.write("Beberapa Organisasi Yang Pernah Saya Ikuti; ")

st.container()
col1, col2, col3,  = st.columns(3)
with col1:
    st.subheader("Forum Permusyawaratan Santri")
   
with col2:
    st.subheader("Ikatan Santri Intra Madrasah")
    
with col3:
    st.subheader("Team Readaksi Plural")
   

st.container()
st.write("---")
col1, col2, col3, = st.columns(3)
with col1:
   
    st.image("FPS.png", width= 190)
with col2:
   
    st.image("isim.png", width= 190)
with col3:
    
    st.image("plural.png", width= 190)

st.container()
st.write("---")
col1, col2, col3,  = st.columns(3)
with col1:
    st.subheader("*Menjabat Sebagai Pimpinan FPS Masa khidmat 2019 - 2020*")
   
with col2:
    st.subheader("*Menjabat Sebagai Dep. Kominfo th 2016 - 2017, Dep. Keuangan 2017 - 2018, Sekertaris jendral 2020*")
    
with col3:
    st.subheader("*Menjabat Sebagai Sekertaris Masa khidmat 2017 - 2019*")