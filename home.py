import streamlit as st
from PIL import Image

def app():
        st.title("Queso Arequipeños")
        st.header('Información', divider=True)
        with st.container():
                st.subheader("Descripción", divider=True)
                st.text("""
                        Los quesos arequipeños son muy populares en Perú. Estos quesos se caracterizan por 
                        tener un sabor fuerte y salado, con una textura firme y granulada. El queso 
                        arequipeño es elaborado con leche de vaca y se cura durante un período de 
                        tiempo que puede variar entre 3 y 12 meses, lo que le da su sabor distintivo. 
                        El queso arequipeño es muy versátil y se puede utilizar en una variedad de platos, 
                        desde sándwiches hasta ensaladas y platos principales. 
                        """)
                imagen = Image.open('img/queso.jpg')
                st.image(imagen, caption='Queso Arequipeño')
                st.subheader("Precio", divider=True)
                st.markdown("El precio esta entre **20** y **25** dependiendo del peso :bell:")


        st.header('Producto', divider=True)
        with st.container():
                #Definimos columnas
                col1, col2, col3 = st.columns(3)
                with col1:
                        st.header("Tipo A")
                        st.image(Image.open("img/queso.jpg"), caption="Queso1")
                with col2:
                        st.header("Tipo B")
                        st.image(Image.open("img/queso1.jpg"), caption="Queso2")
                with col3:
                        st.header("Tipo C")
                        st.image(Image.open("img/queso2.jpg"), caption="Queso3")