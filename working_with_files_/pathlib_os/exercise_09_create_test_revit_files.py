from pathlib import Path

project_path=Path("D:/Python BIM Learning/Warehouse_01")
models_path=project_path/"models"
models_path.mkdir(parents= True , exist_ok= True)

file_01=models_path/"Warehouse_Architecture.rvt"
file_02=models_path/"Warehouse_Structure.RVT"
file_03=models_path/"Site_Model.dwg"

file_01.touch()
file_02.touch()
file_03.touch()

print(f"File created: {file_01.name}")
print(f"File created: {file_02.name}")
print(f"File created: {file_03.name}")