import streamlit as st
from streamlit_option_menu import option_menu

ramos = ["Una Flor", "Ramo 3 flores", "Ramo 5 flores","Ramo 10 flores", "Ramo 15 flores" ]
colores = ["Gris","Rojo","Verde","Multicolor"]
retiros = ["A Domicilio", "A Convenir"]

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

if selected == "Detalles":

    st.subheader("Modos de Pago :credit_card:", divider='rainbow')

    items = ['Eféctivo:', 'Transferencia', 'Galletitas :)']

    # Mostrar la lista usando st.write
    st.write('Lista de elementos:')
    for item in items:
        st.write(f'- {item}')

    st.subheader("Nos ubicas en :world_map:", divider='rainbow')

    st.image("assets/map.jpeg")
    st.markdown("Pulsa [aquí](https://www.google.cl/maps/@-33.6813142,-71.1954499,19.72z?entry=ttu) para ver la direccion")

    st.subheader("Horarios para despachos :motor_scooter:", divider='rainbow')
    dia, hora = st.columns(2)
    dia.text("Lunes")
    hora.text("8:30 a 16:15")
    dia.text("Martes")
    hora.text("8:30 a 16:15")
    dia.text("Miércoles")
    hora.text("8:30 a 13:45")
    dia.text("Jueves")
    hora.text("8:30 a 15:30")
    dia.text("Viernes")
    hora.text("8:30 a 14:15")

    st.subheader("Contacto :hibiscus:" ,divider='rainbow')
    st.caption(":telephone_receiver: +5691235468")

    st.subheader("Instagram :hibiscus:" ,divider='rainbow')
    st.link_button("Siguenos!", "https://www.instagram.com/m._floreseternas/")

if selected == "Imágenes":
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("assets/flor1.png", caption ="Foto Referencial")
    with col2:
        st.image("assets/flor2.jpeg", caption ="Foto Referencial")
    with col3:
        st.image("assets/flor3.jpeg", caption ="Foto Referencial")

if selected == "Reservar":
     st.subheader("Reservar" ,divider='rainbow')

     c1, c2 = st.columns(2)
     
     nombre = c1.text_input("Nombre", placeholder="Nombre")
     email = c2.text_input("Email")
     fecha = c1.date_input("Fecha")
     tipo_retiro = c2.selectbox("Tipo Retiro", retiros)
     tipo_ramo = c1.selectbox("Tipo Ramo", ramos)
     colores = c2.selectbox("Color", colores)
     notas = c1.text_area("Notas")

     enviar = st.button("Reservar")
     
     if enviar:
         if nombre =="":
             st.warning("Nombre es Obligatorio", icon=":material/warning:")
         elif email == "":
             st.warning("Email es Obligatorio", icon=":material/warning:")
         elif fecha == "":
             st.warning("Fecha es Obligatorio", icon=":material/warning:")
         elif tipo_retiro == "":
             st.warning("Retiro es Obligatorio", icon=":material/warning:")
         elif tipo_ramo == "":
             st.warning("Tipo Ramo es Obligatorio", icon=":material/warning:")
         elif colores == "":
             st.warning("Color del ramo es Obligatorio", icon=":material/warning:")
         else:
             st.success("Su pedido ha sido registrado, pronto nos comunicaremos con Usted. Atte Gigi Team",icon=":material/check:")

