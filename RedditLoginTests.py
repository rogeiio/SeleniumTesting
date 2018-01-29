from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


def goToSite():
    driver.get("https://www.reddit.com/")
    assert "reddit" in driver.title


def attemptLogin(loginUser, loginPwd):
    if isLoggedIn():
        return
    elem = driver.find_element_by_name('user')
    elem.send_keys(loginUser)
    elem = driver.find_element_by_name('passwd')
    elem.send_keys(loginPwd)
    elem.send_keys(Keys.RETURN)


def attemptLogout():
    if not isLoggedIn():
        return
    try:
        elem = driver.find_element_by_class_name('logout')
        elem.submit()
    except:
        return


# Check to see if user is logged in by looking for the login form
def isLoggedIn():
    try:
        driver.find_element_by_id('login_login-main')
        return False
    except:
        return True


# Scenario: User is unable to login
def loginFail():
    goToSite()
    assert isLoggedIn() == False
    attemptLogin('badUser', 'badPassword')
    time.sleep(2)
    assert isLoggedIn() == False


# Scenario: User successfully logs into account and logs out.
def loginSuccess():
    goToSite()
    assert isLoggedIn() == False
    attemptLogin('rogelioTesting', 'TestPassword')
    time.sleep(2)
    assert isLoggedIn() == True
    attemptLogout()
    assert isLoggedIn() == False


loginFail()
loginSuccess()
driver.close()
