file_name="exercise_01_bim_text_logger.txt"
with open(file_name,"w",encoding="utf-8") as file:
    file.write("Project: Residential Tower\n")
    file.write("Discipline: Structure\n")
    file.write("LOD: 300\n")
    file.write("Author: Reza Badri\n")
with open(file_name,"r",encoding="utf-8") as file:
    reader=file.read()
print(reader)