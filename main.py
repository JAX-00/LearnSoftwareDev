from patient_utils import check_patient_status, check_temperature

patients = [
    {"name" : "Maria", "age" : 26, "temperature" : 38.5},
{"name" : "John", "age" : 17, "temperature" : 36.5},
{"name" : "Ana", "age" : 32, "temperature" : 37.2},
    {"name" : "David", "age": -2, "temperature": 39.5}
]

adult_fever_patients = []

# loop for
for patient in patients:
    age_status = check_patient_status(patient["age"])
    temperature_status = check_temperature(patient["temperature"])

    if age_status == "Adult" and temperature_status == "Fever":
        adult_fever_patients.append(patient["name"])
        print(patient["name"], "-", age_status, "-", temperature_status)

print(adult_fever_patients)