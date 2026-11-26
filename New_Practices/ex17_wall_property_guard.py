# Exercise 17: Encapsulation with @property and Setter Validation for Revit Wall


class RevitWall:
    def __init__(self, element_id, length_m, height_m):
        self.element_id = element_id
        self.length_m = length_m
        self._height_m = height_m

    @property
    def height_m(self):
        return self._height_m

    @height_m.setter
    def height_m(self, new_height):
        if new_height <= 0:
            print(
                f"[WARNING] Wall {self.element_id}: "
                f"Height must be > 0. Update rejected ({new_height} m)."
            )
        else:
            self._height_m = new_height

    def calculate_area(self):
        return round(self.length_m * self._height_m, 2)

    def __str__(self):
        return f"Wall {self.element_id} | Height: {self.height_m} m | Area: {self.calculate_area()} m2"


wall_1 = RevitWall(101, 6.0, 3.0)
print(f"Initial: {wall_1}")

wall_1.height_m = -2.5
print(f"After Invalid Update: {wall_1}")

wall_1.height_m = 4.0
print(f"After Valid Update: {wall_1}")