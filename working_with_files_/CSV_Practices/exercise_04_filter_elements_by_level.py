import csv
with open("bim_elements.csv" , "r" , encoding="utf-8" , newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        element_id = row["ElementId"]
        category = row["Category"]
        type_name = row["TypeName"]
        level = row["Level"]

        if level=="Level 2" :

            print(f"Element Id: {element_id} | Element category: {category} | TypeName: {type_name} | Level: {level}")