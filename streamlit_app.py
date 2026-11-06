import streamlit as st
st.set_page_config(page_title="CYBER RAYSHA", layout="wide")
st.markdown("<h1 style='text-align:center;color:cyan;'>⚡ CYBER RAYSHA ULTRA ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>By Fajar Septian - Bekasi</p>", unsafe_allow_html=True)
ip=st.text_input("Masukkan IP Target")
if st.button("Lacak IP"):
    st.success(f"IP {ip} terlacak di Jakarta - Bekasi")
ig=st.text_input("Username IG")
if st.button("Stalk IG"):
    st.success(f"Data {ig} berhasil diambil!")
if st.button("Generate Sultan"):
    st.code("Username: raysha_sultan_88")
