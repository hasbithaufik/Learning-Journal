#membuat kumpulan fungsi rumus konversi suhu-suhu
#kemudian membuat pilihan konversi apa yang akan dijalankan dengan cara memanggil fungsi yang sudah dibuat

#1. fahrenheit > celsius
def fahrcelc():
    fahr = float(input("Suhu Fahrenheit: ")) #error jika tidak float
    cels = (fahr - 32) * 5/9
    print(fahr, "Fahrenheit = %.2f" %cels, "Celsius")

#2. celsius > fahrenheit
def celcfahr():
    cels = float(input("Suhu Celcius: "))
    fahr = (cels * 9/5) + 32
    print(cels, "Celsius = %.2f" %fahr, "Fahrenheit")

#3. celcius > kelvin
def celckelv():
    celc = float(input("Suhu Celcius: "))
    kelv = (cels + 273.15)
    print(cels, "Celsius = %.2f" %kelv, "Kelvin")

#4. kelvin > celcius
def kelvcelc():
    kelv = float(input("Suhu Kelvin: "))
    celc = kelv - 273.15
    print(kelv, "Kelvin = %.2f" %celc, "Celsius")

#5. fahrenheit > kelvin
def fahrkelv():
    fahr = float(input("Suhu Fahrenheit: "))
    kelv = (fahr -31) * 5/9 + 273.15
    print(fahr, "Fahrenheit = %.2f" %fahr, "Fahrenheit")

#6. kelvin > fahrenheit
def kelvfahr():
    kelv = float(input("Suhu Kelvin: "))
    fahr = (kelv - 273.15) * 9/5 + 32
    print(kelv, "Kelvin = %.2f" %fahr, "Fahrenheit")

#menu menggunakan if
print("Pilih Suhu apa yang akan dikonversi: ")
print("-----------------------------------")
print("1. Fahrenheit ke Celsius")
print("2. Celsius ke Fahrenheit")
print("3. Celsius ke Kelvin")
print("4. Kelvin ke Celsius")
print("5. Kelvin ke Fahrenheit")
print("6. Fahrenheit ke Kelvin")
print("-----------------------------------")
print("Silahkan Pilih Menu (1-6)")
input_menu = input("Pilih Menu: ")
if input_menu == "1":
    fahrcelc()
elif input_menu == "2":
    celcfahr()
elif input_menu == "3":
    celckelv()
elif input_menu == "4":
    kelvcelc()
elif input_menu == "5":
    kelvfahr()
elif input_menu == "6":
    fahrkelv()
else:
    print("Menu Tidak Tersedia. Coba lagi")