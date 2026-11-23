# Exercise 10: Stream invalid Revit rooms one by one using a generator (yield)

model_rooms = [
    {"number": "101", "name": "Lobby", "area_m2": 45.0},
    {"number": "102", "name": "Storage", "area_m2": None},
    {"number": "103", "name": "Office", "area_m2": 18.5},
    {"number": "104", "name": "Corridor", "area_m2": 0.0},
    {"number": "105", "name": "Meeting Room", "area_m2": 32.0},
]


def find_invalid_rooms(room_list):
    for room in room_list:
        if room["area_m2"] is None or room["area_m2"] <= 0:
            yield room


print("--- INVALID REVIT ROOMS STREAM ---")
for bad_room in find_invalid_rooms(model_rooms):
    print(f"Room {bad_room['number']} | {bad_room['name']} | Area Value: {bad_room['area_m2']}")