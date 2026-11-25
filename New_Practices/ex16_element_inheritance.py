# Exercise 16: OOP Inheritance and super() with Revit BuildingElement, Wall, and Door


class BuildingElement:
    def __init__(self, element_id, level):
        self.element_id = element_id
        self.level = level

    def get_base_info(self):
        return f"ID: {self.element_id} | Level: {self.level}"


class Wall(BuildingElement):
    def __init__(self, element_id, level, length_m, height_m):
        super().__init__(element_id, level)
        self.length_m = length_m
        self.height_m = height_m

    def calculate_area(self):
        return round(self.length_m * self.height_m, 2)

    def __str__(self):
        return f"[Wall] {self.get_base_info()} | Area: {self.calculate_area()} m2"


class Door(BuildingElement):
    def __init__(self, element_id, level, mark, fire_rating_min):
        super().__init__(element_id, level)
        self.mark = mark
        self.fire_rating_min = fire_rating_min

    def is_fire_rated(self):
        return self.fire_rating_min >= 60

    def __str__(self):
        status = "Fire-Rated" if self.is_fire_rated() else "Standard"
        return f"[Door] {self.get_base_info()} | Mark: {self.mark} | Status: {status}"


wall_1 = Wall(101, "L01", 6.0, 3.0)
door_1 = Door(201, "L01", "D-101", 90)
wall_2 = Wall(102, "L02", 4.5, 3.2)
door_2 = Door(202, "L02", "D-201", 0)

model_elements = [wall_1, door_1, wall_2, door_2]

print("--- REVIT MODEL ELEMENTS (INHERITANCE) ---")
for elem in model_elements:
    print(elem)
    