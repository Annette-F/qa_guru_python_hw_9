import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    mail: str
    gender: str
    user_number: str
    date_of_birth: str
    subject: str
    hobbies: str
    photo: str
    address: str
    state: str
    city: str

    def __init__(self, first_name, last_name, mail, gender, user_number, date_of_birth,
                 subject, hobbies, photo, address, state, city):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.gender = gender
        self.user_number = user_number
        self.date_of_birth = date_of_birth
        self.subject = subject
        self.hobbies = hobbies
        self.photo = photo
        self.address = address
        self.state = state
        self.city = city
