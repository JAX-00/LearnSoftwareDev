from patient_utils import check_patient_status

# patient = {
#     "name" : "maria",
#     "age" : check_patient_status(26),
#     "temperature" : check_temperature(38.5)
# }
#
# print("Name :", patient["name"])
# print("Age Status :", patient["age"])
# print("Temperature Status:", patient["temperature"])

print(check_patient_status(-5))
print(check_patient_status(15))
print(check_patient_status(26))