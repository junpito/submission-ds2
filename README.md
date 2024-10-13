# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut, yang berdiri sejak tahun 2000, telah meluluskan banyak siswa berprestasi. Namun, tingginya tingkat dropout menjadi tantangan besar bagi institusi ini. Dropout tidak hanya berdampak pada citra dan reputasi, tetapi juga menurunkan kepercayaan publik. Oleh karena itu, institusi berupaya mendeteksi siswa yang berpotensi dropout lebih awal untuk memberikan intervensi yang tepat.

### Permasalahan Bisnis
Beberapa permasalahan bisnis yang perlu diselesaikan dalam proyek ini adalah:
- Tingkat Dropout yang Tinggi: Mendeteksi siswa yang berpotensi melakukan dropout sebelum akhir masa studi mereka, sehingga dapat dilakukan intervensi secara tepat waktu untuk mengurangi angka dropout.
- Monitoring Performa Siswa: Membuat dashboard yang dapat memvisualisasikan performa akademik siswa sehingga pihak manajemen Jaya Jaya Institut dapat memantau kinerja siswa dan mengambil keputusan yang berbasis data untuk meningkatkan kualitas pendidikan.

### Cakupan Proyek

1. Data Collection: Mengumpulkan data karyawan yang telah disediakan oleh Jaya Jaya Maju, yang mencakup informasi demografi, metrik kinerja, dan flag status mahasiswa (Dropout, Graduate).
2. Data Cleaning dan Preprocessing: Melakukan proses pembersihan dan pemrosesan data untuk memastikan bahwa data siap untuk dianalisis. Langkah ini mencakup penanganan missing values, encoding variabel kategorikal, dan normalisasi data jika diperlukan.
3. Exploratory Data Analysis (EDA): Melakukan analisis data eksploratif untuk mendapatkan wawasan awal tentang distribusi Dropout berdasarkan faktor-faktor seperti jenis kelamin, masalah keuangan, dan sebagainya.
4. Modeling dan Prediksi: Mengembangkan model prediktif untuk mengidentifikasi mahasiswa yang berpotensi meninggalkan perusahaan. Model ini dapat menggunakan teknik machine learning Artificial Neural Network.
5. Pembuatan prototipe prediksi ml: Membuat prototipe alat prediksi ml dengan antarmuka yang mudah di gunakan sehingga bisa membantu staff istitusi memeriksa peluang do seorang mahasiswa.
5. Pembuatan Dashboard: Membuat business dashboard yang intuitif dan interaktif menggunakan tool seperti Tableau atau Power BI, yang membantu HR dalam memonitor attrition rate serta faktor-faktor yang mempengaruhinya.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance

Setup environment:
1. Install library penting yang akan di gunakan
```
pip install -r requirements.txt
```
2. Buka notebook untuk melihat pemprosesan data dan modeling
```
notebook.ipnyb
```
3. Jalankan app.py untuk memprediksi dataset karyawan
```
app.py
```
4.  Atur semua variabel dan tekan prediksi untuk mulai prediksi.
5.  Anda juga bisa pergi langsung ke link prototipe ini untuk memprediksi:https://edutech-submission.streamlit.app/
## Business Dashboard

Business dashborad yang di buat dimaksudkan untuk mempermudah staff institusi untuk memantau kinerja mahasiswa dan memantau keadaan yang berkaitan dengan Dropout pada mahasiswa sehingga bisa dilakukan pencegahan.
Link dashboard:
https://public.tableau.com/shared/2JFKD2MCJ?:display_count=n&:origin=viz_share_link

## Conclusion

Berdasarkan hasil analisis, ditemukan bahwa mahasiswa yang berisiko tinggi untuk dropout cenderung berasal dari kelompok yang mengalami masalah finansial. Hal ini terlihat jelas dari data mahasiswa yang memiliki status Debtor (utang pendidikan), di mana sebagian besar dari mereka tidak menyelesaikan studi. Selain itu, kelompok mahasiswa yang sering terlambat membayar biaya kuliah juga memiliki kecenderungan tinggi untuk dropout. Dari sisi program studi, mahasiswa dari program Management (kelas siang dan malam) menunjukkan tingkat dropout yang cukup tinggi, bahkan lebih tinggi dibandingkan tingkat kelulusan mereka.

Analisis juga menunjukkan bahwa mahasiswa yang mengalami dropout cenderung memiliki nilai rata-rata yang rendah. Pada semester 1, nilai rata-rata mahasiswa yang dropout adalah 7.257, dan semakin menurun pada semester 2 menjadi 5.889. Hal ini mengindikasikan adanya masalah akademis yang signifikan sebelum mereka memutuskan atau terpaksa harus berhenti studi.

### Rekomendasi Action Items (Optional)

Untuk mengatasi permasalahan dropout ini dan membantu Jaya Jaya Institut meningkatkan tingkat kelulusan, beberapa langkah berikut dapat dipertimbangkan:

- Menyediakan program bantuan finansial atau beasiswa khusus bagi mahasiswa yang menghadapi kesulitan ekonomi, terutama bagi mereka yang memiliki status Debtor atau sering terlambat membayar biaya kuliah.
- Meningkatkan layanan bimbingan akademik dan psikologis untuk mahasiswa program Management, terutama yang mengikuti kelas siang dan malam, guna membantu mereka menghadapi tantangan akademik dan non-akademik yang mungkin mempengaruhi kelulusan.
- Memberikan bimbingan akademik tambahan kepada mahasiswa dengan nilai rata-rata rendah, terutama di semester awal, agar mereka dapat memperbaiki performa akademik dan tetap termotivasi untuk menyelesaikan studi.

