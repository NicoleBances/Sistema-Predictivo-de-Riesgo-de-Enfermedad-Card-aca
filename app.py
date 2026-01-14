import streamlit as st
import h2o
import pandas as pd
import os
from utils import traducir_entrada

if not h2o.connection():
    h2o.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "StackedEnsemble_AllModels_1_AutoML_1_20250713_31308")
model = h2o.load_model(MODEL_PATH)

features = [
    'Edad',
    'Salud general',
    'Dificultad al caminar',
    'Diabetes',
    'Días de mala salud física (últimos 30)',
    'Fuma',
    'Actividad física',
    'Cáncer de piel'
]

# Opciones visibles en español
options = {
    'Edad': ["18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59",
             "60-64", "65-69", "70-74", "75-79", "80 o más"],
    'Salud general': ["Pobre", "Regular", "Buena", "Muy buena", "Excelente"],
    'Dificultad al caminar': ["Sí", "No"],
    'Diabetes': ["Sí", "No", "No, prediabetes", "Sí (embarazo)"],
    'Días de mala salud física (últimos 30)': list(range(0, 31)),
    'Fuma': ["Sí", "No"],
    'Actividad física': ["Sí", "No"],
    'Cáncer de piel': ["Sí", "No"]
}

st.set_page_config(page_title="Predicción Cardíaca", layout="centered")

st.title("Sistema de Predicción de Enfermedad Cardíaca")

st.markdown("""
Este proyecto académico utiliza modelos de aprendizaje automático para predecir el riesgo
de padecer enfermedad cardíaca en base a información personal y hábitos de salud.

### ¿Cómo usar esta herramienta?
1. Completa el formulario con tus datos.
2. Haz clic en **Evaluar**.
3. Revisa tu nivel de riesgo y recibe una recomendación.

> 🧠 *Nota: Esta herramienta no reemplaza el diagnóstico médico profesional.*
""")

st.markdown("---")

# --- Sección de predicción ---
st.header("🔎 Evaluación de Riesgo Personal")

user_input = {}

for feature in features:
    if isinstance(options[feature][0], int):
        user_input[feature] = st.slider(feature, min_value=0, max_value=30)
    else:
        user_input[feature] = st.selectbox(feature, options[feature])

if st.button("Evaluar"):
    entrada_convertida = traducir_entrada(user_input)
    input_df = pd.DataFrame([entrada_convertida])
    input_h2o = h2o.H2OFrame(input_df)

    pred = model.predict(input_h2o)
    pred_label = pred.as_data_frame().iloc[0, 0]
    pred_prob = pred.as_data_frame().iloc[0, 1]

    if pred_label == "Yes":
        st.error(f"⚠ Riesgo **alto** de enfermedad cardíaca. (Probabilidad: {pred_prob:.2%})")
        st.warning("Se recomienda consultar con un especialista médico.")
    else:
        st.success(f"✅ Riesgo **bajo** de enfermedad cardíaca. (Probabilidad: {pred_prob:.2%})")
        st.info("Sigue cuidando tu salud con buenos hábitos. 🥦🏃‍♀️🧘")
