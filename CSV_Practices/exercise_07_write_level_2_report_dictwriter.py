import csv

fieldnames = ["ElementId", "Category", "TypeName", "Level"]

with open ("bim_elements.csv" , "r" , encoding="utf-8" , newline="") as input_file :
    reader = csv.DictReader(input_file)

    with open("level_2_elements_dict_report.csv" , "w" , encoding="utf-8" , newline="") as output_file :
        writer = csv.DictWriter(output_file , fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row["Level"] == "Level 2":
                writer.writerow({
                    "ElementId": row["ElementId"],
                    "Category": row["Category"],
                    "TypeName": row["TypeName"],
                    "Level": row["Level"]
                })