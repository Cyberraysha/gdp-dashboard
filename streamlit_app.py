import streamlit as st

st.set_page_config(page_title="CYBER-RAYSHA v2.0", page_icon="💀")

# CSS Final - Skull Gold + Input Jelas
st.markdown("""
<style>
.stApp { background: #0a0a0a; }
h1 { color: #FFD700 !important; text-align: center; letter-spacing: 5px; }
/* Input nomor biar kelihatan jelas */
input[type="text"] {
    background: #1a1a1a !important;
    color: #00FF7F !important;
    border: 2px solid #FFD700 !important;
    font-size: 20px !important;
    font-weight: bold !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>CYBER-RAYSHA v2.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:gold; text-align:center;'>SKULL HOODIE HACKER PROTOCOL • GHOST</p>", unsafe_allow_html=True)

# Input nomor - pasti kelihatan
nomor = st.text_input("PHONE NUMBER", placeholder="0812XXXXXXX")
if st.button("AUTHENTICATE NOW"):
    st.success(f"Nomor {nomor} terkoneksi ke Ghost Node!")
