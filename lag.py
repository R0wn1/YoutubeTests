import streamlit as st
import time

speed = st.slider("Speed", 0.0, 0.1, 0.01)

while True:
    st.write("you are a furry")
    time.sleep(speed)
            
