import allure

from allure_commons.types import Severity
from lesson_11_tests.Application import app
from lesson_11_tests.data import users


@allure.feature("Registry")
@allure.epic("Student reg")
@allure.story("Stud reg page")
@allure.label("owner", "RS")
@allure.tag("smoke", "regression", "web", "reg")
@allure.severity(Severity.CRITICAL)
@allure.link("https://demoqa.com/automation-practice-form", name="stud reg")
@allure.step("Отправка формы регистрации студента")
def test_send_practice_form_(browser_config):
    app.new_reg.open_stud_reg_page()
    app.new_reg.remove_baner_footer()
    app.new_reg.new_student_registration(users.new_user)
    app.new_reg.should_registered_user_with()
