import streamlit as st
from openai import OpenAI

st.title("🔍 Evaluación de Preprocesamiento de Datos")

# Inicializar cliente de OpenAI
openai_api_key = st.secrets["api_key"]
client = OpenAI(api_key=openai_api_key)

# Instrucción y advertencia
st.markdown("""
Pega el fragmento de código donde realizas el preprocesamiento con `StandardScaler`, `MinMaxScaler`, o `RobustScaler`. 
""")

student_code = st.text_area("📋 Pega aquí tu código")

if st.button("🧠 Evaluar código"):
    prompt = f"""
Actúa como un experto en Machine Learning. Evalúa si el siguiente código de preprocesamiento comete el error común de aplicar `.fit()` sobre el conjunto de prueba (lo cual no se debe hacer). 
Indica si el código es correcto o incorrecto. Si hay errores, sugiere una corrección.

Código:
{student_code}

Responde de forma clara y breve:
- ¿El código aplica correctamente los escaladores?
- ¿Se está usando `.fit()` en el test?
- ¿Qué recomendación harías?
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Eres un profesor de Machine Learning revisando código de estudiantes."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0,
    )

    result = response.choices[0].message.content
    st.markdown("### 📄 Resultado:")
    st.write(result)

    # Lanzar globos si el código fue correcto
    if "código es correcto" in result.lower() or "no se encontró error" in result.lower():
        st.success("¡Muy bien hecho! 🎉")
        st.balloons()
