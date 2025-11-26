import time

from BaseSeleniumFramework.Utils import config
from OrangeHRMPOM.Application.Add_Employee.AddEmployee import AddEmployee
from OrangeHRMPOM.Application.Login.LoginPage import LoginPage
from conftest import driver
import BaseSeleniumFramework.Utils.config
import pytest

class Test_Add_Employee:
    def test_add_employee(self,driver):
        emp = AddEmployee(driver)
        emp.navigate_to_pim_menu()
        emp.navigate_to_add_employee_menu()
        emp.add_name(middlename="asp456",lastname="asp789")
        emp.upload_profile_picture(r"C:\MY SPACE\TEST GENERIC ASSETS\JLR Assets 1\Test_asp.jpeg")
        emp.toggle_switch_login_details()
        emp.enter_login_details(username="asp123",password="asp456",confirm_password= "asp456")
        emp.click_save_employee_button()




        

