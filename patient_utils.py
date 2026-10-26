def check_patient_status(age):
    if age < 0 :
        return "Invalid Age"
    elif age >= 18:
        return "Adult"
    return "Child"



# def check_temperature(temperature):
#     if temperature >= 37.5:
#         return "Fever"
#     return "Normal"