import json

input_file = "revit_elements_list.json"
output_file = "bim_json_quality_report.json"

required_fields = ["ElementId", "Category", "TypeName", "Level"]

try:
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    elements = data["Elements"]

    category_counts = {}
    missing_field_elements = []

    for element in elements:
        category = element.get("Category", "Unknown")
        category_counts[category] = category_counts.get(category, 0) + 1

        for field in required_fields:
            if field not in element:
                missing_field_elements.append(element)
                break

    output_data = {
        "ReportName": "BIM JSON Quality Report",
        "TotalElements": len(elements),
        "CategoryCounts": category_counts,
        "RequiredFields": required_fields,
        "MissingFieldElementCount": len(missing_field_elements),
        "MissingFieldElements": missing_field_elements
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(output_data, file, indent=4, ensure_ascii=False)

    print("BIM JSON quality report created successfully.")

except FileNotFoundError:
    print("Input file was not found.")

except json.JSONDecodeError:
    print("Input file is not a valid JSON file.")

except KeyError:
    print("Elements key was not found in the JSON file.")
