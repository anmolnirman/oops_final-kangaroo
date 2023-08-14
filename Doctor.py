class Doctor:
    def __init__(self, doctor_id=None, name=None, speciality=None, timing=None, qualification=None, room_number=None):

        # This will define all doctors object
        self.doctor_id = doctor_id
        self.name = name
        self.speciality = speciality
        self.timing = timing
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id

    def set_doctor_id(self, new_doctor_id):
        self.doctor_id = new_doctor_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_speciality(self):
        return self.speciality

    def set_speciality(self, new_speciality):
        self.speciality = new_speciality

    def get_timing(self):
        return self.timing

    def set_timing(self, new_timing):
        self.timing = new_timing

    def get_qualification(self):
        return self.qualification

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def get_room_number(self):
        return self.room_number

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    def __str__(self):
        return f"{self.doctor_id: <5}_{self.name: <20}_{self.speciality: <15}_" \
               f"{self.timing: <15}_{self.qualification:<15}_{self.room_number: <10}"