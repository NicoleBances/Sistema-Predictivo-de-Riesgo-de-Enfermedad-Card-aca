# Sistema Predictivo de Riesgo de Enfermedad Cardíaca

---

## Descripción del Proyecto

Este proyecto desarrolla un **sistema predictivo para evaluar el riesgo de enfermedad cardíaca** utilizando aprendizaje automático con **H2O**.  

Se entrenaron modelos supervisados:

- Random Forest  
- Gradient Boosting Machine (GBM)  
- Generalized Linear Model (GLM)  
- AutoML (Stacked Ensemble)  

Se implementó una **aplicación web interactiva con Streamlit**, donde los usuarios pueden ingresar sus datos y recibir una predicción personalizada de riesgo cardiovascular.  

**Objetivo:** demostrar el potencial de la ciencia de datos para apoyar la prevención en salud de forma accesible y educativa.  

---

Colaboradores
Francesca Nicole Bances Torres
Marsi Valeria Figueroa Larragán 

---

## Conjunto de Datos

- **Fuente:** Kaggle – [Personal Key Indicators of Heart Disease](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease)  
- **Registros:** 319,795  
- **Variables:** 18, incluyendo la variable objetivo `HeartDisease` (Yes/No).  
- **Tipo de variables:** combinación de categóricas (ej. Diabetes, Smoking, Sex) y numéricas (ej. BMI, PhysicalHealth, SleepTime).  

---

## Análisis Exploratorio de Datos (EDA)

Se realizó un análisis inicial para comprender la estructura del dataset:

- Distribución de variables categóricas y numéricas.  
- Identificación de valores atípicos y limpieza de datos.  
- Relación entre variables predictoras y la variable objetivo.  
- Cálculo de **Information Value (IV)** para medir la capacidad predictiva de cada variable.  

**Variables más relevantes:** `DiffWalking`, `GenHealth`, `Diabetic`, `AgeCategory`, `PhysicalActivity`.  

---

## Modelos Entrenados

| Modelo           | AUC      | Gini     |
|-----------------|----------|----------|
| GLM             | 0.8215   | 0.6431   |
| Boosting        | 0.8201   | 0.6402   |
| Random Forest   | 0.8141   | 0.6283   |
| AutoML (Ensemble)| 0.8247  | 0.6495   |

- **AutoML** obtuvo el mejor desempeño, confirmando la efectividad del ensamblado automático.  
- GLM y Boosting también mostraron resultados competitivos, superiores a Random Forest.  
- Todos los modelos superan un AUC de 0.81, indicando buena capacidad predictiva sobre el dataset.  


---

## Implementación Aplicativa

- **Herramienta:** Streamlit  
- **Interfaz:** Formulario en español para ingresar datos personales.  
- **Resultado:** Predicción de riesgo alto/bajo con recomendaciones preventivas.  
- **Objetivo:** Sistema educativo y de apoyo a la prevención, no diagnóstico médico.

## Conclusiones

1. Se logró construir un sistema predictivo eficaz utilizando variables simples y accesibles.  
2. AutoML fue el modelo con mejor desempeño (AUC = 0.8247, Gini = 0.6495).  
3. Variables más relevantes: salud percibida, edad, diabetes, actividad física y dificultad para caminar.  
4. Incluso sin indicadores clínicos invasivos, se pueden obtener predicciones razonables para apoyo en salud pública.  

---

## Recomendaciones

- Validar el modelo en contextos latinoamericanos y ajustar parámetros con datos locales.  
- Incorporar variables clínicas más detalladas para mejorar precisión.  
- Desarrollar versiones accesibles para usuarios no técnicos, con enfoque preventivo.  
- Monitorear sesgo y equidad del modelo en diferentes subgrupos poblacionales.  
- Mantener entrenamiento iterativo con nuevos datos para actualizar predicciones.   
 

