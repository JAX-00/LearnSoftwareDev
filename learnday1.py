def check_patient_status(age):
    # Menentukan status berdasarkan umur (misal: < 18 Anak-anak, >= 18 Dewasa)
    if age >= 18:
        return "Adult"
    else:
        return "Child"

def check_temperature(temperature):
    # Menentukan status demam (misal: >= 37.5 dianggap Demam/Fever)
    if temperature >= 37.5:
        return "Fever"
    else:
        return "Normal"

def main():
    # 1. Input dan Validasi Umur (Age)
    try:
        age_input = input("Enter patient age: ")
        age = int(age_input)  # Mencoba mengubah input menjadi angka bulat
    except ValueError:
        print("Invalid age. Please enter a number.")
        return # Menghentikan program agar tidak lanjut jika error

    # 2. Input dan Validasi Suhu (Temperature)
    try:
        temp_input = input("Enter temperature: ")
        temperature = float(temp_input)  # Mencoba mengubah input menjadi angka desimal
    except ValueError:
        print("Invalid temperature. Please enter a number.")
        return # Menghentikan program agar tidak lanjut jika error

    # 3. Input Nama (Tidak perlu try-except karena teks selalu valid)
    name = input("Enter patient name: ")

    # added validation feature
    if not name:
        print("invalid name.")
        return

    # 4. Memproses data menggunakan fungsi yang diminta
    status = check_patient_status(age)
    temp_status = check_temperature(temperature)

    # 5. Menampilkan Output Hasil
    print("\n--- Patient Registration ---")
    print(f"Patient: {name}")
    print(f"Status: {status}")
    print(f"Temperature: {temp_status}")

# Menjalankan program utama
if __name__ == "__main__":
    main()