with open("raw_rooms.txt","r")as file:
    line_number=0
    for line in file:
        clean_line=line.strip()
        if clean_line=="":
            continue
        parts=clean_line.split(",")
        if len(parts)<3:
            continue
        room_number=parts[0].strip()
        room_name=parts[1].strip().title()
        room_level=parts[2].strip().title()
        line_number+=1
        print("-"*80)
        print(f"{line_number}-Room Number: {room_number} | Room Name: {room_name} | Room Level:{room_level}")