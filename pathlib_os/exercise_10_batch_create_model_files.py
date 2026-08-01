from pathlib import Path

project_path=Path("D:/Python BIM Learning/Warehouse_01")
models_path=project_path/"models"

models_path.mkdir(parents= True , exist_ok= True)

model_files=[
"Warehouse_Architecture.rvt",
"Warehouse_Structure.rvt",
"Warehouse_MEP.rvt",
"Warehouse_Site.dwg",
"Warehouse_Coordination.ifc",
"model_notes.txt"
]
for item in model_files:
    model_path=models_path/item
    model_path.touch()
    print(f"Created file: {model_path.name}")