student = {
    "name": "Navya",
    "age": 20,
    "course": "Python"
}

print(student)

print(student["name"])
print(student["age"])

student["age"] = 21

print(student)

student["city"] = "Hyderabad"

print(student)

for key, value in student.items():
    print(key, value)