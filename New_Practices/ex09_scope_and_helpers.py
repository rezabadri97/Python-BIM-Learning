# Exercise 09: Revit column reporter using helper functions and proper variable scope

main_model = "Hospital_Arch.rvt"
linked_struct_model = "Hospital_Struct_Link.rvt"


def feet_to_meters(feet_value):
    return round(feet_value * 0.3048, 2)


def create_column_report(column_id, height_ft, model_name="Hospital_Arch.rvt"):
    # Local variable calculated using the helper function
    height_m = feet_to_meters(height_ft)
    return f"[{model_name}] Column {column_id} | Height: {height_m} m"


report_1 = create_column_report(501, 10.5)
report_2 = create_column_report(502, 12.0, model_name=linked_struct_model)

print(report_1)
print(report_2)