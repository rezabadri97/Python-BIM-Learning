# Exercise 05: Modular Revit Wall Finish Area & Cost Estimator

from typing import Optional, Tuple

FEET_TO_METERS = 0.3048

FINISH_UNIT_PRICES = {
    "Paint": 12.0,
    "Tile": 35.0,
    "Plaster": 18.0,
}

raw_walls = [
    {"id": 3001, "name": "Living Room North", "length_ft": 26.25, "height_ft": 9.84, "openings_m2": 4.0, "finish_type": "Paint"},
    {"id": 3002, "name": "Kitchen Wet Wall", "length_ft": 16.4, "height_ft": 9.84, "openings_m2": 2.0, "finish_type": "Tile"},
    {"id": 3003, "name": "Corridor Partition", "length_ft": 32.8, "height_ft": 11.48, "openings_m2": 5.0, "finish_type": "Plaster"},
    {"id": 3004, "name": "Broken Wall Model", "length_ft": 0.0, "height_ft": 9.84, "openings_m2": 0.0, "finish_type": "Paint"},
    {"id": 3005, "name": "Oversized Opening Error", "length_ft": 13.12, "height_ft": 9.84, "openings_m2": 15.0, "finish_type": "Paint"},
]


def feet_to_meters(value_ft: float, decimals: int = 2) -> float:
    """Convert Revit internal imperial length (feet) to metric meters."""
    return round(value_ft * FEET_TO_METERS, decimals)


def calculate_wall_areas(
    length_ft: float,
    height_ft: float,
    openings_m2: float = 0.0,
) -> Optional[Tuple[float, float]]:
    """Calculate gross and net wall areas in m2, returning None if geometry is invalid."""
    # Guard clause 1: check valid positive wall dimensions
    if length_ft <= 0 or height_ft <= 0:
        return None

    length_m = feet_to_meters(length_ft)
    height_m = feet_to_meters(height_ft)
    gross_area_m2 = round(length_m * height_m, 2)

    # Guard clause 2: ensure openings area does not exceed gross wall area
    if openings_m2 < 0 or openings_m2 > gross_area_m2:
        return None

    net_area_m2 = round(gross_area_m2 - openings_m2, 2)
    return gross_area_m2, net_area_m2


def estimate_finish_cost(
    net_area_m2: float,
    unit_price: float,
    waste_factor: float = 0.10,
) -> float:
    """Estimate wall finish cost including material waste percentage."""
    area_with_waste = net_area_m2 * (1 + waste_factor)
    return round(area_with_waste * unit_price, 2)


total_net_area = 0.0
total_cost = 0.0
invalid_wall_ids = []

print("--- REVIT WALL FINISHES & COST ESTIMATOR ---")

for wall in raw_walls:
    wall_id = wall["id"]
    wall_name = wall["name"]
    finish = wall["finish_type"]

    areas = calculate_wall_areas(
        wall["length_ft"],
        wall["height_ft"],
        wall["openings_m2"],
    )

    if areas is None:
        print(f"ID: {wall_id} | {wall_name} | Status: INVALID GEOMETRY (Skipped)")
        invalid_wall_ids.append(wall_id)
        continue

    gross_area, net_area = areas
    unit_price = FINISH_UNIT_PRICES[finish]

    if finish == "Tile":
        cost = estimate_finish_cost(net_area, unit_price, waste_factor=0.15)
    else:
        cost = estimate_finish_cost(net_area, unit_price)

    total_net_area += net_area
    total_cost += cost

    print(
        f"ID: {wall_id} | {wall_name} | Gross: {gross_area} m2 | "
        f"Net: {net_area} m2 | Finish: {finish} | Cost: ${cost}"
    )

valid_walls_count = len(raw_walls) - len(invalid_wall_ids)

print("\n--- ESTIMATION SUMMARY ---")
print(f"Valid Walls Processed: {valid_walls_count}")
print(f"Invalid Walls Skipped: {len(invalid_wall_ids)} (IDs: {invalid_wall_ids})")
print(f"Total Net Finish Area: {round(total_net_area, 2)} m2")
print(f"Total Estimated Cost: ${round(total_cost, 2)}")