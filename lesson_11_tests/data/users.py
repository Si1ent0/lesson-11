import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    subjects: str
    img: str
    address: str
    country: str
    city: str
    success_text: str

new_user = User(first_name='Egor', last_name='Letov', email='Letov_Perestroyka@home.ru',
            mobile='8123456789',
            subjects='Song and music',
            img='ava.png',
            address='Brighton Beach New York City',
            country='NCR',
            city='Delhi',
            success_text='Thanks for submitting the form'
               )

@dataclasses.dataclass
class UserInfo:
    label_values: str
    student_name: str
    student_email: str
    gender: str
    mobile: str
    date_of_birth: str
    subjects: str
    hobbies: str
    picture: str
    address: str
    state_and_city: str


user_info = UserInfo(
        label_values='Label Values',
        student_name='Student Name Egor Letov',
        student_email='Student Email Letov_Perestroyka@home.ru',
        gender='Gender Male',
        mobile='Mobile 8123456789',
        date_of_birth='Date of Birth 10 September,1964',
        subjects='Subjects',
        hobbies='Hobbies Music',
        picture='Picture ava.png',
        address='Address Brighton Beach New York City',
        state_and_city='State and City NCR Delhi'
    )