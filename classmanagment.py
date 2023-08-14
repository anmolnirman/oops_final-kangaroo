class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):

        # This will display instructions for user to use this command
        while True:
            print("Welcome to Alberta Hospital (AH) Management system ")
            print("Select from the following options, or select 3 to stop: ")
            print("1. Doctors")
            print("2. Patients")
            print("3. Exit")
            choice = input(">>> ")
            if choice == "1":
                while True:

                    # This will show instruction to user to get doctor's information.
                    # This will call functions from different class according to user's input.
                    print("Doctors Menu")
                    print("1. Display Doctors List")
                    print("2. Search Doctor by ID")
                    print("3. Search Doctor by Name")
                    print("4. Add New Doctor")
                    print("5. Edit Doctor Information")
                    print("6. Back to Main Menu")
                    choice = input(">>> ")
                    if choice == "1":
                        self.doctor_manager.display_doctors_list()
                    elif choice == "2":
                        self.doctor_manager.search_doctor_by_id()
                    elif choice == "3":
                        self.doctor_manager.search_doctor_by_name()
                    elif choice == "4":
                        self.doctor_manager.add_dr_to_file()
                    elif choice == "5":
                        self.doctor_manager.edit_doctor_info()
                    elif choice == "6":
                        break
                    else:
                        print("Invalid choice. Please try again.")

            elif choice == "2":
                while True:

                    # This will show instruction to user to get patient's information.
                    # This will call functions from different class according to user's input.
                    print("Patients Menu")
                    print("1. Display Patients List")
                    print("2. Search Patient by ID")
                    print("3. Add New Patient")
                    print("4. Edit Patient Information")
                    print("5. Back to Main Menu")
                    choice = input(">>> ")
                    if choice == "1":
                        self.patient_manager.display_patients_list()
                    elif choice == "2":
                        self.patient_manager.search_patient_by_id()
                    elif choice == "3":
                        self.patient_manager.add_patient_to_file()
                    elif choice == "4":
                        self.patient_manager.edit_patient_info_by_id()
                    elif choice == "5":
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif choice == "3":

                # This will end the program.Thank You!
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid choice. Please try again.")


Management().display_menu()