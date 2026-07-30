with open("exercise_01_bim_text_logger.txt", "a",encoding="utf-8") as file:
    file.write("Status: Review Passed\n")
    file.write("Date:2026-07-30\n")
with open("exercise_01_bim_text_logger.txt","r",encoding="utf-8") as file:
    reader=file.read()
print(reader)