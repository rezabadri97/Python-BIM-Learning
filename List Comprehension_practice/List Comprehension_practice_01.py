elements = [
    {"id": 1, "name": "Wall A", "category": "Wall"},
    {"id": 2, "name": "Door B", "category": "Door"},
    {"id": 3, "name": "Wall C", "category": "Wall"}
]
new={item["id"] : item["name"] for item in elements if item["category"]=="Wall"}
print(new)