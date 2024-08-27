import time

a = int(input("masukan jumlah siswa: "))

for i in range(a):
    nama = (input("masukan nama siswa / siswi: "))
    t1 = float(input("masukan nilai tugas ke 1 anda: "))
    t2 = float(input("Masukan nilai Tugas ke 2 anda: "))
    t3 = float(input("masukan nilai tugas ke 3 anda: "))

    b = 3

    all = t1 + t2 + t3

    avv = all // b

    if avv >=70:
        print("Kamu lulus tetap pertahankan ya!")
    elif avv >= 50 and avv <= 69:
        print("waduh nilai kamu hrus ada perbaikan, tetap semangat ya!")
    else:
        print("waduh kamu belum lulus, jangan lupa belajar lagi ya")

    time.sleep(1)
    print ("selamat ya ", nama, "nilai rata rata kamu itu = ",avv, "Tetap semangat Belajar YAAAA!")

