import json

revit_report={
    "ProjectName": "Residential Tower",
    "Software": "Revit 2026",
    "ExportedElements": 412,
    "HasClashes": False
}


with open("revit_report_output.json" , "w" , encoding="utf-8") as file:
    json.dump(revit_report, file, indent=4 , ensure_ascii=False)

print("JSON file created successfully.")