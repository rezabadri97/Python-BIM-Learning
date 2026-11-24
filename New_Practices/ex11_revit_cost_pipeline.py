# Exercise 11: Combined Revit Audit, Parameter Updater & Cost Takeoff Pipeline

raw_elements = [
    {"id": 5001, "category": "Walls", "length_ft": 30.0, "unit_cost": 150.0},
    {"id": 5002, "category": "Doors", "length_ft": 3.0, "unit_cost": 400.0},
    {"id": 5003, "category": "Windows", "length_ft": 6.0, "unit_cost": 300.0},
    {"id": 5004, "category": "Walls", "length_ft": None, "unit_cost": 150.0},
    {"id": 5005, "category": "Doors", "length_ft": 0.0, "unit_cost": 400.0},
    {"id": 5006, "category": "Walls", "length_ft": 20.0, "unit_cost": 180.0},
    {"id": 5007, "category": "Doors", "length_ft": 6.0, "unit_cost": 350.0},
]


def feet_to_meters(feet_value):
    return round(feet_value * 0.3048, 2)


def calculate_metric_cost(length_ft, unit_cost):
    length_m = feet_to_meters(length_ft)
    total_cost = round(length_m * unit_cost, 2)
    return length_m, total_cost


def stream_valid_elements(elements):
    for elem in elements:
        if elem["length_ft"] is not None and elem["length_ft"] > 0:
            yield elem


def filter_by_categories(elements, *categories):
    filtered = []
    for elem in elements:
        if elem["category"] in categories:
            filtered.append(elem)
    return filtered


def update_element(element, **new_params):
    for key, value in new_params.items():
        element[key] = value
    return element


def sort_by_cost(elements, descending=True):
    return sorted(elements, key=lambda elem: elem["total_cost"], reverse=descending)


# --- Execute Pipeline ---
valid_stream = stream_valid_elements(raw_elements)
target_elements = filter_by_categories(valid_stream, "Walls", "Doors")

for elem in target_elements:
    length_m, total_cost = calculate_metric_cost(elem["length_ft"], elem["unit_cost"])
    update_element(
        elem,
        length_m=length_m,
        total_cost=total_cost,
        status="Approved",
        model="Hospital_Arch.rvt",
    )

ranked_elements = sort_by_cost(target_elements, descending=True)

# --- Print Report ---
grand_total_cost = 0.0

print("--- REVIT COST TAKEOFF REPORT (RANKED) ---")
for rank, elem in enumerate(ranked_elements, start=1):
    grand_total_cost += elem["total_cost"]
    print(
        f"[{rank}] ID: {elem['id']} | {elem['category']} | "
        f"Length: {elem['length_m']} m | Cost: ${elem['total_cost']} | "
        f"Status: {elem['status']} ({elem['model']})"
    )

print("\n--- PIPELINE SUMMARY ---")
print(f"Total Raw Elements: {len(raw_elements)}")
print(f"Processed Valid Elements (Walls & Doors): {len(ranked_elements)}")
print(f"Grand Total Cost: ${round(grand_total_cost, 2)}")