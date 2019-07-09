# Read file

# First method to read file
f = open("localFile1.txt", "r")
file_data = f.read()
print(file_data)
f.close()
print("Finished reading localFile1\n")


# Second method to read file
with open("localFile2.txt", "r") as f:
    file_data = f.read()
print(file_data)
print("Finished reading localFile2\n")
	

# Third method to read file
with open("localFile3.txt") as f:
    print(f.read(11))
    print(f.read(10))
    print(f.read())
print("Finished reading localFile3\n")


# Fourth method to read file
f_lines = []
with open("localFile4.txt") as f:
    for line in f:
        firstPart = line.split(",")[0]
        secondPart = line.split(",")[1]
        f_lines.append(str(firstPart)+":" + str(secondPart))
for line in f_lines:
    print(line, end='')
print("Finished reading localFile4\n")


# End of file
print()
input("Press Enter to continue...")