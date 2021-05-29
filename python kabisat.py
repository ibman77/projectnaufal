tahun = int(input("Input Tahun: "))

if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print("Adalah Tahun Kabisat")
        else:
            print("Bukan Tahun Kabisat")
    else:
        print("Adalah Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")