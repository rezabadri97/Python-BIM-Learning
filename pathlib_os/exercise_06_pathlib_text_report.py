from pathlib import Path

project_path = Path("D:/Python BIM Learning/Warehouse_01")

reports_path = project_path / "reports"
text_path = reports_path / "bim_model_status.txt"

reports_path.mkdir(parents=True, exist_ok=True)

text_path.write_text(
    "Project: Warehouse_01\n"
    "Model: Warehouse_Architecture.rvt\n"
    "Discipline: Architecture\n"
    "Status: In Progress",
    encoding="utf-8"
)

report_content = text_path.read_text(encoding="utf-8")

print("--- BIM MODEL STATUS ---")
print(report_content)
