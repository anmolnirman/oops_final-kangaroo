class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    @staticmethod
    def format_dr_info(doctor):

        # This will format doctor objects according to text file format.
        return f"{doctor.doctor_id}_{doctor.name}_{doctor.speciality}_" \
               f"{doctor.timing}_{doctor.qualification}_{doctor.room_number}\n"

    @staticmethod
    def enter_dr_info():

        # ask user about doctor info
        doctor_id = input("Enter Doctor's ID: ")
        name = input("Enter Doctor's Name: ")
        speciality = input("Enter Doctor's Speciality: ")
        timing = input("Enter Doctor's Timing: ")
        qualification = input("Enter Doctor's Qualification: ")
        room_number = input("Enter Doctor's Room Number: ")

        # convert doctor properties into object
        doctor = Doctor(doctor_id, name, speciality, timing, qualification, room_number)
        return doctor

    def read_doctors_file(self):

        # This function will read or take data from doctors.txt file
        with open("doctors.txt", "r") as file:
            for line in file:
                doctor_id, name, speciality, timing, qualification, room_number = line.strip().split("_")
                doctor = Doctor(doctor_id, name, speciality, timing, qualification, room_number)
                self.doctors.append(doctor)

    def search_doctor_by_id(self):

        # This function will get doctor's information by its doctor_id
        doctor_id = input("Enter Doctor ID: ")
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                print("{:<5}{:<20}{:<15}{:<15}{:<15}{:<10}"
                      .format("ID", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
                self.display_doctor_info(doctor)
                return
        print("Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self):

        # This function will get doctor's information by its name
        name = input("Enter Doctor name: ")
        for doctor in self.doctors:
            if doctor.name == name:
                print("{:<5}{:<20}{:<15}{:<15}{:<15}{:<10}"
                      .format("ID", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
                self.display_doctor_info(doctor)
                return
        print("No doctor found with the given name.")

    @staticmethod
    def display_doctor_info(doctor):

        # This will format data and display data from doctors.txt
        print("{:<5}{:<20}{:<15}{:<15}{:<15}{:<10}"
              .format(doctor.doctor_id, doctor.name, doctor.speciality, doctor.timing,
                      doctor.qualification, doctor.room_number))

    def edit_doctor_info(self):

        # This function is used to update information about any doctor by taking inputs.
        doctor_id = input("Please enter the id of the doctor that you want to edit their information: ")
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                doctor.name = input("Enter new Name:  ")
                doctor.speciality = input("Enter the doctor speciality: ")
                doctor.timing = input("Enter the doctor timing: ")
                doctor.qualification = input("Enter the doctor qualification: ")
                doctor.room_number = input("Enter the doctor room number: ")
                self.write_list_of_doctors_to_file()
                print(f"Doctor whose ID is {doctor.doctor_id} has been edited")
                return
        print("Cannot find the Doctor...")

    def display_doctors_list(self):
        for doctor in self.doctors:
            self.display_doctor_info(doctor)
            print()

    def write_list_of_doctors_to_file(self):

        # This function can be used to make changes in doctors.txt file
        with open("doctors.txt", "w") as file:
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor))

    def add_dr_to_file(self):

        # This function is used to add new doctor's information in text file.
        doctor = self.enter_dr_info()
        self.doctors.append(doctor)
        with open("doctors.txt", "a") as file:
            file.write(self.format_dr_info(doctor))
        print(f"Doctor whose ID is {doctor.doctor_id} has been added")