# Exercise 13: Revit Window Glazing Area & Thermal Heat Loss Audit Pipeline

raw_windows = [
    {"id": 7001, "orientation": "South", "width_ft": 6.0, "height_ft": 5.0, "u_value": 1.2},
    {"id": 7002, "orientation": "North", "width_ft": 4.0, "height_ft": 5.0, "u_value": 1.6},
    {"id": 7003, "orientation": "West", "width_ft": 8.0, "height_ft": 6.0, "u_value": 2.1},
    {"id": 7004, "orientation": "South", "width_ft": None, "height_ft": 5.0, "u_value": 1.3},
    {"id": 7005, "orientation": "West", "width_ft": 5.0, "height_ft": 0.0, "u_value": 1.8},
    {"id": 7006, "orientation": "South", "width_ft": 10.0, "height_ft": 7.0, "u_value": 1.5},
    {"id": 7007, "orientation": "South", "width_ft": 5.0, "height_ft": 5.0, "u_value": None},
    {"id": 7008, "orientation": "West", "width_ft": 4.0, "height_ft": 4.0, "u_value": 1.0},
]


def feet_to_meters(feet_value):
    return round(feet_value * 0.3048, 2)


def stream_valid_windows(windows):
    for win in windows:
        w = win["width_ft"]
        h = win["height_ft"]
        u = win["u_value"]
        if (w is not None and h is not None and u is not None) and (w > 0 and h > 0 and u > 0):
            yield win


def filter_by_orientations(windows, *orientations):
    filtered = []
    for win in windows:
        if win["orientation"] in orientations:
            filtered.append(win)
    return filtered


def calculate_window_metrics(width_ft, height_ft, u_value, temp_diff=20.0):
    w_m = feet_to_meters(width_ft)
    h_m = feet_to_meters(height_ft)
    area_m2 = round(w_m * h_m, 2)
    heat_loss_w = round(area_m2 * u_value * temp_diff, 2)
    return area_m2, heat_loss_w


def update_window(window, **new_params):
    for key, value in new_params.items():
        window[key] = value
    return window


def sort_by_heat_loss(windows, descending=True):
    return sorted(windows, key=lambda win: win["heat_loss_w"], reverse=descending)


# --- Execute Pipeline ---
valid_stream = stream_valid_windows(raw_windows)
target_windows = filter_by_orientations(valid_stream, "South", "West")

for win in target_windows:
    area_m2, heat_loss_w = calculate_window_metrics(
        win["width_ft"], win["height_ft"], win["u_value"]
    )
    status = "Efficient" if win["u_value"] <= 1.4 else "Needs Upgrade"
    update_window(
        win,
        area_m2=area_m2,
        heat_loss_w=heat_loss_w,
        audit_phase="Energy Check",
        energy_status=status,
    )

ranked_windows = sort_by_heat_loss(target_windows, descending=True)

# --- Print Report ---
total_glazing_area = 0.0
total_heat_loss = 0.0
upgrade_count = 0

print("--- REVIT WINDOW THERMAL AUDIT REPORT ---")
for rank, win in enumerate(ranked_windows, start=1):
    total_glazing_area += win["area_m2"]
    total_heat_loss += win["heat_loss_w"]
    if win["energy_status"] == "Needs Upgrade":
        upgrade_count += 1
    print(
        f"[{rank}] ID: {win['id']} | {win['orientation']} | "
        f"Area: {win['area_m2']} m2 | Heat Loss: {win['heat_loss_w']} W | "
        f"Status: {win['energy_status']} ({win['audit_phase']})"
    )

print("\n--- THERMAL AUDIT SUMMARY ---")
print(f"Total Raw Windows: {len(raw_windows)}")
print(f"Processed Windows (South & West): {len(ranked_windows)}")
print(f"Total Glazing Area: {round(total_glazing_area, 2)} m2")
print(f"Total Heat Loss: {round(total_heat_loss, 2)} W")
print(f"Windows Needing Upgrade: {upgrade_count}")