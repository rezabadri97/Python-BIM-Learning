def parse_room_line(line, line_no):
    raw = line.strip()
    if not raw:
        raise ValueError("Empty line")

    if "|" not in raw:
        raise ValueError("Missing separator '|'")

    name, area_text = raw.split("|", 1)
    name = name.strip()
    area_text = area_text.strip()

    if not name:
        raise ValueError("Room name is empty")

    try:
        area = float(area_text)
    except ValueError:
        raise ValueError(f"Area is not a number: {area_text}")

    if area <= 0:
        raise ValueError(f"Area must be > 0, got {area}")

    return {"name": name, "area": area}


valid_rooms = []
errors = []

path = "data/rooms_raw.txt"
with open(path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        try:
            room = parse_room_line(line, i)
            valid_rooms.append(room)
        except ValueError as e:
            errors.append(f"Line {i}: {e} | raw={line.strip()}")

print("Valid rooms:", len(valid_rooms))
print("Errors:", len(errors))
for err in errors:
    print(" -", err)
