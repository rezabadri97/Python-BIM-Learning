from pathlib import Path

project_path = Path("D:/Python BIM Learning/Warehouse_01")

models_path = project_path / "models"

file_path=models_path / "Warehouse_Coordination.ifc"

print(f"Full file name: {file_path.name}")
print(f"File name without extension: {file_path.stem}")
print(f"File extension: {file_path.suffix}")