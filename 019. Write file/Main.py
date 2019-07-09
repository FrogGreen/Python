# Write file

# First method to write file
f = open('localFile1.txt', 'w')
for i in range(10):
    f.write("localFile1, message" + str(i) + "\n")
f.close()
print("Writing localFile1 finished!\n")


# Second method to write file
with open('localFile2.txt', 'w') as f:
    for i in range(10):
        f.write("localFile2, message" + str(i) + "\n")
print("Writing localFile2 finished!\n")


# End of file
print()
input("Press Enter to continue...")