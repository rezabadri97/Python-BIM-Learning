# Drill 02 (ex22): RevitDoor Static/Class Methods & Level Stream Filter


class RevitDoor:
    def __init__(self, mark, level, width_m):
        self.mark = mark
        self.level = level
        self.width_m = width_m

    @staticmethod
    def feet_to_meters(feet_value):
        return round(feet_value * 0.3048, 2)

    @classmethod
    def from_imperial(cls, mark, level, width_ft):
        width_m = cls.feet_to_meters(width_ft)
        return cls(mark, level, width_m)

    def __str__(self):
        return f"Door {self.mark} | Level: {self.level} | Width: {self.width_m} m"


def stream_doors_by_levels(doors, *levels):
    for door in doors:
        if door.level in levels:
            yield door


# Create actual RevitDoor objects (metric and imperial)
door_1 = RevitDoor("D-101", "L01", 0.9)
door_2 = RevitDoor.from_imperial("D-102", "L01", 3.5)
door_3 = RevitDoor("D-301", "L03", 1.2)
door_4 = RevitDoor.from_imperial("D-201", "L02", 3.0)

all_doors = [door_1, door_2, door_3, door_4]

target_doors = stream_doors_by_levels(all_doors, "L01", "L02")
matched_count = 0

print("--- FILTERED REVIT DOORS (L01 & L02) ---")
for rank, door in enumerate(target_doors, start=1):
    matched_count += 1
    print(f"[{rank}] {door}")

print(f"\nTotal Doors in Model: {len(all_doors)}")
print(f"Filtered Doors (L01 & L02): {matched_count}")