import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('model_karyawan.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Penerimaan Karyawan LogiEqual", page_icon="🧑‍💼", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #fff;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin: 2rem auto;
        max-width: 650px;
    }
    h1, h2 {
        text-align: center;
        color: #227093;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown("<h1>💼 Penerimaan Karyawan LogiEqual</h1>", unsafe_allow_html=True)

# Form Input
with st.form("seleksi_form"):
    jenis_kelamin = st.radio("🚻 Jenis Kelamin", ["Perempuan", "Laki-laki"], horizontal=True)
    usia = st.slider("🎂 Usia", 18, 60, 25)
    pendidikan = st.selectbox("🎓 Pendidikan Terakhir", ["SMA", "D3", "S1", "S2"])
    pengalaman = st.number_input("🧰 Pengalaman Kerja (tahun)", 0, 40, 1)
    interview = st.slider("💬 Skor Interview", 0, 100, 75)
    submit = st.form_submit_button("📊 Prediksi Kelulusan")

# Mapping
pend_map = {"SMA": 0, "D3": 1, "S1": 2, "S2": 3}
gender_map = {"Perempuan": 0, "Laki-laki": 1}

if submit:
    fitur = np.array([[gender_map[jenis_kelamin], usia, pend_map[pendidikan], pengalaman, interview]])
    prediksi = model.predict(fitur)[0]

    st.markdown("---")
    if prediksi == 1:
        st.success(f"🎉 Pelamar **LOLOS** seleksi. Terima kasih sudah berkontribusi untuk kesetaraan gender di LogiEqual.")
    else:
        st.error("😞 Pelamar **TIDAK LOLOS** seleksi.")

st.markdown('</div>', unsafe_allow_html=True)
