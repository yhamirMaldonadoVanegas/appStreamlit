import streamlit as st
from streamlit_option_menu import option_menu

import admin, home

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function): 
        self.apps.append({
            "title":title,
            "function":function
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Menu",
                options=["Admin","Home"],
                icons=["person-circle","house"],
                menu_icon="cast",
                default_index=1,
            )

        if app == "Admin":
            admin.app()
        elif app == "Home":
            home.app()

    run()