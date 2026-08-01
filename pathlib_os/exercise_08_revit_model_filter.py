from pathlib import Path

project_path=Path("D:/Python BIM Learning/Warehouse_01/models")

for item in project_path.iterdir():
    if item.is_file() and item.suffix.lower()==".rvt":
        print(f"Revit model: {item.name}")
