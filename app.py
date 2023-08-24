import streamlit as st 
from PIL import Image

st.title("Mi Primera Aplicación")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para inferfaces multimodales")
st.write("Facilmente puedo realizar backend y frontend")

# IMAGENES
image = Image.open("Interfaces Mult2.png")
st.image(image, caption="Interfaces Multimodales")

# TEXTO
texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("El texto escrito es", texto)

# COLUMNAS
st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo") # Caja de check
  if resp:
    st.write("¡Correcto!")
    
with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz",("Visual","Auditiva","Táctil"))
  if modo == "Visual": # Selección Multiple
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audición es fundamental para tu interfaz")
  if modo == "Táctil":
    st.write("El tacto es fundamental para tu interfaz")

# BOTONES
st.subheader("Uso de botones")
if st.button("Presiona el boton"):
  st.write("Gracias por presionar, sapa")
else:
  st.write("P R E S I O N A M E... te reto")

# MENU DESPLEGABLE
st.subheader("Selectbox")
in_mond = st.selectbox(
  "Selecciona la modalidad",("Audio","Visual","Háptico")
  )
if in_mod == "Audio":
  set_mod = "Reproducir audio"
elif in_mod == "Visual":
  set_mod = "Reproducir video"
elif in_mod == "Háptico":
  set_mod = "Reproducir vibración"
st.write("La acción es:", set_mod)


