# function
def check_patient_status(age):
    if age >=18:
        return "Adult"
    return "Child"

def check_temperature(temperature):
    if temperature >= 37.5:
        return "Fever"
    return "Normal"

# Data
patients = [
{
    "name" : "Maria",
    "age" : 26,
    "temperature" : 38.5
}, {
    "name" : "John",
    "age" : 17,
    "temperature" : 36.5
}, {
    "name" : "Ana",
    "age" : 32,
    "temperature" : 37.2
},{
    "name" : "David",
    "age" : 19,
    "temperature" : 39.5
}
]

def create_patient_summary(patient):
    # Ambil nama pasient
    name = patient["name"]
    age_status = check_patient_status(patient["age"])
    temperature_check = check_temperature(patient["temperature"])

    return f"{name} is {age_status} and has {temperature_check}."

for patient in patients:
    summary = create_patient_summary(patient)
    print(summary)

