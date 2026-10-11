# function
def check_temperature(temperature):
    if temperature >= 37.5:
        return "Fever"
    else:
        return "Normal"

def check_patient_status(age):
    if age >= 18:
        return "Adult"
    else:
        return "Child"

# Data List -> Dictionary
patients = [
    {
        "name" : "Maria",
        "age" : 26,
        "temperature": 38.5
    },{
        "name" : "John",
        "age" : 17,
        "temperature": 36.5
    },{
        "name" : "Ana",
        "age" : 32,
        "temperature": 37.2
    },{
        "name" : "David",
        "age" : 19,
        "temperature": 39.5
    },
]

# 1. Menampilkan semua pasien
for patient in patients:
    age = check_patient_status(patient["age"])
    status = check_temperature(patient["temperature"])

    print(
        patient["name"],
        "-",
        age,
        "-",
        status
    )

    #

# 2. List Comprehension: pasien dewasa
adult_patients = [
    patient["name"]
    for patient in patients
    if check_patient_status(patient["age"]) == "Adult"
]

print("Adult patients:", adult_patients)


# Function
def check_temperature(temperature):
    if temperature >= 37.5:
        return "Fever"
    else:
        return "Normal"


def check_patient_status(age):
    if age >= 18:
        return "Adult"
    else:
        return "Child"


# Data: List of Dictionaries
patients = [
    {"name": "Maria", "age": 26, "temperature": 38.5},
    {"name": "John", "age": 17, "temperature": 36.5},
    {"name": "Ana", "age": 32, "temperature": 37.2},
    {"name": "David", "age": 19, "temperature": 39.5}
]


# 1. Menampilkan semua pasien
for patient in patients:
    age_status = check_patient_status(patient["age"])
    temperature_status = check_temperature(patient["temperature"])

    print(
        patient["name"],
        "-",
        age_status,
        "-",
        temperature_status
    )


# 2. List Comprehension: pasien dewasa
adult_patients = [
    patient["name"]
    for patient in patients
    if check_patient_status(patient["age"]) == "Adult"
]

print("Adult patients:", adult_patients)


# 3. List Comprehension: pasien demam
fever_patients = [
    patient["name"]
    for patient in patients
    if check_temperature(patient["temperature"]) == "Fever"
]

print("Fever patients:", fever_patients)


# 4. List Comprehension: pasien dewasa DAN demam
adult_fever_patients = [
    patient["name"]
    for patient in patients
    if check_patient_status(patient["age"]) == "Adult"
    and check_temperature(patient["temperature"]) == "Fever"
]

print("Adult patients with fever:", adult_fever_patients)















