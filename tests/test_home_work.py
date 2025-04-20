import allure

from lesson_11_tests.Application import app
from lesson_11_tests.data import users

@allure.step("Отправка формы регистрации студента")
def test_send_practice_form_(browser_config):
    app.new_reg.open_stud_reg_page()
    app.new_reg.remove_baner_footer()
    app.new_reg.new_student_registration(users.new_user)
    app.new_reg.should_registered_user_with()
