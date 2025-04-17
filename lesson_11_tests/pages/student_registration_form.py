import os

from selene import browser, be, have
from lesson_11_tests.data import users
from lesson_11_tests.data.users import User


new_user = users.new_user
user_info = users.user_info

class StudentRegistrationFormPage:
    def __init__(self):
        # Личные данные xpath
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('[for="gender-radio-1"]')
        self.user_number = browser.element('#userNumber')
        # Дата рождения xpath
        self.birthdate_form = browser.element('#dateOfBirthInput')
        self.month_cont = browser.element('.react-datepicker__month-container')
        self.month_select = browser.element('.react-datepicker__month-select')
        self.month_september = browser.element('//option[contains(text(), "September")]')
        self.year_select = browser.element('.react-datepicker__year-select')
        self.year = browser.element('//option[contains(text(), "1964")]')
        self.day_select = browser.element('//div[contains(text(), "10")]')
        # Хобби
        self.subject_cont = browser.element('#subjectsContainer')
        self.subject_input = browser.element('#subjectsInput')
        self.hobbies_checkbox = browser.element('[for="hobbies-checkbox-3"]')
        # Изображение
        self.send_upload_img = browser.element('#uploadPicture')
        # Личные данные xpath
        self.address = browser.element('#currentAddress')
        self.country= browser.element('#react-select-3-input')
        self.city= browser.element('#react-select-4-input')
        # Кнопка отправки формы xpath
        self.submit_button = browser.element('#submit')
        # Окно и уведомление об успешной отправке xpath
        self.send_popup = browser.element('.modal-content')
        self.success_submit_text = browser.element('.modal-title')
        # Кнопка закрытия окна об успешной регистрации
        self.button_close_pop_up = browser.element('#closeLargeModal')

    def open_stud_reg_page(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.should(be.blank).type(value)

    def fill_last_name(self, value):
        self.last_name.should(be.blank).type(value)

    def fill_email(self, value):
        self.email.should(be.blank).type(value)

    def select_gender(self):
        self.gender.click()

    def fill_user_number(self, value):
        self.user_number.should(be.blank).type(value)

    def fill_date_of_birth(self):
        self.birthdate_form.click()
        self.month_cont.should(be.visible)
        self.month_select.click()
        self.month_september.click()
        self.year_select.click()
        self.year.click()
        self.day_select.click()

    def fill_subject(self, value):
        self.subject_cont.click()
        self.subject_input.should(be.blank).type(value)

    def hobby_select(self):
        self.hobbies_checkbox.click()

    def upload_img(self, value):
        self.send_upload_img.send_keys(os.path.abspath(value))

    def fill_address(self,address, country, city):
        self.address.should(be.blank).type(address)
        self.country.set_value(country).press_tab()
        self.city.set_value(city).press_tab()

    def submit_form(self):
        self.submit_button.click()

    def success_form(self, value ):
        self.send_popup.should(be.visible)
        self.success_submit_text.should(have.text(value))

    def should_registered_user_with(self):
        browser.element('.table').all('tr').should(have.exact_texts(
            user_info.label_values,
        user_info.student_name,
        user_info.student_email,
        user_info.gender,
        user_info.mobile,
        user_info.date_of_birth,
        user_info.subjects,
        user_info.hobbies,
        user_info.picture,
        user_info.address,
        user_info.state_and_city
            )
        )

    def close_success_pop_up(self):
        self.button_close_pop_up.click()


    def new_student_registration(self, user: User):
        # Заполнение полей формы
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender()
        self.fill_user_number(user.mobile)
        self.fill_date_of_birth()
        self.fill_subject(user.subjects)
        self.hobby_select()
        self.upload_img(user.img)
        self.fill_address(user.address, user.country, user.city )
        self.submit_form()
        self.success_form(user.success_text)