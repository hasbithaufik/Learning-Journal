def celsius_conv():
    celsius = float(input("Masukkan suhu Celsius: "))
    fahrenheit = float((celsius * 9/5) + 32)
    kelvin = float(celsius + 273.15)
    print(celsius, "Celsius = %.2f" %fahrenheit, "Fahrenheit")
    print(celsius, "Celsius = %.2f" %kelvin, "Kelvin" )

def fahrenheit_conv():
    fahrenheit = float(input("Masukkan suhu Fahrenheit: "))
    celsius = float((fahrenheit - 32) * 5/9)
    kelvin = float((fahrenheit - 31) * 5/9 + 273.15)
    print(fahrenheit, "Fahrenheit = %.2f" %celsius, "Celsius" )
    print(fahrenheit, "Fahrenheit = %.2f" %kelvin, "Kelvin" )

def kelvin_conv():
    kelvin = float(input("Masukkan suhu Kelvin: "))
    celsius = float(kelvin -273.15)
    fahrenheit = float((kelvin - 273.15) * 9/5 + 32)
    print(kelvin, "Kelvin = %.2f" %celsius, "Celsius")
    print(kelvin, "Kelvin = %.2f" %fahrenheit, "Fahrenheit")

print("Pilih suhu apa yang akan dikonversi:")
print("------------------------------------")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")
input_menu = input("Pilih (1/2/3): ")
if input_menu == "1":
    celsius_conv()
elif input_menu == "2":
    fahrenheit_conv()
elif input_menu == "3":
    kelvin_conv()
else:
    print("Menu tidak tersedia. Coba lagi.")


