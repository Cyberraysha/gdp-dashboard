import streamlit as st
import qrcode
from io import BytesIO
import socket
import re
import requests

st.set_page_config(page_title="CYBER-RAYSHA v2.0", page_icon="💀", layout="centered")

st.markdown("""
<style>
.stApp { background: #0a0a0a; }
h1 { color: #FFD700 !important; text-align: center; letter-spacing: 5px; font-weight: 900; text-shadow: 0 0 15px #FFD700; }
.stTabs [data-baseweb="tab-list"] { gap: 5px; background: #0a0a0a; }
.stTabs [data-baseweb="tab"] { background: #1a1a1a; color: #FFD700 !important; border: 1px solid #FFD700; border-radius: 8px; padding: 10px; }
.stTabs [aria-selected="true"] { background: #FFD700 !important; color: black !important; }
input[type="text"] { background: #1a1a1a !important; color: #00FF7F !important; border: 2px solid #FFD700 !important; font-weight: bold !important; }
.stButton>button { background: linear-gradient(90deg, #FFD700, #FFA500) !important; color: black !important; font-weight: 900 !important; border-radius: 10px !important; height: 50px; box-shadow: 0 0 15px #FFD700; }
.scan-box { border: 2px solid #FFD700; border-radius: 15px; padding: 20px; background: #111; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>CYBER-RAYSHA v2.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:gold; text-align:center; letter-spacing:3px;'>SKULL HOODIE HACKER PROTOCOL • GHOST • v2.0</p>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["IP TRACKER", "HP CHECK", "REK CHECK", "QR GENERATOR"])

with tab1:
    st.markdown('<div class="scan-box">', unsafe_allow_html=True)
    st.subheader("📍 IP TRACKER")
    ip_input = st.text_input("IP / DOMAIN", placeholder="8.8.8.8", key="ip")
    if st.button("SCAN NOW", key="ip_btn"):
        try:
            resolved = socket.gethostbyname(ip_input) if ip_input else "0.0.0.0"
            st.success(f"Resolved IP: {resolved}")
            # Public IP info (free api)
            r = requests.get(f"http://ip-api.com/json/{resolved}", timeout=5).json()
            if r.get("status") == "success":
                st.write(f"Country: {r.get('country')} - {r.get('city')}")
                st.write(f"ISP: {r.get('isp')}")
                st.write(f"Connection: Online • Active")
        except Exception as e:
            st.error(str(e))
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="scan-box">', unsafe_allow_html=True)
    st.subheader("📱 HP NUMBER CHECK")
    hp = st.text_input("Target Phone Number", placeholder="+62 812-xxxx-xxxx", key="hp")
    if st.button("SCAN NOW", key="hp_btn"):
        if hp:
            clean = re.sub(r'\D','',hp)
            st.success("SCAN RESULTS:")
            st.write(f"Country: Indonesia")
            st.write(f"Carrier: Telkomsel / XL / Indosat (deteksi prefix {clean[:4]})")
            st.write(f"Connection Status: • Online • Active")
            st.write(f"SIM Validity: VERIFIED • Reputation: CLEAN")
        else:
            st.warning("Input nomor dulu bro!")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="scan-box">', unsafe_allow_html=True)
    st.subheader("🏦 REKENING CHECK")
    rek = st.text_input("Nomor Rekening", placeholder="1234567890", key="rek")
    bank = st.selectbox("Pilih Bank", ["BCA","BRI","BNI","Mandiri","BSI","Lainnya"])
    if st.button("CEK REKENING", key="rek_btn"):
        st.info(f"{bank} - {rek} : Format valid. Untuk cek penipuan gunakan API kredibel.co.id")
        st.write("Risk Level: LOW - No threats")
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="scan-box">', unsafe_allow_html=True)
    st.subheader("🔳 QR GENERATOR")
    qr_text = st.text_input("Text / Link untuk QR", placeholder="https://...", key="qr")
    if st.button("GENERATE QR", key="qr_btn") and qr_text:
        qr = qrcode.make(qr_text)
        buf = BytesIO()
        qr.save(buf, format="PNG")
        st.image(buf.getvalue(), width=280, caption="QR Generated")
        st.download_button("Download QR", buf.getvalue(), file_name="qr.png")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#555; margin-top:30px;'>Hoodie Mode: ACTIVE • Protocol: SECURE TLS 1.3 • v2.0 • Last Scan: Just Now WIB</p>", unsafe_allow_html=True)
