from patient_utils import check_patient_status, check_temperature

patient = {
    "name" : "maria",
    "age" : 26,
    "temperature" : 38.5
}

age_status = check_patient_status(patient["age"])
temperature_status = check_temperature(patient["temperature"])

print("Name:", patient["name"])
print("Age Status:", age_status)
print("Temperature Status:", temperature_status)

