# Exercise 19: @staticmethod (Unit Converter) and @classmethod (Imperial Factory)


class RevitWall:
    def __init__(self, element_id, level, length_m, height_m):
        self.element_id = element_id
        self.level = level
        self.length_m = length_m
        self.height_m = height_m

    @staticmethod
    def feet_to_meters(feet_value):
        return round(feet_value * 0.3048, 2)

    @classmethod
    def from_imperial(cls, element_id, level, length_ft, height_ft):
        length_m = cls.feet_to_meters(length_ft)
        height_m = cls.feet_to_meters(height_ft)
        return cls(element_id, level, length_m, height_m)

    def calculate_area(self):
        return round(self.length_m * self.height_m, 2)

    def __str__(self):
        return (
            f"Wall {self.element_id} | {self.level} | "
            f"{self.length_m}m x {self.height_m}m | Area: {self.calculate_area()} m2"
        )


# 1. Call @staticmethod directly on the class (no wall object needed)
sample_m = RevitWall.feet_to_meters(10.0)
print(f"Quick Conversion: 10.0 ft = {sample_m} m")

# 2. Create walls using both normal __init__ (metric) and @classmethod (imperial)
wall_1 = RevitWall(101, "L01", 6.0, 3.0)
wall_2 = RevitWall.from_imperial(102, "L01", 15.0, 10.0)
wall_3 = RevitWall.from_imperial(103, "L02", 25.0, 12.0)

model_walls = [wall_1, wall_2, wall_3]
total_area = 0.0

print("\n--- REVIT WALLS REPORT (METRIC & IMPERIAL INPUTS) ---")
for wall in model_walls:
    print(wall)
    total_area += wall.calculate_area()

print(f"\nTotal Walls: {len(model_walls)}")
print(f"Total Wall Area: {round(total_area, 2)} m2")