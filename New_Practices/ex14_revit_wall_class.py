# Exercise 14: Introduction to OOP - Building a RevitWall class


class RevitWall:
    def __init__(self, element_id, level, length_m, height_m, is_structural=False):
        self.element_id = element_id
        self.level = level
        self.length_m = length_m
        self.height_m = height_m
        self.is_structural = is_structural

    def calculate_area(self):
        return round(self.length_m * self.height_m, 2)

    def get_summary(self):
        area = self.calculate_area()
        role = "Structural" if self.is_structural else "Architectural"
        return f"Wall {self.element_id} | {self.level} | {role} | Area: {area} m2"


# Create wall instances (objects) from the RevitWall class
wall_1 = RevitWall(101, "L01", 6.5, 3.0, is_structural=True)
wall_2 = RevitWall(102, "L01", 4.2, 3.0)
wall_3 = RevitWall(103, "L02", 8.0, 3.5, is_structural=True)

model_walls = [wall_1, wall_2, wall_3]
total_area = 0.0

print("--- REVIT WALLS OOP REPORT ---")
for wall in model_walls:
    print(wall.get_summary())
    total_area += wall.calculate_area()

print(f"\nTotal Walls: {len(model_walls)}")
print(f"Total Wall Area: {round(total_area, 2)} m2")