# Exercise 02: Revit Door QA/QC Audit & Duplicate Mark Detection

raw_doors = [
    {"id": 2001, "mark": " D-101 ", "level": "Level 1", "fire_rating_min": 60},
    {"id": 2002, "mark": "d-102", "level": "Level 1", "fire_rating_min": 0},
    {"id": 2003, "mark": "D-101", "level": "Level 1", "fire_rating_min": 90},
    {"id": 2004, "mark": "", "level": "Level 2", "fire_rating_min": 60},
    {"id": 2005, "mark": "D-201", "level": "Level 2", "fire_rating_min": 120},
    {"id": 2006, "mark": "   ", "level": "Level 2", "fire_rating_min": 0},
    {"id": 2007, "mark": "d-201 ", "level": "Level 3", "fire_rating_min": 30},
    {"id": 2008, "mark": "D-301", "level": "Level 3", "fire_rating_min": 90},
]

seen_marks = set()
duplicate_marks = set()
missing_mark_ids = []
duplicate_door_ids = []
doors_per_level = {}

print("--- REVIT DOOR QA/QC AUDIT ---")

for door in raw_doors:
    # Normalize mark parameter by stripping spaces and converting to uppercase
    clean_mark = door["mark"].strip().upper()

    # Validate mark status
    if clean_mark == "":
        status = "MISSING MARK"
        missing_mark_ids.append(door["id"])
        clean_mark = "N/A"
    elif clean_mark in seen_marks:
        status = "DUPLICATE MARK"
        duplicate_marks.add(clean_mark)
        duplicate_door_ids.append(door["id"])
    else:
        status = "VALID"
        seen_marks.add(clean_mark)

    # Count doors grouped by Revit level
    level = door["level"]
    if level in doors_per_level:
        doors_per_level[level] += 1
    else:
        doors_per_level[level] = 1

    print(f"ID: {door['id']} | Mark: {clean_mark} | Level: {level} | Status: {status}")

# Filter fire-rated doors (60 min or higher) using list comprehension
fire_rated_ids = [door["id"] for door in raw_doors if door["fire_rating_min"] >= 60]

print("\n--- QA/QC SUMMARY ---")
print(f"Total Doors Audited: {len(raw_doors)}")
print("Doors Count Per Level:")
for level, count in doors_per_level.items():
    print(f"  - {level}: {count} doors")

print(f"Missing Mark Door IDs: {missing_mark_ids}")
print(f"Duplicate Marks Found: {sorted(duplicate_marks)}")
print(f"Duplicate Mark Door IDs: {duplicate_door_ids}")
print(f"Fire-Rated Doors (>= 60 min) IDs: {fire_rated_ids}")