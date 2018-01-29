# import needed webdriver from selenium
from selenium import webdriver

# import keys to let the driver "Press" the Return key
from selenium.webdriver.common.keys import Keys

# import time to allow driver to sleep for a few seconds after attempting to login
import time

# provide working username and password when running
USER_NAME = ''
PASSWORD = ''
driver = webdriver.Chrome()


# Go to the website and make sure it is the correct site
def goToSite():
    driver.get("https://www.reddit.com/")
    assert "reddit" in driver.title


# attempt to login to the site using the provided user and password
def attemptLogin(loginUser, loginPwd):
    # no need to try to log in if the user is already logged in
    if isLoggedIn():
        return
    elem = driver.find_element_by_name('user')
    elem.send_keys(loginUser)
    elem = driver.find_element_by_name('passwd')
    elem.send_keys(loginPwd)
    elem.send_keys(Keys.RETURN)


# attempt to logout of the site
def attemptLogout():
    # no need to try to logout if the user is not logged in
    if not isLoggedIn():
        return

    # submit logout form if it exists
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
    attemptLogin(USER_NAME, PASSWORD)
    time.sleep(2)
    assert isLoggedIn() == True
    attemptLogout()
    assert isLoggedIn() == False


loginFail()
loginSuccess()
driver.close()
