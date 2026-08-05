def check_room(room):
    room_number=room[0]
    room_name=room[1]
    level=room[2]


    if room_name.strip()=="":
        return f"Room {room_number}: Missing Name"
    elif level.strip()=="":
        return f"Room {room_number}: Missing Level"
    else:
        return f"Room {room_number}: OK"
    



rooms = [
    ["101", "", "Level 1"],
    ["102", "Meeting Room", ""],
    ["103", "Storage", "Level 2"]
]

with open("Report01.txt","w") as file:
    file.write("="*40+"\n")
    file.write("\n")
    file.write("Room Report\n")
    file.write("\n")
    file.write("="*40+"\n")
    file.write("\n")
    file.write("Detailed Result\n ")
    file.write("\n")

    for room in rooms:
        result=check_room(room)
        file.write(result+"\n")
    file.write("\n")
    file.write("="*40+"\n")
    name_issue=0
    level_issue=0
    item_checked=0
    for room in rooms:
        if room[1].strip()=="":
            name_issue+=1
        
        if room[2].strip()=="":
            level_issue+=1
        item_checked+=1
    file.write("\n")
    file.write("Summary\n")
    file.write("\n")
    file.write(f"Total Item checked: {item_checked}\n")
    file.write("\n")
    file.write(f"Name Issues:{name_issue}\n")
    file.write("\n")
    file.write(f"Level Issues: {level_issue}\n")
    file.write("\n")
    file.write("="*40+"\n")
    file.write("\n")
    file.write("End of The Report\n")
    file.write("\n")
    file.write("="*40+"\n")