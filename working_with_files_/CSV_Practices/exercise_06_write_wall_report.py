import csv
with open ("bim_elements.csv" , "r" , encoding="utf-8" , newline="") as input_file :
    reader = csv.DictReader(input_file)

    with open("wall_elements_report.csv" , "w" , encoding="utf-8" , newline="") as file :
        writer = csv.writer(file)

        writer.writerow(["ElementId","Category","TypeName","Level"])

        for row in reader:
            if row["Category"] == "Wall" :
                writer.writerow([
                  row["ElementId"] ,  
                row["Category"],
                row["TypeName"],
                row["Level"]
                ]
                )