import streamlit as st

st.set_page_config(
    page_title="Portfolio|Nailiyah",
    page_icon="👩‍🎓",
    layout="wide"
)

st.title(" MY WELCOME TO PORTFOLIO  👩‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS.")

import streamlit as st

st.container()
col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("me.jpg", width= 390)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : NAILIYATUL AZIZAH")
   st.caption("NIM : 0402201077")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 01 April 2002 
            - Alamat : GG. Delima Sengon Tanjung Brebes
            - Hobi : Baca
            - Cita-cita : Jadi Orang Manfaat
            - Hal yang disukai : Eat
            - Status : Sudah Di Miliki
            """
        )

st.header("Call Me If You Want")
