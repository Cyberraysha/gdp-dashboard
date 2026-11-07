import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="CYBER-RAYSHA v2.0", layout="centered")

st.markdown("""
<style>
.stApp { background: #050505; }
.gold-title { color: #FFD700; font-size: 32px; font-weight: 900; text-align:center; letter-spacing:2px; text-shadow: 0 0 15px #FFD700; }
.sub { color: white; text-align:center; font-size:12px; letter-spacing:3px; }
.label { color: #FFD700 !important; font-weight: bold; margin-top:15px; }
input { background: #0f0f0f !important; color: #00FF66 !important; border: 2px solid #FFD700 !important; border-radius: 15px !important; height: 55px !important; font-size:18px !important; }
.stButton>button { background: #FFD700 !important; color: black !important; font-weight: 900 !important; border-radius: 15px !important; height: 60px; width: 100%; font-size:20px; box-shadow: 0 0 20px #FFD700; }
.result-card { background: white; border-radius: 20px; padding: 20px; margin-top:20px; }
.result-card p { color: black !important; margin:5px 0; }
.bottom-nav { position: fixed; bottom:0; left:0; right:0; background: #111; display:flex; justify-content: space-around; padding:10px; border-top: 1px solid gold; }
.circuit { background-image: radial-gradient(circle at 1px 1px, #FFD70022 1px, transparent 0); background-size: 20px 20px; }
</style>
""", unsafe_allow_html=True)

# SKULL HEADER
st.markdown("<div style='text-align:center; padding:20px;' class='circuit'>", unsafe_allow_html=True)
st.markdown("<div style='font-size:80px;'>☠️</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='gold-title'>CYBER-RAYSHA v2.0</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>LUXURY HACKER DASHBOARD • SECURE ANALYSIS</div>", unsafe_allow_html=True)

st.markdown("<div class='label'>HP NUMBER CHECK</div>", unsafe_allow_html=True)
st.markdown("<div class='label' style='font-size:12px; color:white !important;'>PHONE NUMBER</div>", unsafe_allow_html=True)

hp = st.text_input("phone", value="083848957580", label_visibility="collapsed", placeholder="0838...")

if st.button("📍 SCAN NOW"):
    st.markdown("""
    <div class="result-card">
        <p style="font-weight:900; font-size:18px;">✅ STATUS: SAFE</p>
        <hr>
        <p><b>CARRIER</b> Telkomsel &nbsp;&nbsp; <b>RISK LEVEL</b> <span style="color:green;">0.2% • LOW 🛡️</span></p>
        <p><b>LOCATION</b> Indonesia • Jakarta</p>
        <p><b>ACTIVITY</b> No Threats Detected</p>
        <p style="font-size:12px; color:gray;">Last scanned • 12 Oct 2024 • 09:41 WIB</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="display:flex; justify-content:space-around; background:#111; padding:15px; border-radius:15px; border:1px solid gold; margin-top:30px;">
    <div style="text-align:center; color:gold;">🏠<br>HOME</div>
    <div style="text-align:center; color:gray;">🕒<br>HISTORY</div>
    <div style="text-align:center; color:gray;">🛡️<br>SECURITY</div>
    <div style="text-align:center; color:gray;">👤<br>PROFILE</div>
</div>
""", unsafe_allow_html=True)
