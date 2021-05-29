user_input = int(input("Masukkan angka :"))

k = 1

for i in range(0, user_input):
    for j in range(0, k):
        print(" * ", end = "")
        
    k = k + 1
    
    print()