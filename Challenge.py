##Challenge 1

##Challenge 2
sisiAtas = input("masukan sisiAtas :")
sisiBawah = input("masukan sisiBawah :")
tinggi = input("masukan tinggi :")

Luas = int(int(tinggi)*int(sisiAtas + sisiBawah)/2)
print(int(Luas))

##Challenge 3
nilai = input("masukkan nilai ")
nilai = int(nilai)
if nilai >100:
    print("nilai yang dimasukkan 0-100")
elif nilai >80:
    print("nilai A")
elif nilai >60:
    print("nilai B")
elif nilai >40:
    print("nilai C")
elif nilai >20:
    print("nilai D")
elif nilai >0:
    print("nilai E")
else:
    print("Nilai yang dimasukkan 0-100")
    
##Challenge 4
pembeli = input("Masukan jumlah belanja : ")
pembeli = int(pembeli)
if pembeli >= 100000:
    diskon = 10/100
else :
    diskon = 5/100
hitung = pembeli * diskon
total = pembeli - hitung
print("diskon :",hitung)
print("harga setelah diskon :", total)