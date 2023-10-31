import streamlit as st
import home
def app():
    st.title("Login")
    with st.form("login_form"):
        # Crear formulario
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        submit_button = st.form_submit_button(label="Iniciar sesión")

        # Verificar credenciales
        if submit_button:
            if username == "admin" and password == "123":
                st.success("Inicio de sesión exitoso.")
                # Redirigir a la página de inicio
            else:
                st.error("Credenciales incorrectas.")
