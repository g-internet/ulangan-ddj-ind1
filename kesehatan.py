a = int(input("masukan jumlah pasien: "))
for i in range(a):
    nama = (input("masukan nama anda: "))
    bb = float(input("masukan Berat Badan kamu(Kg): "))
    tb = float(input("masukan tinggi badan anda(m): "))

    bmi = bb / tb
    
    print(bmi)

    if bmi < 18.5:
        print("waduh kamu kurus, makan sama olahraga yang Tepat ya!")
    elif 18.5 <= bmi and bmi < 26:
        print("nah ginikan Normal pas gitu lohh")
    elif 26 < bmi and bmi < 30:
        print("Kamu kelebihan berat bedan, kurangin makan banyak nya ya")
    else:
        print("Waduh kamu obesitas, coba mulai diet dan olahraga yang cukup ya !")

    print ("Hai",nama , "bmi Kamu itu " , bmi)