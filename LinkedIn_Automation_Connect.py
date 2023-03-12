from selenium import webdriver
import time

# Set up Chrome driver
driver = webdriver.Chrome('C:/Users/anmol/ChromeDriver/chromedriver.exe')

# Navigate to LinkedIn
driver.get('https://www.linkedin.com')
time.sleep(2)

# login page
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

# Fill in the login credentials
username.send_keys('Enter_your_LinkedIn_Email/username')
password.send_keys('Enter_linkedIn_password')
time.sleep(4)

# Submit the login form
submit = driver.find_element_by_xpath("//button[@type='submit']").click()


# Navigate to the search results for 2nd degree connections
driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=14")

time.sleep(3)

# Click on the "Connect" buttons for a subset of search results
all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]


# Click on each "Connect" button and send a connection request
for button in connect_buttons:
    driver.execute_script("arguments[0].click();", button)
    time.sleep(3)
    try:
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        time.sleep(4)
    except:
        pass
    try:
        close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
        time.sleep(4)
    except:
        pass
