import csv

quality_fieldnames = [
    "ElementId",
    "Category",
    "TypeName",
    "Level",
    "ReviewStatus",
    "Priority",
    "ActionRequired"
]

summary_fieldnames = ["Level", "Count"]
level_counts = {}

with open("bim_elements.csv", "r", encoding="utf-8", newline="") as input_file:
    reader = csv.DictReader(input_file)

    with open("bim_quality_control_report.csv", "w", encoding="utf-8", newline="") as quality_file:
        quality_writer = csv.DictWriter(quality_file, fieldnames=quality_fieldnames)

        quality_writer.writeheader()

        for row in reader:
            element_id = row["ElementId"]
            category = row["Category"]
            type_name = row["TypeName"]
            level = row["Level"]

            if category == "Wall":
                review_status = "Structural Review"
            elif category == "Door":
                review_status = "Opening Review"
            elif category == "Window":
                review_status = "Facade Review"
            elif category == "Floor":
                review_status = "Slab Review"
            else:
                review_status = "General Review"

            if level == "Level 1":
                priority = "High"
            elif level == "Level 2":
                priority = "Normal"
            else:
                priority = "Low"

            if category == "Wall" and level == "Level 1":
                action_required = "Check Load Bearing Condition"
            elif category == "Door":
                action_required = "Check Opening Size"
            elif category == "Window":
                action_required = "Check Sill Height"
            else:
                action_required = "No Immediate Action"

            quality_writer.writerow({
                "ElementId": element_id,
                "Category": category,
                "TypeName": type_name,
                "Level": level,
                "ReviewStatus": review_status,
                "Priority": priority,
                "ActionRequired": action_required
            })

            if level in level_counts:
                level_counts[level] += 1
            else:
                level_counts[level] = 1

with open("level_summary_report.csv", "w", encoding="utf-8", newline="") as summary_file:
    summary_writer = csv.DictWriter(summary_file, fieldnames=summary_fieldnames)

    summary_writer.writeheader()

    for level, count in level_counts.items():
        summary_writer.writerow({
            "Level": level,
            "Count": count
        })
