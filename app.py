import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Cargar el modelo
MODEL_PATH = 'best_model.h5'
model = load_model(MODEL_PATH)

# Función para preprocesar la imagen
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalización
    return img_array

# Interfaz de Streamlit
st.title("COVID-19 Detection App")
uploaded_file = st.file_uploader("Sube una imagen de rayos X", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
   
    img_path = os.path.join("uploads", uploaded_file.name)  # Guardar la imagen subida
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    
    st.image(img_path, caption="Imagen cargada", use_column_width=True) # Mostrar la imagen

    
    img = preprocess_image(img_path) # Preprocesar la imagen

    #
    prediction = model.predict(img)

    # Mostrar el resultado
    if prediction > 0.5:
        st.write("Predicción: **COVID-19 positivo**")
    else:
        st.write("Predicción: **Normal**")
