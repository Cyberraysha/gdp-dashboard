with tab1:
    ip = st.text_input("Masukkan IP (kosongkan = IP kamu sendiri)", placeholder="8.8.8.8")
    if st.button("LACAK SEKARANG", key="ip"):
        try:
            # INI FIX NYA BRO - Kalo kosong ambil IP asli user
            if not ip.strip():
                ip_asli = requests.get("https://api.ipify.org", timeout=5).text
                ip = ip_asli
                st.info(f"IP kamu terdeteksi: {ip}")
            
            r = requests.get(f"http://ip-api.com/json/{ip.strip()}", timeout=10).json()
            if r['status']=='success':
                st.success(f"IP {r['query']} - {r['city']}, {r['country']}")
                col1,col2 = st.columns(2)
                with col1:
                    st.write(f"**Kota:** {r['city']}")
                    st.write(f"**Provinsi:** {r['regionName']}")
                    st.write(f"**ISP:** {r['isp']}")
                    st.warning("Ini cuma lokasi tower ISP ya, bukan alamat rumahmu. Tenang, aman.")
                with col2:
                    st.write(f"**Negara:** {r['country']}")
                    st.write(f"**Koordinat:** {r['lat']}, {r['lon']}")
                    st.map(data={'lat':[r['lat']], 'lon':[r['lon']]})
                    st.link_button("Buka di Google Maps", f"https://maps.google.com/?q={r['lat']},{r['lon']}")
                    
                    # INI TOMBOL JUALAN SOLUSI LU
                    st.divider()
                    st.write("**Mau IP gak kebaca orang?**")
                    st.link_button("🔒 CARA GANTI IP GRATIS", "https://www.google.com/search?q=cara+ganti+ip+hp")
            else:
                st.error("IP tidak valid")
        except Exception as e:
            st.error(str(e))
