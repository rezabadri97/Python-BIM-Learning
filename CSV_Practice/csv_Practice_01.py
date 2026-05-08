import csv
rows = [
    {"name": "Ali", "age": 25, "city": "Tehran"},
    {"name": "Sara", "age": 30, "city": "Shiraz"},
    {"name": "Reza", "age": 28, "city": "Tabriz"}
]

with open("Data_01.csv", "w",newline="",encoding="utf-8") as file:
   file_dict=["name", "age", "city"]
   writer=csv.DictWriter(file,fieldnames=file_dict)

   writer.writerows(rows)