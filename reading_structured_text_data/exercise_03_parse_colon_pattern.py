with open("rooms.txt", "r") as file:
    for line in file:
        cleanLine=line.strip()
        parts=cleanLine.split(":")
        key=parts[0]
        value=parts[1]
        print(f"Key: {key} | Value: {value}")