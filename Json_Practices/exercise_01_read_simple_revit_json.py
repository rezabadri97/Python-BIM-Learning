import json

with open("revit_export_summary.json", "r", encoding="utf-8") as file:
    export_summary = json.load(file)

project_name = export_summary["ProjectName"]
exported_by = export_summary["ExportedBy"]
export_date = export_summary["ExportDate"]
total_elements = export_summary["TotalElements"]
has_warnings = export_summary["HasWarnings"]

print(f"Project Name: {project_name}")
print(f"Exported By: {exported_by}")
print(f"Export Date: {export_date}")
print(f"Total Elements: {total_elements}")
print(f"Has Warnings: {has_warnings}")
