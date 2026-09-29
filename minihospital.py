patients = []


def add_patient():

    print("\n========== ADD PATIENT ==========")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:
        if patient["id"] == patient_id:
            print("Patient ID already exists!")
            return

    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Gender: ")
    phone = input("Enter Phone Number: ")
    problem = input("Enter Patient Problem: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "problem": problem,
        "doctor": "Not Assigned",
        "department": "Not Assigned",
        "status": "Not Consulted"
    }

    patients.append(patient)

    print("\nPatient added successfully!")


def search_patient():

    print("\n========== SEARCH PATIENT ==========")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:

        if patient["id"] == patient_id:

            print("\nPatient Found!")
            print("------------------------------")
            print("Patient ID :", patient["id"])
            print("Name       :", patient["name"])
            print("Age        :", patient["age"])
            print("Gender     :", patient["gender"])
            print("Phone      :", patient["phone"])
            print("Problem    :", patient["problem"])
            print("Doctor     :", patient["doctor"])
            print("Department :", patient["department"])
            print("Status     :", patient["status"])
            print("------------------------------")

            return

    print("Patient not found.")


def display_patients():

    print("\n========== ALL PATIENTS ==========")

    if len(patients) == 0:
        print("No patient records available.")
        return

    for patient in patients:

        print("\n------------------------------")
        print("Patient ID :", patient["id"])
        print("Name       :", patient["name"])
        print("Age        :", patient["age"])
        print("Gender     :", patient["gender"])
        print("Problem    :", patient["problem"])
        print("Doctor     :", patient["doctor"])
        print("Department :", patient["department"])
        print("Status     :", patient["status"])
        print("------------------------------")


def assign_doctor():

    print("\n========== DOCTOR ASSIGNMENT ==========")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:

        if patient["id"] == patient_id:

            doctor = input("Enter Doctor Name: ")
            department = input("Enter Department: ")

            patient["doctor"] = doctor
            patient["department"] = department

            print("\nDoctor assigned successfully!")
            print("Doctor     :", doctor)
            print("Department :", department)

            return

    print("Patient not found.")


def update_status():

    print("\n========== CONSULTATION STATUS ==========")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:

        if patient["id"] == patient_id:

            print("\nChoose Consultation Status")
            print("1. Not Consulted")
            print("2. Waiting")
            print("3. In Consultation")
            print("4. Consultation Completed")

            choice = input("Enter your choice: ")

            if choice == "1":
                patient["status"] = "Not Consulted"

            elif choice == "2":
                patient["status"] = "Waiting"

            elif choice == "3":
                patient["status"] = "In Consultation"

            elif choice == "4":
                patient["status"] = "Consultation Completed"

            else:
                print("Invalid choice.")
                return

            print("\nConsultation status updated!")
            print("Current Status:", patient["status"])

            return

    print("Patient not found.")


def update_patient():

    print("\n========== UPDATE PATIENT ==========")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:

        if patient["id"] == patient_id:

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Phone Number")
            print("4. Problem")

            choice = input("Enter your choice: ")

            if choice == "1":

                patient["name"] = input("Enter new name: ")
                print("Name updated successfully.")

            elif choice == "2":

                patient["age"] = int(input("Enter new age: "))
                print("Age updated successfully.")

            elif choice == "3":

                patient["phone"] = input("Enter new phone number: ")
                print("Phone number updated successfully.")

            elif choice == "4":

                patient["problem"] = input("Enter new problem: ")
                print("Problem updated successfully.")

            else:
                print("Invalid choice.")

            return

    print("Patient not found.")


def delete_patient():

    print("\n========== DELETE PATIENT ==========")

    patient_id = input("Enter Patient ID: ")

    for patient in patients:

        if patient["id"] == patient_id:

            patients.remove(patient)

            print("Patient record deleted successfully.")

            return

    print("Patient not found.")


def total_patients():

    print("\n========== TOTAL PATIENTS ==========")

    print("Total number of patients:", len(patients))


while True:

    print("\n")
    print("==============================================")
    print("       MINI HOSPITAL MANAGEMENT SYSTEM")
    print("==============================================")

    print("1. Add Patient")
    print("2. Search Patient")
    print("3. Display All Patients")
    print("4. Assign Doctor and Department")
    print("5. Update Consultation Status")
    print("6. Update Patient Information")
    print("7. Delete Patient")
    print("8. Show Total Patients")
    print("9. Exit")

    print("==============================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        search_patient()

    elif choice == "3":
        display_patients()

    elif choice == "4":
        assign_doctor()

    elif choice == "5":
        update_status()

    elif choice == "6":
        update_patient()

    elif choice == "7":
        delete_patient()

    elif choice == "8":
        total_patients()

    elif choice == "9":
        print("\nThank you for using the Hospital Management System!")
        break

    else:
        print("\nInvalid choice. Please try again.")
