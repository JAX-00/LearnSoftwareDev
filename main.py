from patient_utils import check_patient_status

patients = [
    {"name" : "Maria", "age" : 26, "temperature" : 38.5},
{"name" : "John", "age" : 17, "temperature" : 36.5},
{"name" : "Ana", "age" : 32, "temperature" : 37.2},
    {"name" : "David", "age": -2, "temperature": 39.5}
]

# loop for
for patient in patients:
    status = check_patient_status(patient["age"])

    if status == "Invalid Age":
        print(patient["name"], "-", status)
