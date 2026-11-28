# Exercise 20: OOP Composition (RevitModel Has-A Elements) combined with Inheritance,
# Polymorphism, @property, @staticmethod, @classmethod, yield, *args, and lambda.


class BuildingElement:
    def __init__(self, element_id, level):
        self.element_id = element_id
        self.level = level

    @staticmethod
    def feet_to_meters(feet_value):
        return round(feet_value * 0.3048, 2)

    def get_base_info(self):
        return f"ID: {self.element_id} | Level: {self.level}"

    def calculate_volume(self):
        return 0.0


class Wall(BuildingElement):
    def __init__(self, element_id, level, length_m, height_m, thickness_m):
        super().__init__(element_id, level)
        self.length_m = length_m
        self.height_m = height_m
        self._thickness_m = thickness_m

    @property
    def thickness_m(self):
        return self._thickness_m

    @thickness_m.setter
    def thickness_m(self, new_thickness):
        if new_thickness <= 0:
            print(
                f"[WARNING] Wall {self.element_id}: "
                f"Thickness must be > 0. Update rejected ({new_thickness} m)."
            )
        else:
            self._thickness_m = new_thickness

    @classmethod
    def from_imperial(cls, element_id, level, length_ft, height_ft, thickness_ft):
        length_m = cls.feet_to_meters(length_ft)
        height_m = cls.feet_to_meters(height_ft)
        thickness_m = cls.feet_to_meters(thickness_ft)
        return cls(element_id, level, length_m, height_m, thickness_m)

    def calculate_volume(self):
        return round(self.length_m * self.height_m * self._thickness_m, 2)

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


class RevitModel:
    def __init__(self, project_name):
        self.project_name = project_name
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def stream_by_levels(self, *levels):
        for elem in self.elements:
            if elem.level in levels:
                yield elem

    def get_total_volume(self):
        total = 0.0
        for elem in self.elements:
            total += elem.calculate_volume()
        return round(total, 2)

    @staticmethod
    def sort_by_volume(elements, descending=True):
        return sorted(elements, key=lambda elem: elem.calculate_volume(), reverse=descending)


# --- Create Elements ---
wall_1 = Wall(101, "L01", 10.0, 3.0, 0.25)
wall_1.thickness_m = -0.1  # Trigger setter guard

wall_2 = Wall.from_imperial(102, "L02", 20.0, 10.0, 1.0)
slab_1 = Slab(201, "L01", 40.0, 0.20)
slab_2 = Slab(202, "L03", 50.0, 0.25)
slab_3 = Slab(203, "L02", 35.0, 0.20)

# --- Compose Model ---
model = RevitModel("Tower_Struct.rvt")
model.add_element(wall_1)
model.add_element(wall_2)
model.add_element(slab_1)
model.add_element(slab_2)
model.add_element(slab_3)

# --- Query & Rank ---
target_stream = model.stream_by_levels("L01", "L02")
ranked_elements = RevitModel.sort_by_volume(target_stream, descending=True)

filtered_volume = 0.0

print(f"\n--- REVIT MODEL REPORT: {model.project_name} (L01 & L02) ---")
for rank, elem in enumerate(ranked_elements, start=1):
    filtered_volume += elem.calculate_volume()
    print(f"[{rank}] {elem}")

print("\n--- MODEL SUMMARY ---")
print(f"Total Elements in Model: {len(model.elements)}")
print(f"Total Model Concrete Volume: {model.get_total_volume()} m3")
print(f"Filtered Elements (L01 & L02): {len(ranked_elements)}")
print(f"Filtered Concrete Volume: {round(filtered_volume, 2)} m3")
