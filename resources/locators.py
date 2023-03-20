from selenium.webdriver.common.by import By


class LoginPageLocators:

    hudl_logo = (By.XPATH, "//*[@data-qa-id='hudl-logo']")
    email_input = (By.XPATH, "//*[@data-qa-id='email-input']")
    password_input = (By.XPATH, "//*[@data-qa-id='password-input']")
    login_btn = (By.XPATH, "//*[@data-qa-id='login-btn']")
    error_display = (By.XPATH, "//*[@data-qa-id='error-display']")
    need_help_link = (By.XPATH, "//*[@data-qa-id='need-help-link']")
    email_help_headline = (By.XPATH, "//*[@data-qa-id='email-help-headline']")
    back_arrow = (By.XPATH, "//span[contains(text(),'Back')]")
    back_arrow_org = (By.XPATH, "//*[@data-qa-id='go-back']")
    login_organization_btn = (By.XPATH, "//*[@data-qa-id='log-in-with-organization-btn']")
    login_org_title = (By.XPATH, "//h2[contains(text(),'Log into Hudl with your Organization')]")
    login_email_pswd_btn = (By.XPATH, "//*[@data-qa-id='log-in-with-email-and-password']")


class HomePageLocators:
    upload_btn = (By.XPATH, "//*[@data-qa-id='webnav-globalnav-upload']")
