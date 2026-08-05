with open("bim_spaces.txt","w",encoding="utf-8") as file:
    file.write("Entrance Hall\n")
    file.write("Open Office\n")
    file.write("Server Room\n")
    file.write("Mechanical Room\n")
    file.write("Toilet\n")
with open("bim_spaces.txt","r",encoding="utf-8") as file:
    for line in file:
        room_name=line.strip()
        print("Room:", room_name)