# Exercise 12: Revit Structural Concrete Column Takeoff Pipeline

raw_columns = [
    {"id": 6001, "level": "L01", "width_ft": 2.0, "depth_ft": 2.0, "height_ft": 10.0},
    {"id": 6002, "level": "L01", "width_ft": 1.5, "depth_ft": 1.5, "height_ft": 10.0},
    {"id": 6003, "level": "L03", "width_ft": 2.0, "depth_ft": 2.5, "height_ft": 12.0},
    {"id": 6004, "level": "L02", "width_ft": None, "depth_ft": 2.0, "height_ft": 10.0},
    {"id": 6005, "level": "L02", "width_ft": 2.0, "depth_ft": 0.0, "height_ft": 10.0},
    {"id": 6006, "level": "L02", "width_ft": 2.5, "depth_ft": 2.5, "height_ft": 12.0},
    {"id": 6007, "level": "L02", "width_ft": 1.5, "depth_ft": 2.0, "height_ft": 11.0},
]


def feet_to_meters(feet_value):
    return round(feet_value * 0.3048, 2)


def calculate_column_metrics(width_ft, depth_ft, height_ft, density=2400.0):
    w_m = feet_to_meters(width_ft)
    d_m = feet_to_meters(depth_ft)
    h_m = feet_to_meters(height_ft)
    volume_m3 = round(w_m * d_m * h_m, 2)
    weight_kg = round(volume_m3 * density, 2)
    return volume_m3, weight_kg


def stream_valid_columns(columns):
    for col in columns:
        w = col["width_ft"]
        d = col["depth_ft"]
        h = col["height_ft"]
        if (w is not None and d is not None and h is not None) and (w > 0 and d > 0 and h > 0):
            yield col


def filter_by_levels(columns, *levels):
    filtered = []
    for col in columns:
        if col["level"] in levels:
            filtered.append(col)
    return filtered


def update_column(column, **new_params):
    for key, value in new_params.items():
        column[key] = value
    return column


def sort_by_volume(columns, descending=True):
    return sorted(columns, key=lambda col: col["volume_m3"], reverse=descending)


# --- Execute Pipeline ---
valid_stream = stream_valid_columns(raw_columns)
target_columns = filter_by_levels(valid_stream, "L01", "L02")

for col in target_columns:
    volume_m3, weight_kg = calculate_column_metrics(
        col["width_ft"], col["depth_ft"], col["height_ft"]
    )
    update_column(
        col,
        volume_m3=volume_m3,
        weight_kg=weight_kg,
        concrete_grade="C30",
        status="Verified",
    )

ranked_columns = sort_by_volume(target_columns, descending=True)

# --- Print Report ---
total_volume = 0.0
total_weight = 0.0

print("--- REVIT CONCRETE COLUMN TAKEOFF REPORT ---")
for rank, col in enumerate(ranked_columns, start=1):
    total_volume += col["volume_m3"]
    total_weight += col["weight_kg"]
    print(
        f"[{rank}] ID: {col['id']} | Level: {col['level']} | "
        f"Volume: {col['volume_m3']} m3 | Weight: {col['weight_kg']} kg | "
        f"Grade: {col['concrete_grade']} ({col['status']})"
    )

print("\n--- STRUCTURAL TAKEOFF SUMMARY ---")
print(f"Total Raw Columns: {len(raw_columns)}")
print(f"Processed Columns (L01 & L02): {len(ranked_columns)}")
print(f"Total Concrete Volume: {round(total_volume, 2)} m3")
print(f"Total Concrete Weight: {round(total_weight, 2)} kg")