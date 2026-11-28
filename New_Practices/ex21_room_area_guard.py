# Drill 01 (ex21): RevitRoom @property Guard & Lambda Sorting


class RevitRoom:
    def __init__(self, number, name, area_m2):
        self.number = number
        self.name = name
        self._area_m2 = area_m2

    @property
    def area_m2(self):
        return self._area_m2

    @area_m2.setter
    def area_m2(self, new_area):
        if new_area <= 0:
            print(
                f"[WARNING] Room {self.number}: "
                f"Area must be > 0. Update rejected ({new_area} m2)."
            )
        else:
            self._area_m2 = new_area

    def __str__(self):
        return f"Room {self.number} - {self.name} | Area: {self.area_m2} m2"


def sort_rooms_by_area(rooms, descending=True):
    return sorted(rooms, key=lambda room: room.area_m2, reverse=descending)


# Create actual RevitRoom objects (instances), not plain lists
room_01 = RevitRoom("101", "Lobby", 45.0)
room_02 = RevitRoom("102", "Office", 22.5)
room_03 = RevitRoom("103", "Conference", 60.0)

rooms = [room_01, room_02, room_03]

# Test the property setter guard
room_02.area_m2 = -10.0

sorted_rooms = sort_rooms_by_area(rooms)

print("\n--- REVIT ROOMS RANKED BY AREA ---")
for rank, room in enumerate(sorted_rooms, start=1):
    print(f"[{rank}] {room}")
    