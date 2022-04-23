while True:
    i=input("Input Data Inventory Baru (ya/tidak)?")
    if i == "ya" or i == "Ya":
        file = open ("db-inventory.txt","a")
        print("*"*40)
        x = input("Input Nama Perangkat :")
        y = input("Input Lokasi :")
        print("-"*40)
        file.write("Nama Perangkat : "+x+", \t Lokasi : "+y+"\n")
        file.close()
    elif i == 'tidak' or i == 'Tidak':
        file = open("db-inventory.txt","r")
        print("*"*40)
        for item in file:
            item = item.strip()
            print(item)
        break