# function check age
def check_patient_status(age):
    if age >= 18:
        return "Adult"
    return "Child"

# Validation check use Try and Except
try:
    age = int(input("Enter patient age: "))
    print(check_patient_status(age))
except ValueError:
    print("Invalid age. Please enter a number.")

