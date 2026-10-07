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

# For
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

    # Latiha filter data
    if status == "Fever":
        print(
            patient["name"],
            "-",
            status
        )



