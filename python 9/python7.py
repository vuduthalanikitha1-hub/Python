with open("test.txt", "w") as file:
    file.write("Python")
with open("test.txt", "r") as file:
    print(file.read())
with open("test.txt", "a") as file:
    file.write("\nProgramming")