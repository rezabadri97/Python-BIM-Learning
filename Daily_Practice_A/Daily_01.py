rooms = [
    {"number": "101", "name": "Lobby", "area": 35.5, "level": "Level 1", "is_placed": True},
    {"number": "102", "name": "Office", "area": 18.0, "level": "Level 1", "is_placed": True},
    {"number": "103", "name": "Storage", "area": 0, "level": "Level 1", "is_placed": False},
    {"number": "201", "name": "Meeting Room", "area": 42.3, "level": "Level 2", "is_placed": True},
    {"number": "202", "name": "WC", "area": 6.5, "level": "Level 2", "is_placed": True},
    {"number": "203", "name": "Server Room", "area": -5, "level": "Level 2", "is_placed": True}
]


def get_room_status(room):
    if room["is_placed"] == False:
        return "NOT PLACED"
    elif room["area"] <= 0:
        return "INVALID AREA"
    else:
        return "OK"


total_rooms = 0
ok_rooms = 0
not_placed_rooms = 0
invalid_area_rooms = 0
total_valid_area = 0

print("=== ROOM REPORT ===")

for room in rooms:
    total_rooms += 1

    status = get_room_status(room)

    print(f'Room {room["number"]} - {room["name"]} - {room["level"]} - Area: {room["area"]} sqm - Status: {status}')

    if status == "OK":
        ok_rooms += 1
        total_valid_area += room["area"]
    elif status == "NOT PLACED":
        not_placed_rooms += 1
    elif status == "INVALID AREA":
        invalid_area_rooms += 1

print()
print("=== SUMMARY ===")
print(f"Total rooms: {total_rooms}")
print(f"OK rooms: {ok_rooms}")
print(f"Not placed rooms: {not_placed_rooms}")
print(f"Invalid area rooms: {invalid_area_rooms}")
print(f"Total valid area: {total_valid_area} sqm")

print()
print("=== LEVEL 2 ROOMS ===")

for room in rooms:
    if room["level"] == "Level 2":
        print(f'Room {room["number"]} - {room["name"]} - Area: {room["area"]} sqm')
