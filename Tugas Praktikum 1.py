print("--------------------------------------")
print("Nama: Franklyn Galvin Lodo            ")
print("NIM: 2409116047                       ")
print("Tugas Praktikum Dasar-Dasar Pemograman")
print("--------------------------------------")

#Login sederhana
nama = "Franklyn Galvin Lodo"
NIM = "2409116047"

isi_nama = input("Masukkan nama:")
isi_NIM = input("Masukkan NIM:")

if isi_nama == nama and isi_NIM == NIM:
    print("Login Berhasil!")
    lanjut = 'yes'
    #Menghitung Gaji Karyawan
    while lanjut == 'yes':
        jam_kerja = float(input("Masukkan jam kerja:"))
        tarif_kerja = float(input("Masukkan tarif kerja:"))
        gaji_karyawan = jam_kerja * tarif_kerja
        if jam_kerja > 160:
            total_gaji = gaji_karyawan + gaji_karyawan * 0.10
            print("Total gaji karyawan:")
            print(total_gaji)
        elif jam_kerja > 0:
            gaji = gaji_karyawan
            print("Total gaji karyawan:")
            print(gaji)
        else:
            print("gaji tidak dapat dibayar")
        ulang= input("Apakah masih ingin menghitung gaji karyawan lagi? (yes/no):")
        if ulang == 'yes':
            lanjut = 'yes'
        else:
            lanjut = 'no'
            print("Terimakasih sudah menghitung gaji karyawan")
else:
    print("Login Gagal, Nama atau NIM salah")