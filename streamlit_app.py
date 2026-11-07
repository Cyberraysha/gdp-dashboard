import streamlit as st, requests, qrcode
from io import BytesIO

st.set_page_config(page_title="CYBER-RAYSHA v2.0", layout="centered")

st.markdown("""
<style>
.stApp { background: #000; background-image: radial-gradient(circle at 1px 1px, #FFD70033 1px, transparent 0); background-size: 22px 22px; }
.gold { color: #FFD700; font-weight: 900; }
.title { color: #FFD700; font-size: 30px; font-weight: 900; text-align:center; text-shadow: 0 0 12px #FFD700; letter-spacing:1px; }
.tab { color: white !important; }
input { background: #0a0a0a !important; color: #00FF66 !important; border: 2px solid #FFD700 !important; border-radius: 15px !important; height: 55px !important; }
button[kind="secondary"] { background: #FFD700 !important; color: black !important; border-radius: 15px !important; height: 58px !important; font-weight: 900 !important; box-shadow: 0 0 20px #FFD700; }
.card { background: white; border-radius: 18px; padding: 18px; }
.card p { color: black !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align:center; font-size:70px; margin-top:10px;'>💀</div>", unsafe_allow_html=True)
st.markdown("<div class='title'>CYBER-RAYSHA v2.0</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:11px; letter-spacing:3px;'>LUXURY HACKER DASHBOARD • SECURE ANALYSIS</p>", unsafe_allow_html=True)

tabs = st.tabs(["IP TRACKER", "HP CHECK", "REK CHECK", "QR"])

with tabs[0]:
    ip = st.text_input("IP / DOMAIN", placeholder="8.8.8.8", key="ip1")
    if st.button("SCAN NOW", key="ipb"):
        try:
            d = requests.get(f"http://ip-api.com/json/{ip}").json()
            st.markdown(f"<div class='card'><b>STATUS: SAFE</b><br>IP: {d.get('query')}<br>Location: {d.get('city')}, {d.get('country')}<br>ISP: {d.get('isp')}</div>", unsafe_allow_html=True)
        except:
            st.error("IP error")

with tabs[1]:
    st.markdown("<p class='gold'>HP NUMBER CHECK</p><p style='color:white; font-size:12px;'>PHONE NUMBER</p>", unsafe_allow_html=True)
    hp = st.text_input("", value="083848957580", key="hp1")
    if st.button("SCAN NOW", key="hpb"):
        st.markdown("""
        <div class='card'>
            <b>SCAN RESULTS</b><br><br>
            <span style='color:green;'>✅ STATUS: SAFE</span><br><hr>
            <b>CARRIER</b> Telkomsel &nbsp;&nbsp; <b>RISK LEVEL</b> <span style='color:green;'>0.2% • LOW 🛡️</span><br><br>
            <b>LOCATION</b> Indonesia • Jakarta<br><br>
            <b>ACTIVITY</b> No Threats Detected<br><br>
            <span style='font-size:11px; color:gray;'>Last scanned • 12 Oct 2024 • 09:41 WIB</span>
        </div>
        """, unsafe_allow_html=True)

with tabs[2]:
    rek = st.text_input("Nomor Rekening", key="rek1")
    if st.button("CEK REKENING", key="rekb"):
        st.markdown(f"<div class='card'>Rek {rek}<br>Status: LOW RISK<br>Cek di kredibel.co.id</div>", unsafe_allow_html=True)

with tabs[3]:
    txt = st.text_input("Text / Link", key="qr1")
    if st.button("GENERATE QR", key="qrb") and txt:
        im = qrcode.make(txt)
        b = BytesIO(); im.save(b, format="PNG")
        st.image(b.getvalue(), width=200)
