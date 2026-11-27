# Exercise 18: OOP Polymorphism & Method Overriding for Revit Concrete Takeoff


class BuildingElement:
    def __init__(self, element_id, level):
        self.element_id = element_id
        self.level = level

    def get_base_info(self):
        return f"ID: {self.element_id} | Level: {self.level}"

    def calculate_volume(self):
        return 0.0


class Wall(BuildingElement):
    def __init__(self, element_id, level, length_m, height_m, thickness_m):
        super().__init__(element_id, level)
        self.length_m = length_m
        self.height_m = height_m
        self.thickness_m = thickness_m

    def calculate_volume(self):
        return round(self.length_m * self.height_m * self.thickness_m, 2)

    def __str__(self):
        return f"[Wall] {self.get_base_info()} | Volume: {self.calculate_volume()} m3"


class Slab(BuildingElement):
    def __init__(self, element_id, level, area_m2, thickness_m):
        super().__init__(element_id, level)
        self.area_m2 = area_m2
        self.thickness_m = thickness_m

    def calculate_volume(self):
        return round(self.area_m2 * self.thickness_m, 2)

    def __str__(self):
        return f"[Slab] {self.get_base_info()} | Volume: {self.calculate_volume()} m3"


wall_1 = Wall(101, "L01", 10.0, 3.0, 0.25)
slab_1 = Slab(201, "L01", 40.0, 0.20)
wall_2 = Wall(102, "L02", 6.0, 3.0, 0.20)
slab_2 = Slab(202, "L02", 42.0, 0.25)

concrete_elements = [wall_1, slab_1, wall_2, slab_2]
total_concrete_m3 = 0.0

print("--- REVIT CONCRETE VOLUME TAKEOFF (POLYMORPHISM) ---")
for elem in concrete_elements:
    print(elem)
    total_concrete_m3 += elem.calculate_volume()

print(f"\nTotal Concrete Elements: {len(concrete_elements)}")
print(f"Total Concrete Volume: {round(total_concrete_m3, 2)} m3")
