import re
import os

pattern = r"\t\tVESSEL\n\t\t{(\n\t\t\t.+)+\n\t\t}"
patternPID = r"pid = .+"
patternName = r"name = .+"

path = input("Path to KSP save file: ").replace("\\", "/")
output = input("Path to output directory (Usually should be .../LMPServer/Universe/Vessels): ").replace("\\", "/")

overwrite = 0

with open(path, encoding="utf-8") as file:
    doc = "".join(file.readlines())

vessels = []

for match in re.finditer(pattern, doc, re.MULTILINE):
    result = match.group(0)
    
    cleaned = result.replace("\t\tVESSEL\n\t\t{\n\t\t\t", "")
    cleaned = cleaned.replace("\n\t\t}", "")
    cleaned = cleaned.replace("\n\t\t\t", "\n")
    
    vessels.append(cleaned)

    pid = re.search(patternPID, cleaned).group(0).replace("pid = ", "")
    name = re.search(patternName, cleaned).group(0).replace("name = ", "")

    if not os.path.exists(output):
        os.makedirs(output)
        print("Created output directory " + output)

    if os.path.exists(output + "/" + pid + ".txt"):

        if overwrite == 0:
            response = input("Vessel " + pid + " (" + name + ") already exists. Overwrite? (y/n/a) ").lower()
            if response == "y":
                print("Overwritting vessel " + pid + " (" + name + ")")
            elif response == "a":
                overwrite = 1
            elif response == "n":
                continue
            else:
                print("File not written.")
                continue
        else:
            print("Overwritting vessel " + pid + " (" + name + ")")
    else:
        print("Found vessel " + pid + " (" + name + ")")

    with open(output + "/" + pid + ".txt", "w", encoding="utf-8") as vesselFile:
        vesselFile.write(cleaned)
