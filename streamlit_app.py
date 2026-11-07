import streamlit as st
import requests
import phonenumbers
from phonenumbers import carrier, geocoder
from PIL import Image
import cv2
import numpy as np

st.set_page_config(page_title="ER-RAYSA SUPER CHECK", page_icon="🛡️", layout="centered")

st.title("🛡️ ER-RAYSA SUPER CHECK")
st.caption("Bantu Cek IP, Nomor HP & Rekening Penipu - Aman & Legal")

tab1, tab2, tab3, tab4 = st.tabs(["🌍 CEK IP", "📱 CEK NO HP", "🏦 CEK REKENING", "🔳 CEK QR"])

with tab1:
    st.subheader("Cek IP Viewer TikTok")
    ip_input = st.text_input("Masukkan IP", placeholder="Contoh: 36.85.12.44 (punya lu yang Malang tadi)")
    if st.button("CEK IP SEKARANG", key="ip"):
        if ip_input:
            try:
                r = requests.get(f"http://ip-api.com/json/{ip_input}").json()
                if r['status'] == 'success':
                    st.success(f"IP {ip_input} Ketemu!")
                    st.write(f"**Kota / Area:** {r['city']}, {r['regionName']}, {r['country']}")
                    st.write(f"**Provider:** {r['isp']}")
                    st.write(f"**Timezone:** {r['timezone']}")
                else:
                    st.error("IP gak ketemu")
            except:
                st.error("Gagal cek IP")

with tab2:
    st.subheader("Cek Nomor HP (Wajib Izin Pemilik)")
    st.warning("⚠️ Ini cuma cek provider & area registrasi awal, BUKAN GPS live orangnya!")
    nomor = st.text_input("Masukkan nomor HP", placeholder="08123456789")
    if st.button("CEK NOMOR SEKARANG", key="hp"):
        if nomor:
            try:
                parse = phonenumbers.parse(nomor, "ID")
                prov = carrier.name_for_number(parse, "id")
                area = geocoder.description_for_number(parse, "id")
                valid = phonenumbers.is_valid_number(parse)
                st.success(f"Nomor {nomor} Valid!" if valid else "Nomor tidak valid")
                st.write(f"**Provider:** {prov}")
                st.write(f"**Area Registrasi Awal:** {area}")
                st.info("Ini bukan posisi dia sekarang, ini cuma tempat nomor ini pertama kali didaftarkan.")
                wa_num = phonenumbers.format_number(parse, phonenumbers.PhoneNumberFormat.E164).replace("+","")
                st.link_button("💬 Chat WA Nomor Ini", f"https://wa.me/{wa_num}")
            except:
                st.error("Nomor gak valid bro")

with tab3:
    st.subheader("Cek Rekening Penipu")
    st.write("Ini fitur paling penting buat korban ketipu di FB!")
    st.link_button("🔍 CEK DI CEKREKENING.ID (Resmi Kominfo)", "https://cekrekening.id")
    st.link_button("🔍 CEK DI KREDIBEL.CO.ID", "https://kredibel.co.id")
    st.write("---")
    st.write("**Abis cek, apa yang harus dilakuin korban?**")
    st.write("1. Screenshot hasil cek yang ada laporan penipu")
    st.write("2. Lapor ke bank pemilik rekening minta blokir")
    st.write("3. Lapor online ke patrolisiber.id")

with tab4:
    st.subheader("Cek Kode QR Transferan")
    st.write("Kalo korban transfer pake QRIS, upload foto QR nya disini!")
    uploaded = st.file_uploader("Upload foto QR Code", type=["jpg","png","jpeg"])
    if uploaded:
        file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        st.image(opencv_image, caption="Foto QR yang diupload", channels="BGR")
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(opencv_image)
        if data:
            st.success("QR Berhasil Dibaca!")
            st.code(data)
            st.write("Copy ID itu terus cek di Tab Cek Rekening!")
        else:
            st.error("QR gak kebaca bro, coba foto yang lebih jelas.")
