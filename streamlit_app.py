import streamlit as st
import requests

st.set_page_config(page_title="IP Checker Indonesia", page_icon="🌏")
st.title("🌏 CEK LOKASI IP")
st.write("Cek IP bocor dimana. Support semua provider Indonesia.")

ip_input = st.text_input("Masukkan IP yang mau di cek:", placeholder="Contoh: 114.10.23.45 atau 8.8.8.8")

if st.button("CEK LOKASI SEKARANG"):
    if not ip_input.strip():
        st.error("Masukkan IP dulu bro. Cek IP di google ketik 'what is my ip'")
        st.stop()
    
    try:
        ip = ip_input.strip()
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=10).json()
        
        if r['status']=='success':
            st.success(f"IP {r['query']} Ketemu!")
            
            # Ganti Bekasi jadi Jakarta biar general
            kota = r['city']
            if "Bekasi" in kota or "Bekasi" in r['regionName']:
                kota_tampil = "Jakarta Area"
            else:
                kota_tampil = kota

            c1,c2 = st.columns(2)
            with c1:
                st.metric("Kota / Area", kota_tampil)
                st.write(f"**Provinsi:** {r['regionName']}")
                st.write(f"**Negara:** {r['country']}")
            with c2:
                st.metric("Provider", r['isp'])
                st.write(f"**Koordinat:** {r['lat']}, {r['lon']}")
                st.map(data={'lat':[r['lat']], 'lon':[r['lon']]})
            
            st.info(f"📍 Lokasi: {kota_tampil}, {r['regionName']} - {r['country']} | ISP: {r['isp']}")
            st.caption("Note: Ini lokasi server provider, bukan alamat rumah exact.")
            
        else:
            st.error("IP tidak valid. Pastikan format IP bener, contoh: 36.72.12.5")
    except Exception as e:
        st.error(f"Gagal cek: {e}")
