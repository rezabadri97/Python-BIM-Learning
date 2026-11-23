# Exercise 08: Sort Revit rooms by area using lambda and sorted()

rooms = [
    {"number": "101", "name": "Restroom", "area_m2": 6.5},
    {"number": "102", "name": "Open Office", "area_m2": 120.0},
    {"number": "103", "name": "Kitchenette", "area_m2": 14.2},
    {"number": "104", "name": "Conference Room", "area_m2": 45.8},
]


def sort_rooms_by_area(room_list):
    return sorted(room_list, key=lambda room: room["area_m2"], reverse=True)


sorted_rooms = sort_rooms_by_area(rooms)

print("--- REVIT ROOMS SORTED BY AREA (LARGEST FIRST) ---")
for room in sorted_rooms:
    print(f"Room {room['number']} | {room['name']} | Area: {room['area_m2']} m2")