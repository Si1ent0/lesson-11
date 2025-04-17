from selene.support.shared import browser

from lesson_11_tests.pages.student_registration_form import StudentRegistrationFormPage


class Application:
    def __init__(self):
        self.new_reg = StudentRegistrationFormPage()

app = Application()