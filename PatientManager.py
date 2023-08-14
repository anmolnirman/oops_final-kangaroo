class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    @staticmethod
    def format_patient_info_for_file(patient):

        # This will format patient objects according to text file format.
        return f"{patient.pid}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}\n"

    @staticmethod
    def enter_patient_info():

        # ask user for patient info.
        pid = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")

        # convert patient properties to objects.
        patient = Patient(pid, name, disease, gender, age)
        return patient

    def read_patients_file(self):

        # This function will read or take data from patients.txt file
        with open("patients.txt", "r") as file:
            for line in file:
                pid, name, disease, gender, age = line.strip().split("_")
                patient = Patient(pid, name, disease, gender, age)
                self.patients.append(patient)

    def search_patient_by_id(self):

        # This function will get doctor's information by its pid.
        pid = input("Enter patient ID: ")
        for patient in self.patients:
            if patient.pid == pid:
                print("{:<5}{:<15}{:<15}{:<15}{:<15}".format("ID", "Name", "Disease", "Gender", "Age"))
                self.display_patient_info(patient)
                return
        print("Can't find the Patient with the same id on the system")

    @staticmethod
    def display_patient_info(patient):

        # This will format data and display data from patients.txt
        print("{:<5}{:<15}{:<15}{:<15}{:<15}"
              .format(patient.pid, patient.name, patient.disease, patient.gender, patient.age))

    def edit_patient_info_by_id(self):

        # This function is used to update information about any patient by taking inputs.
        pid = input("Please enter the id of the Patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.pid == pid:
                patient.name = input("Enter new name: ")
                patient.disease = input("Enter new disease: ")
                patient.gender = input("Enter new gender: ")
                patient.age = input("Enter new age: ")
                self.write_list_of_patients_to_file()
                print(f"Patient whose ID is {patient.pid} has been edited.")
                return
        print("Can't find the Patient with the same id on the system")

    def display_patients_list(self):
        for patient in self.patients:
            self.display_patient_info(patient)
            print()

    def write_list_of_patients_to_file(self):

        # This function can be used to make changes in patients.txt file
        with open("patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient))

    def add_patient_to_file(self):

        # This function is used to add new patient's information in text file.
        patient = self.enter_patient_info()
        self.patients.append(patient)
        with open("patients.txt", "a") as file:
            file.write(self.format_patient_info_for_file(patient))
        print(f"Patient whose ID is {patient.pid} has been added.")