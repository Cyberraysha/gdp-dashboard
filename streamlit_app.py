import streamlit as st
import requests

st.set_page_config(page_title="CYBER RAYSHA ULTRA V2", page_icon="💀", layout="wide")

st.markdown("""
<style>
.stApp { background:#000; color:#00ffcc; }
h1 { color:#00ffcc; text-align:center; text-shadow:0 0 15px #00ffcc; }
.stTextInput input { background:#111 !important; color:#00ffcc !important; border:1px solid #00ffcc !important; }
.stButton>button { background:#00ffcc; color:#000; font-weight:bold; width:100%; border-radius:10px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>💀 CYBER RAYSHA ULTRA V2 💀</h1><p style='text-align:center;'>By Fajar Septian - Bekasi | Real IP + Map</p>", unsafe_allow_html=True)
st.markdown("---")

tab1, tab2 = st.tabs(["🌐 LACAK IP + PETA REAL", "📸 STALK IG REAL"])

with tab1:
    ip = st.text_input("Masukkan IP (kosongkan = IP kamu sendiri)", placeholder="8.8.8.8")
    if st.button("LACAK SEKARANG", key="ip"):
        try:
            r = requests.get(f"http://ip-api.com/json/{ip.strip()}", timeout=10).json()
            if r['status']=='success':
                st.success(f"IP {r['query']} - {r['city']}, {r['country']}")
                col1,col2 = st.columns(2)
                with col1:
                    st.write(f"**Kota:** {r['city']}")
                    st.write(f"**Provinsi:** {r['regionName']}")
                    st.write(f"**ISP:** {r['isp']}")
                with col2:
                    st.write(f"**Negara:** {r['country']}")
                    st.write(f"**Koordinat:** {r['lat']}, {r['lon']}")
                st.map(data={'lat':[r['lat']], 'lon':[r['lon']]})
                st.link_button("Buka di Google Maps", f"https://maps.google.com/?q={r['lat']},{r['lon']}")
            else:
                st.error("IP tidak valid")
        except Exception as e:
            st.error(str(e))

with tab2:
    username = st.text_input("Username IG tanpa @", placeholder="nasa")
    if st.button("STALK SEKARANG", key="ig"):
        if username:
            st.link_button(f"Buka Profil @{username}", f"https://www.instagram.com/{username}/")
            st.image(f"https://unavatar.io/instagram/{username}", width=250)
            st.caption("Menampilkan foto profil publik. Jika akun private, hanya foto yang bisa tampil.")
