from behave import *
from selenium import webdriver
import resources.locators
from pages.base_page import BasePage
from resources.locators import LoginPageLocators


@given('open chrome browser')
def open_browser(context):
    context.driver = webdriver.Chrome(executable_path=".\..\..\drivers\chromedriver.exe")
    context.page1 = BasePage(context.driver)


@when('navigate to hudl login page')
def nagivate_login_page(context):
    context.driver.get("https://www.hudl.com/login")


@then('verify hudl logo is present')
def verify_logo(context):
    context.page1.element_displayed(resources.locators.LoginPageLocators.hudl_logo)


@then('close browser')
def close_browser(context):
    context.driver.close()


@then('verify email input is present')
def email_input_presence(context):
    context.page1.element_displayed(resources.locators.LoginPageLocators.email_input)


@then('verify password input is present')
def password_input_presence(context):
    context.page1.element_displayed(resources.locators.LoginPageLocators.password_input)


@then('click on Login button')
def login_btn_click(context):
    context.page1.click(resources.locators.LoginPageLocators.login_btn)


@then('login error message appear')
def login_error_msg(context):
    context.page1.element_displayed(resources.locators.LoginPageLocators.error_display)


@then('click on Need help?')
def need_help_click(context):
    context.page1.click(resources.locators.LoginPageLocators.need_help_link)


@then('verify it navigated to Login Help')
def verify_log_help_page(context):
    context.page1.element_displayed(resources.locators.LoginPageLocators.email_help_headline)


@then('click on Back Arrow')
def back_arrow_click(context):
    context.page1.click(resources.locators.LoginPageLocators.back_arrow)


@then('click on Back Arrow Org')
def back_arrow_click(context):
    context.page1.click(resources.locators.LoginPageLocators.back_arrow_org)


@then('click on Log In with an Organization')
def login_organization_click(context):
    context.page1.click(resources.locators.LoginPageLocators.login_organization_btn)


@then('verify it navigated to Log into Hudl with your Organization')
def organization_login_page(context):
    context.page1.element_displayed(resources.locators.LoginPageLocators.login_org_title)


@then('click on Log In with Email and Password')
def login_email_pswd_btn(context):
    context.page1.click(resources.locators.LoginPageLocators.login_email_pswd_btn)


@then('insert email "{email}"')
def insert_email(context, email):
    context.page1.send_keys(resources.locators.LoginPageLocators.email_input, email)


@then('insert password "{password}"')
def insert_password(context, password):
    context.page1.send_keys(resources.locators.LoginPageLocators.password_input, password)


@then('validate you are in user homepage')
def validate_homepage_element(context):
    context.page2 = BasePage(context.driver)
    context.page2.url_changed("https://www.hudl.com/home")

