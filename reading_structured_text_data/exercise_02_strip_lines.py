with open("rooms.txt","r") as file:
    for line in file:
        cleanline=line.strip()
        print(cleanline)