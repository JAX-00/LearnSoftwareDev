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
patient = {
    "name" : "Maria",
    "age" : 26,
    "temperature" : 38.5
}

def create_patient_summary(patient):
    # Ambil nama pasient
    name = patient["name"]
    age_status = check_patient_status(patient["age"])
    temperature_check = check_temperature(patient["temperature"])

    return f"{name} is {age_status} and has {temperature_check}."

print(create_patient_summary(patient))