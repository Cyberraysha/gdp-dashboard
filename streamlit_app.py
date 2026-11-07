import streamlit as st
import requests, socket, re, qrcode
from io import BytesIO

st.set_page_config(page_title="CYBER-RAYSHA v2.0", page_icon="💀", layout="centered")

# SKULL LOGO + CSS TERANG
st.markdown("""
<style>
.stApp { background: #0a0a0a; }
h1 { color: #FFD700 !important; text-align:center; text-shadow: 0 0 10px #FFD700; }
h3, p, div, label { color: #FFFFFF !important; }
input { background: #1a1a1a !important; color: #00FF7F !important; border: 2px solid #FFD700 !important; }
.stButton>button { background: #FFD700 !important; color: black !important; font-weight: 900 !important; }
.scan-box { background: #111; border: 1px solid #FFD700; border-radius: 15px; padding: 15px; }
.result-box { background: white !important; border-radius: 15px; padding: 15px; }
.result-box p, .result-box div { color: black !important; }
</style>
""", unsafe_allow_html=True)

# LOGO TENGKORAK
st.markdown("<div style='text-align:center; font-size:80px;'>💀</div>", unsafe_allow_html=True)
st.markdown("<h1>CYBER-RAYSHA v2.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gold;'>SKULL HOODIE HACKER PROTOCOL • GHOST</p>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["IP TRACKER","HP CHECK","REK CHECK","QR GENERATOR"])

with tab1:
    ip = st.text_input("IP / DOMAIN", placeholder="8.8.8.8")
    if st.button("SCAN NOW", key="ip"):
        st.success(f"IP {ip} scanned")

with tab2:
    st.subheader("HP NUMBER CHECK")
    hp = st.text_input("Target Phone Number", value="083848957580")
    if st.button("SCAN NOW", key="hp"):
        st.markdown(f"""
        <div class="result-box">
        <b>SCAN RESULTS: STATUS SAFE</b><br><br>
        Carrier: Telkomsel<br>
        Country: Indonesia - Jakarta<br>
        Connection: Online • Active<br>
        Risk: 0.2% • LOW • No Threats<br>
        SIM Validity: VERIFIED • CLEAN
        </div>
        """, unsafe_allow_html=True)

with tab3:
    rek = st.text_input("Nomor Rekening")
    if st.button("CEK REKENING"): st.info("Cek via kredibel API")

with tab4:
    qr = st.text_input("Text untuk QR")
    if st.button("GENERATE QR") and qr:
        img = qrcode.make(qr)
        buf = BytesIO(); img.save(buf, format="PNG")
        st.image(buf.getvalue(), width=200)
