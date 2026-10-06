# function
def check_temperature(temperature):
    # Menentukan status demam (misal: >= 37.5 dianggap Demam/Fever)
    if temperature >= 37.5:
        return "Fever"
    else:
        return "Normal"

# List: bisa diubah dan bisa memiliki duplicate data
skills = ["python", "SQL", "Git"]
skills.append("Django")


# Tuple: tidak bisa diubah dan bisa memiliki duplicate
patient_info = ("Maria", 25)


# Set: bisa diubah dan tidak menyimpan duplicate
departments = {"General", "Pediatrics", "General"}
departments.add("Emergency")

#Temperature
temperature = 38.5

#Dictionary mengunakan key
patient = {
    "name" : "Maria",
    "age" : 25,
    "temperature" : temperature,
    "department" : "General",
    "status" : check_temperature(temperature),
    "contact" : {
        "phone": "7700000",
        "city": "Dili"
    }
}

# ubah data dictionary
patient["age"] = 26

print(skills)
print(patient)
print(departments)

print(patient["name"])
print(patient["age"])
print(patient["temperature"])
print(patient["contact"]["city"])
print(patient["contact"]["phone"])