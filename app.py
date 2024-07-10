import streamlit as st
import pickle
from streamlit_option_menu import option_menu


jurusan_model = pickle.load(open('jurusan.Model.sav', 'rb'))
with st.sidebar:
            selected=option_menu('Sistem Penentuan Jurusan',
                                ['About',
                                'Prediksi Jurusan'
                                ],
                                  icons=['file-text', 'person'],
                                  default_index=0
                                  )

 #Explanation Page
if (selected == 'About'):

      #page title
      st.title('Apa itu Jurusan')

      #body of text
      st.write('Jurusan adalah suatu hal yang paling utama sebelum anda memasuki pembelajaran')
      st.title('Dataset')

#Jurusan prediksi
if (selected == 'Prediksi Jurusan'):
      st.title('Prediksi Jurusan dengan KNN')
      col1, col2, col3 = st.colomns(3)
      with col1:
        Nama_Siswa = st.text_input('Nama Siswa')

      with col2:
        Nilai_Matematika = st.number_input('Matematika')
    
      with col3:
        Nilai_IPA = st.number_input('IPA')
      
      with col1:
        Nilai_IPS = st.number_input('IPS')
      
      with col2:
        Nilai_Bahasa_Inggris = st.number_input('Bahasa Inggris')

        #jurusan prediksi
        jurusan_predict

        if st.button('Test Nilai Saya'):
          jurusan_hasil = jurusan_model.predict([[Matematika, IPA, IPS, Bahasa_Inggris]])
          if prediksi_baru == 0:
            jurusan_adalah = "Desain Komunikasi Visual"
          elif prediksi_baru == 1:
            jurusan_adalah = "Desain Pemodelan dan Informasi Bangunan"
          elif prediksi_baru == 2:
            jurusan_adalah = "Perhotelan"
          elif prediksi_baru == 3:
            jurusan_adalah = "Teknik Instalasi Tenaga Listrik"
          elif prediksi_baru == 4:
            jurusan_adalah = "Teknik Komputer dan Jaringan"
          elif prediksi_baru == 5:
            jurusan_adalah = "Teknik Sepeda Motor"
          elif prediksi_baru == 6:
            jurusan_adalah = "Teknik Pemesinan"
          elif prediksi_baru == 7:
            jurusan_adalah = "Teknik Kendaraan Ringan"
          else:
            jurusan_adalah = "Tidak ada Jurusan yang sesuai"

          print("Jurusan yang sesuai untuk Anda adalah: ", jurusan_predict)
        st.success(jurusan_predict)
