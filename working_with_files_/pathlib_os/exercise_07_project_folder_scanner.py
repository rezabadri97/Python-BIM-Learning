from pathlib import Path

folder_path=Path("D:/Python BIM Learning/Warehouse_01")

for item in folder_path.iterdir():
    if item.is_dir():
        print(f"Folder Name: {item.name}")
    elif item.is_file():
        print(f"File Name: {item.name}")
