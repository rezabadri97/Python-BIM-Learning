from pathlib import Path

project_path=Path("D:/Python BIM Learning/Warehouse_01")

models_folder=project_path/"models"
documantation=project_path/"documantation"
cad_file=models_folder/"Layout.dwg"

if models_folder.is_dir():
    print("Models folder exists.")
else:
    print("Model folder does`nt exsist.")

if documantation.is_dir():
    print("Documentation folder exists.")
else:
    print("Documentation folder does not exist.")

if cad_file.is_file():
    print("Cad file exists.")
else:
    print("Cad file does`nt exists.")
    