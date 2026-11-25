# Exercise 15: Class Attributes (Type Parameters) vs Instance Attributes & __str__


class RevitDoor:
    # Class attributes (shared across all instances, like Revit Type Parameters)
    category = "Doors"
    material = "Steel"

    def __init__(self, mark, level, width_m):
        # Instance attributes (unique per object, like Revit Instance Parameters)
        self.mark = mark
        self.level = level
        self.width_m = width_m

    def __str__(self):
        return (
            f"[{self.category}] Mark: {self.mark} | Level: {self.level} | "
            f"Width: {self.width_m} m | Material: {self.material}"
        )


door_1 = RevitDoor("D-101", "L01", 0.9)
door_2 = RevitDoor("D-102", "L01", 1.2)
door_3 = RevitDoor("D-201", "L02", 1.0)

model_doors = [door_1, door_2, door_3]

print("--- BEFORE EDIT TYPE ---")
for door in model_doors:
    print(door)

# Simulate Revit "Edit Type": update the class attribute once for all doors
RevitDoor.material = "Fire-Rated Wood"

print("\n--- AFTER EDIT TYPE (CLASS ATTRIBUTE UPDATED) ---")
for door in model_doors:
    print(door)