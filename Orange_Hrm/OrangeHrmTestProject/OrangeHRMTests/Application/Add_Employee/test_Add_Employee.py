import time
import uuid

from BaseSeleniumFramework.Utils import config
from OrangeHRMPOM.Application.Add_Employee.AddEmployee import AddEmployee
from OrangeHRMPOM.Application.Login.LoginPage import LoginPage
from conftest import driver
import BaseSeleniumFramework.Utils.config
import pytest
from BaseSeleniumFramework.Helpers.DriverHelper import BasePage
from selenium.webdriver.common.by import By
import pytest_check as check
class Test_Add_Employee:

#test case for add employee with login details
    def test_add_employee(self, driver):
        emp = AddEmployee(driver)
        # ARRANGE
        first_name = "cleanuptest_" + uuid.uuid4().hex[:6]
        middle_name = "aspjkl6"
        last_name = "asp7jlhj9"

        username = "cleanuptest_user_" + uuid.uuid4().hex[:6]
        password = "Ideathon123"
        confirm_password = "Ideathon123"

        profile_pic_path = r"/Users/akshay.potdar/IDEATHON/prfile1.jpeg"

        # Navigation setup
        emp.navigate_to_pim_menu()
        emp.navigate_to_add_employee_menu()

        # ACT
        emp.add_name(
            firstname=first_name,
            middlename=middle_name,
            lastname=last_name
        )
        emp.upload_profile_picture(profile_pic_path)
        emp.toggle_switch_login_details()
        emp.enter_login_details(
            username=username,
            password=password,
            confirm_password=confirm_password
        )
        emp.click_save_employee_button()
        # ASSERT
        name_locator = (By.XPATH, "//div[@class='orangehrm-edit-employee-name']/h6")
        BasePage(driver).wait_for_element_presence(name_locator)
        time.sleep(2)
        displayed_name = driver.find_element(*name_locator).text
        print(displayed_name)
        check.is_true(displayed_name.startswith(first_name))



