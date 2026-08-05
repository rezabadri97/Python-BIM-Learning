import json

with open("revit_elements_list.json", "r", encoding="utf-8") as file:
    data = json.load(file)

elements = data["Elements"]
filtered_elements = []

for element in elements:
    if element["Category"] == "Wall":
        filtered_elements.append(element)

output_data = {
    "FilteredCategory": "Wall",
    "Elements": filtered_elements
}

with open("wall_elements_report.json", "w", encoding="utf-8") as file:
    json.dump(output_data, file, indent=4, ensure_ascii=False)

print("Filtered JSON report created successfully.")
