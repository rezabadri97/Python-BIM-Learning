with open("room_data.txt","r") as file:
    line_number=0
    for line in file:
        clean_line=line.strip()
        parts=clean_line.split(",")
        
        room_number=parts[0]
        room_name=parts[1]
        level=parts[2]

        line_number+=1
        
        print("*******************")
        print(f"{line_number}- Room Name: {room_name} | Room Number: {room_number} | Level: {level}")
