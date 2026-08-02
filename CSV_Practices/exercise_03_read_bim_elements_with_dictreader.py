import csv
with open("bim_elements.csv" , "r" , encoding="utf-8" , newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        element_id = row["ElementId"]
        type_name = row["TypeName"]
        level = row["Level"]

        print(f"Element Id: {element_id} | TypeName: {type_name} | Level: {level}")