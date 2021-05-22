print("Menghitung Luas Persegi Panjang")
print("-------------------------------")

size1 = input("Input panjang: ")
try:
    panjang = int(size1)
except:
    print("Error, please use numeric digits.")
if panjang<1:
    print("Error, please enter a positive numbers.")

size2 = input("Input lebar: ")
try:
    lebar = int(size2)
except:
    print("Error, please use numeric digits.")
if lebar<1:
    print("Error, please enter a positive numbers.")

luas = panjang * lebar

print(f"Luas Persegi Panjang = {luas}")
if luas<1:
    print("The result should be a positive numbers.")