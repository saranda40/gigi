import streamlit as st
from streamlit_option_menu import option_menu
from st_social_media_links import SocialMediaIcons
import sqlite3 
from sqlite3 import Error

# Conectar a la base de datos SQLite (o crearla si no existe)
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        st.error(e)
    return conn

# Crear tabla pedidos
def create_table(conn):
    try:
        sql_create_pedidos_table = """ CREATE TABLE IF NOT EXISTS pedidos (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            nombre TEXT NOT NULL,
                                            email TEXT NOT NULL,
                                            fecha DATE NOT NULL,
                                            tipo_retiro INTEGER NOT NULL,
                                            tipo_ramo INTEGER NOT NULL,
                                            colores INTEGER NOT NULL,
                                            notas TEXT
                                        ); """
        sql_create_colores_table = """ 
        CREATE TABLE IF NOT EXISTS colores (
            id_color INTEGER PRIMARY KEY AUTOINCREMENT,
            colores TEXT NOT NULL
        ); """

        cursor = conn.cursor()
        cursor.execute(sql_create_pedidos_table)
        cursor.execute(sql_create_colores_table)
    except Error as e:
        st.error(e)

# Insertar un nuevo pedido en la tabla
def insert_pedido(conn, pedido):
    sql = ''' INSERT INTO pedidos(nombre, email, fecha, tipo_retiro, tipo_ramo, colores, notas)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pedido)
    conn.commit()
    return cur.lastrowid

# Ruta de la base de datos
database = "./pedidos.db"

# Crear conexión a la base de datos
conn = create_connection(database)

# Crear tabla si no existe
if conn is not None:
    create_table(conn)
else:
    st.error("Error! No se puede conectar a la base de datos.")

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

st.image('./assets/flor.jpeg','Flores Eternas Gigi')
st.title('Flores Eternas GIGI')
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
    social_media_links = ["https://www.instagram.com/m._floreseternas/"]
    colors = [None]
    social_media_icons = SocialMediaIcons(social_media_links, colors)
    social_media_icons.render(sidebar=False)
    


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
     st.subheader("Pedidos" ,divider='rainbow')

     c1, c2 = st.columns(2)

     nombre = c1.text_input("Nombre")
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
             
              pedido = (nombre, email, fecha, tipo_retiro, tipo_ramo, colores, notas)
        
                # Insertar pedido en la base de datos
              if conn is not None:
                    pedido_id = insert_pedido(conn, pedido)
                    if pedido_id:
                        st.success("Su pedido ha sido registrado, pronto nos comunicaremos con Usted. Atte Gigi Team", icon=":material/check:")
                    else:
                        st.error("Hubo un error al registrar su pedido. Inténtelo de nuevo.")
              else:
                    st.error("No se pudo conectar a la base de datos.")

