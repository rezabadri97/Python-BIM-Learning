from pathlib import Path

project_path = Path("D:/Python BIM Learning/Warehouse_01")

models_path = project_path / "models"

old_path=models_path / "Warehouse_Coordination.ifc"

new_path=models_path / "Warehouse_01_Coordination.ifc"

old_path.rename(new_path)

print(f"Renamed file: {old_path.name} -> {new_path.name}")