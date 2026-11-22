# Exercise 04: ISO 19650 Revit Sheet Naming Auditor & Auto-Generator

PROJECT_CODE = "HOSP"
VALID_DISCIPLINES = {"ARC", "STR", "MEP"}
VALID_LEVELS = {"L00", "L01", "L02", "L03", "RF"}

raw_sheet_names = [
    "HOSP-ARC-L01-0001",
    " hosp-str-l02-0012 ",
    "HOSP-CIV-L01-0003",
    "HOSP-MEP-L05-0004",
    "HOSP-ARC-RF-12",
    "HOSP_ARC_L01_0005",
    "PROJ-ARC-L00-06",
]

valid_sheets = []
invalid_sheets = []

print("--- ISO 19650 REVIT SHEET NAMING AUDIT ---")

for index, raw_name in enumerate(raw_sheet_names, start=1):
    clean_name = raw_name.strip().upper()
    errors = []

    parts = clean_name.split("-")

    if len(parts) != 4:
        errors.append("Expected 4 parts separated by '-'")
    else:
        proj, disc, lvl, num = parts

        if proj != PROJECT_CODE:
            errors.append(f"Invalid project code '{proj}'")
        if disc not in VALID_DISCIPLINES:
            errors.append(f"Invalid discipline '{disc}'")
        if lvl not in VALID_LEVELS:
            errors.append(f"Invalid level '{lvl}'")
        if not (len(num) == 4 and num.isdigit()):
            errors.append(f"Sheet number '{num}' must be 4 digits")

    if not errors:
        valid_sheets.append(clean_name)
        print(f"[{index}] {clean_name} | Status: VALID")
    else:
        invalid_sheets.append(clean_name)
        error_text = "; ".join(errors)
        print(f"[{index}] {clean_name} | Status: INVALID -> {error_text}")

compliance_rate = round((len(valid_sheets) / len(raw_sheet_names)) * 100, 1)

print("\n--- AUDIT SUMMARY ---")
print(f"Total Sheets Audited: {len(raw_sheet_names)}")
print(f"Valid Sheets: {len(valid_sheets)}")
print(f"Invalid Sheets: {len(invalid_sheets)}")
print(f"Compliance Rate: {compliance_rate}%")

print("\n--- AUTO-GENERATE NEW ISO 19650 SHEET ---")

while True:
    disc_input = input("Enter Discipline (ARC/STR/MEP): ").strip().upper()
    if disc_input in VALID_DISCIPLINES:
        break
    print("Invalid discipline! Please try again.")

while True:
    lvl_input = input("Enter Level (L00/L01/L02/L03/RF): ").strip().upper()
    if lvl_input in VALID_LEVELS:
        break
    print("Invalid level! Please try again.")

next_num = 1
while True:
    formatted_num = str(next_num).zfill(4)
    new_sheet_name = f"{PROJECT_CODE}-{disc_input}-{lvl_input}-{formatted_num}"
    if new_sheet_name not in valid_sheets:
        break
    next_num += 1

valid_sheets.append(new_sheet_name)
print(f"Generated Unique ISO Sheet Name: {new_sheet_name}")
print(f"Updated Valid Sheets Count: {len(valid_sheets)}")