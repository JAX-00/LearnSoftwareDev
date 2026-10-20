# function check age take from other file
from learn3 import check_patient_status

# Validation check use Try and Except
try:
    age = int(input("Enter patient age: "))

    # validasi nilai input
    if age < 0:
        print("Age cannot be negative")
    else:
        print(check_patient_status(age))

except ValueError:
    print("Invalid age. Please enter a number.")

