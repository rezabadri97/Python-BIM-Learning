from pathlib import Path

project_path=Path("D:/Python BIM Learning")

warehouse_path=project_path/"Warehouse_01"

models_path=warehouse_path/"models"
documantation_path=warehouse_path/"documantaion"

if not models_path.exists():
    models_path.mkdir(parents=True , exist_ok=True)
else:
    print(f"Folder already exists:{models_path}")

if not documantation_path.exists():
    documantation_path.mkdir(parents=True , exist_ok=True)
else:
    print(f"Folder already exists:{documantation_path}")

cad_file_path=models_path/"Layout.dwg"

print(f"Project Path: {warehouse_path}")
print(f"File name: {cad_file_path.name}")
print(f"File Suffix: {cad_file_path.suffix}")
print(f"Parent Path: {cad_file_path.parent}")