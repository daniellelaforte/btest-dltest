import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!
options = ChromeOptions()
#options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://bstackdemo.com')
    WebDriverWait(driver, 10).until(EC.title_contains('StackDemo'))
    get_url = driver.current_url
    print("The current url is:"+str(get_url))

    signin = driver.find_element(By.ID,'signin')

    signin.click();
    WebDriverWait(driver, 10).until(EC.title_contains('StackDemo'))
    get_url = driver.current_url
    print("The current url is:"+str(get_url))

    username = driver.find_element(By.ID, 'react-select-2-input')
    password = driver.find_element(By.ID, 'react-select-3-input')

    username.clear()
    password.clear()
    username.send_keys('demouser');
    username.send_keys(Keys.RETURN);
    password.send_keys('testingisfun99');
    password.send_keys(Keys.RETURN);

    try:
        loginbtn = driver.find_element(By.ID,'login-btn')
        ActionChains(driver).move_to_element(loginbtn).click().perform()
        print('Clickable')
    except:
        print('Not clickable')

    actualUrl="https://bstackdemo.com/?signin=true";
    wait = WebDriverWait(driver, 4)
    expectedUrl=driver.current_url;
    print("after sign in", driver.current_url)
    #assert expectedUrl == actualUrl;

    bike=driver.find_element(By.CSS_SELECTOR,"input[value='Samsung']");
    ActionChains(driver).move_to_element(bike).click().perform()

    unique_div = driver.find_element(By.ID, "11")
# Locate the button within the unique div (assuming it's the first button element)
    heart = unique_div.find_element(By.TAG_NAME, "button")

# Click the button
    heart.click()
    wait = WebDriverWait(driver, 4)
    favbutton = driver.find_element(By.ID, "favourites")
    favbutton.click()
    wait = WebDriverWait(driver, 4)

    try:
        isitthere = driver.find_element(By.ID, "11")
        print("it is there")
    except:
        print("it is not there")

finally:
    # Stop the driver
    driver.quit()
