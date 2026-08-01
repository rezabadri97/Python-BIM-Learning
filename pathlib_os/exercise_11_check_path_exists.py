from pathlib import Path

project_path = Path("D:/Python BIM Learning/Warehouse_01")

models_path = project_path / "models"

mep_file = models_path / "Warehouse_MEP.rvt"

fake_model_file = models_path / "Warehouse_Fake_Model.rvt"

if models_path.exists():
    print("Models folder exists.")
else:
    print("Models folder does not exist.")

if mep_file.exists():
    print("Warehouse_MEP.rvt exists.")
else:
    print("Warehouse_MEP.rvt does not exist.")

if fake_model_file.exists():
    print("Warehouse_Fake_Model.rvt exists.")
else:
    print("Warehouse_Fake_Model.rvt does not exist.")
