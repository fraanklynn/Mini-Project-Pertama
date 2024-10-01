### Nama : Franklyn Galvin Lodo
### flowchart
![Franklyn Galvin 2409116047 (2)](https://github.com/user-attachments/assets/08d68f9c-1ae6-4b92-bf2d-e55033e3b69f)
## baris 1-3 perkenalan identitas mahasiswa 
### memakai 
### print("Nama: Franklyn Galvin Lodo            ")
### print("NIM: 2409116047                       ")
### print("Tugas Praktikum Dasar-Dasar Pemograman")
### Login sederhana
## baris 1-4 menerapkan login sederhana dengan input nama dan nim memakai input
### isi_nama = input("Masukkan nama:")
### isi_NIM = input("Masukkan NIM:")
### nama = "Franklyn Galvin Lodo"
### NIM = "2409116047"
## selanjutnya memakai (if ==) agar login berhasil dan jika salah outputnya akan berbeda
### if isi_nama == nama and isi_NIM == NIM:
### print("Login Berhasil!")
## Selanjutnya memakai indikator lanjut = 'yes' agar saat memakai while/looping tidak salah
### lanjut = 'yes'
## Menghitung Gaji Karyawan
## while lanjut == yes adalah loopingnya
### while lanjut == 'yes':
## baris 1-3 pengisian jam kerja, tarif kerja , dan gaji karyawan memakai float mengapa? jika jam kerja memakai koma maka tarif kerja akan disesuaikan
### jam_kerja = float(input("Masukkan jam kerja:"))
### tarif_kerja = float(input("Masukkan tarif kerja:"))
### gaji_karyawan = jam_kerja * tarif_kerja
## selanjutnya jika jam kerja di atas 160 maka akan ada bonus tarif kerja sebesar 10% codingnya seperti dibawah
### if jam_kerja > 160:
### total_gaji = gaji_karyawan + gaji_karyawan * 0.10
### print("Total gaji karyawan:")
### print(total_gaji)
## selanjutnya memakai elif karna jika ada jam kerja diatas 0 dan dibawah 160 maka gaji dibayar sesuai tarif kerja
### elif jam_kerja > 0:
### gaji = gaji_karyawan
### print("Total gaji karyawan:")
### print(gaji)
## selanjutnya jika ada karyawan yang tidak bekerja atau jam kerja dibawah 0/minus maka gaji tidak dapat dibayar
### else:
### print("gaji tidak dapat dibayar")
## lalu ulang = input lagi untuk mengetahui ingin menghitung gaji karyawan lagi atau tidak 
### ulang= input("Apakah masih ingin menghitung gaji karyawan lagi? (yes/no):")
## jika yes maka akan otomatis mengulang dari input jam kerja 
### if ulang == 'yes':
### lanjut = 'yes'
## jika no maka akan keluar dari program 
### else:
### lanjut = 'no'
### print("Terimakasih sudah menghitung gaji karyawan")
## jika nama atau nim salah maka login akan gagal
### else:
### print("Login Gagal, Nama atau NIM salah")

### output jika jam kerja diatas 160
![Screenshot 2024-09-30 224549](https://github.com/user-attachments/assets/929d3812-af8e-486d-8ffa-8cb229a1931f)

### output jika jam kerja dibawah 160
![Screenshot 2024-09-30 224748](https://github.com/user-attachments/assets/b84a39e0-4318-4898-9fec-8261d2569527)

### output pengulangan dan jika tidak mengulang
![Screenshot 2024-09-30 224842](https://github.com/user-attachments/assets/33a3b742-a0ac-485e-b959-edc8de2a7499)

### output login sederhana kalau benar
![Screenshot 2024-09-30 225004](https://github.com/user-attachments/assets/204fd0dc-b6a3-4ecb-a73a-1c72254f915a)

### output login jika salah
![Screenshot 2024-09-30 225101](https://github.com/user-attachments/assets/d9053fc7-25ae-40b3-b644-a0721154708f)


