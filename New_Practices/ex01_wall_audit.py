# Exercise 01: Revit Wall Quantity Takeoff & Thickness Audit

FEET_TO_METERS = 0.3048

raw_walls = [
    {"id": 1001, "type_name": "Exterior - Brick 250mm", "length_ft": 32.8, "height_ft": 10.0, "thickness_mm": "250"},
    {"id": 1002, "type_name": "Interior - Gypsum 100mm", "length_ft": 16.4, "height_ft": 9.8, "thickness_mm": "100"},
    {"id": 1003, "type_name": "Core - Concrete 300mm", "length_ft": 20.0, "height_ft": 11.5, "thickness_mm": "300"},
    {"id": 1004, "type_name": "Interior - Block 150mm", "length_ft": 24.6, "height_ft": 10.0, "thickness_mm": "150"},
    {"id": 1005, "type_name": "Exterior - Concrete 200mm", "length_ft": 40.0, "height_ft": 10.0, "thickness_mm": "200"},
]

heavy_wall_ids = []
total_area_m2 = 0.0

print("--- REVIT WALL AUDIT REPORT ---")

for wall in raw_walls:
    # Convert internal Revit units (feet) to metric (meters)
    length_m = round(wall["length_ft"] * FEET_TO_METERS, 2)
    height_m = round(wall["height_ft"] * FEET_TO_METERS, 2)
    area_m2 = round(length_m * height_m, 2)

    # Accumulate total wall area
    total_area_m2 += area_m2

    # Cast string thickness parameter to integer for comparison
    thickness = int(wall["thickness_mm"])

    # Classify wall based on thickness threshold
    if thickness >= 200:
        category = "Heavy / Structural"
        heavy_wall_ids.append(wall["id"])
    else:
        category = "Light Partition"

    print(f"ID: {wall['id']} | {wall['type_name']} | Area: {area_m2} m2 | Category: {category}")

print("\n--- AUDIT SUMMARY ---")
print(f"Total Walls Audited: {len(raw_walls)}")
print(f"Total Wall Area: {round(total_area_m2, 2)} m2")
print(f"Heavy/Structural Walls Count: {len(heavy_wall_ids)}")
print(f"Heavy Wall IDs: {heavy_wall_ids}")