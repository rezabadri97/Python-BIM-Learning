import csv 
with open("bim_elements.csv" , "r" , encoding="utf-8" , newline="") as file:

    reader=csv.reader(file)

    header=next(reader)

    for row in reader :
        element_id=row[0]
        category=row[1]
        level=row[3]

        print(f"Element Id: {element_id} | Category: {category} | Level: {level}")
    