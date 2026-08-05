import json

with open("revit_elements_list.json", "r", encoding="utf-8") as file:
    data = json.load(file)

elements = data["Elements"]

for element in elements:
    if element["Category"] == "Door":
        print(f"Element ID: {element['ElementId']}")
        print(f"Type Name: {element['TypeName']}")
        print(f"Level: {element['Level']}")
        print("---")
