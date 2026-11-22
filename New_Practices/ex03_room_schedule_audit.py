# Exercise 03: Revit Multi-Floor Room Schedule & Area Compliance Audit

AREA_STANDARDS = {
    "Office": (12.0, 25.0),
    "Meeting": (20.0, 45.0),
    "Restroom": (4.0, 10.0),
}

building_floors = [
    {
        "floor_name": "Level 01",
        "rooms": [
            {"number": "101", "name": "Manager Office", "type": "Office", "area_m2": 18.5},
            {"number": "102", "name": "Small Office", "type": "Office", "area_m2": 9.0},
            {"number": "103", "name": "Main Restroom", "type": "Restroom", "area_m2": None},
        ],
    },
    {
        "floor_name": "Level 02",
        "rooms": [
            {"number": "201", "name": "Board Room", "type": "Meeting", "area_m2": 52.0},
            {"number": "202", "name": "Staff Restroom", "type": "Restroom", "area_m2": 6.5},
            {"number": "203", "name": "Duplicate Room", "type": "Office", "area_m2": 0.0},
            {"number": "204", "name": "Team Room", "type": "Meeting", "area_m2": 30.0},
        ],
    },
]

total_valid_area = 0.0
valid_rooms_count = 0
compliant_count = 0
size_issue_count = 0
invalid_rooms = []

print("--- REVIT MULTI-FLOOR ROOM AUDIT ---")

for floor in building_floors:
    floor_name = floor["floor_name"]
    floor_area = 0.0
    print(f"\n=== Auditing {floor_name} ===")

    for room in floor["rooms"]:
        room_num = room["number"]
        room_name = room["name"]
        area = room["area_m2"]

        # Guard against unplaced or unenclosed/redundant Revit rooms
        if area is None:
            print(f"Room {room_num} | {room_name} | Status: INVALID (Not Placed)")
            invalid_rooms.append((floor_name, room_num, "Not Placed"))
            continue

        if area <= 0:
            print(f"Room {room_num} | {room_name} | Status: INVALID (Not Enclosed / Redundant)")
            invalid_rooms.append((floor_name, room_num, "Not Enclosed / Redundant"))
            continue

        # Accumulate valid room metrics
        floor_area += area
        total_valid_area += area
        valid_rooms_count += 1

        # Unpack min and max area thresholds from tuple
        min_area, max_area = AREA_STANDARDS[room["type"]]

        if area < min_area:
            status = "UNDER-SIZED"
            size_issue_count += 1
        elif area > max_area:
            status = "OVER-SIZED"
            size_issue_count += 1
        else:
            status = "COMPLIANT"
            compliant_count += 1

        print(f"Room {room_num} | {room_name} | Area: {area} m2 | Status: {status}")

    print(f">> {floor_name} Total Valid Area: {round(floor_area, 2)} m2")

avg_area = round(total_valid_area / valid_rooms_count, 2) if valid_rooms_count > 0 else 0.0

print("\n--- BUILDING AUDIT SUMMARY ---")
print(f"Total Valid Rooms: {valid_rooms_count}")
print(f"Total Valid Building Area: {round(total_valid_area, 2)} m2")
print(f"Average Valid Room Area: {avg_area} m2")
print(f"Compliant Rooms: {compliant_count}")
print(f"Size Non-Compliant Rooms: {size_issue_count}")
print(f"Invalid Rooms Found ({len(invalid_rooms)}):")

for f_name, r_num, issue in invalid_rooms:
    print(f"  - {f_name} | Room {r_num} | Issue: {issue}")