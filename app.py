import streamlit as st
from streamlit_option_menu import option_menu

page_title="Flores Eternas Gigi"
page_icon="🎉"
layout="centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

# Define CSS styles
with open('./assets/css/styles.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.image('./assets/flor.jpeg','Flores Eternas Gigi',width=200)
st.title('Flores Eternas Gigi')
st.text('Venta de Flores eternas individuales y por Ramos, con todo el amor del mundo')

selected = option_menu(menu_title=None,options=["Reservar","Imágenes","Detalles"],icons=["bookmark","bi-flower1","bi-ticket-detailed"],orientation="horizontal")
