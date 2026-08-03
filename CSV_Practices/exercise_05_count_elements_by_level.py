import csv

level_counts = {}

with open("bim_elements.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        level = row["Level"]

        if level in level_counts:
            level_counts[level] += 1
        else:
            level_counts[level] = 1

for level, count in level_counts.items():
    print(f"{level}: {count}")
