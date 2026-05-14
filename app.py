import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mi App de Ingresos", layout="centered")
st.title("💰 Gestor de Suscripciones Premium")

if 'subs' not in st.session_state:
    st.session_state.subs = []

with st.form("registro"):
    nombre = st.text_input("Nombre del Servicio")
    costo = st.number_input("Costo Mensual (USD)", min_value=0.0)
    if st.form_submit_button("Guardar"):
        st.session_state.subs.append({"Servicio": nombre, "Costo": costo})

if st.session_state.subs:
    df = pd.DataFrame(st.session_state.subs)
    st.table(df)

    if len(st.session_state.subs) >= 3:
        st.error("🔒 Límite gratuito alcanzado. Desbloquea la versión Pro.")
        # BOTÓN DE PAGO REAL
        st.markdown(f'<a href="TU_LINK_DE_STRIPE_AQUI" target="_blank" style="text-decoration:none;"><div style="background-color:#6772E5;color:white;padding:15px;text-align:center;border-radius:5px;font-weight:bold;">PAGAR $2.99 PARA CONTINUAR</div></a>', unsafe_allow_html=True)
