import streamlit as st 
from PIL import Image

st.title("Mi Primera Aplicación")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para inferfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")
image = Image.open("Interfaces Mult2.png")

st.image(image, caption="Interfaces Multimodales")
